# 代码解读
#https://zhuanlan.zhihu.com/p/418184940
class Attention(nn.Module):  # Multi-head selfAttention 模块
    def __init__(self,
                 dim,  # 输入token的dim #一般为16*16*3=768
                 num_heads=8,  # head的个数
                 qkv_bias=False,  # 生成qkv时是否使用偏置
                 qk_scale=None,
                 attn_drop_ratio=0.,  # 两个dropout ratio
                 proj_drop_ratio=0.):
        super(Attention, self).__init__()
        self.num_heads = num_heads
        head_dim = dim // num_heads  # 每个head的dim=96
        self.scale = qk_scale or head_dim ** -0.5  # 不去传入qkscale，也就是1/√dim_k=1/√96
        #nn.Linear只改变输入tensor的最后一个维度
        self.qkv = nn.Linear(dim, dim * 3, bias=qkv_bias)  # 使用一个全连接层，一次得到qkv，代替了三次1*1卷积
        self.attn_drop = nn.Dropout(attn_drop_ratio)
        self.proj = nn.Linear(dim, dim)  # 把多个head进行Concat操作，然后通过Wo映射，这里用全连接层代替
        self.proj_drop = nn.Dropout(proj_drop_ratio)

    def forward(self, x):
        # [batch_size, num_patches + 1, total_embed_dim] 加1代表类别，针对ViT-B/16，dim是768
        B, N, C = x.shape  #N一般为14*14+1,即token个数+1，patch个数+1，C为768

        # qkv(): -> [batch_size, num_patches + 1, 3 * total_embed_dim]
        # reshape: -> [batch_size, num_patches + 1, 3（代表qkv）, num_heads（代表head数）, embed_dim_per_head（每个head的qkv维度）]
        #最后两个维度，相当于把原本长度为C=768的token均分成了8个token，每个长96
        # permute: -> [3, batch_size, num_heads, num_patches + 1, embed_dim_per_head]
        #[3,B,8,197,96]
        qkv = self.qkv(x).reshape(B, N, 3, self.num_heads, C // self.num_heads).permute(2, 0, 3, 1, 4)
        # [batch_size, num_heads, num_patches + 1, embed_dim_per_head]
        q, k, v = qkv[0], qkv[1], qkv[2]  # make torchscript happy (cannot use tensor as tuple)
        #即qkv均为[B,8,197,96],8个头，197个token，每个token长96

        # transpose: -> [batch_size, num_heads, embed_dim_per_head, num_patches + 1] = [B,8,96,197]
        # @: multiply -> [batch_size, num_heads, num_patches + 1, num_patches + 1] = [B,8,197,197]
        #因为是矩阵乘法，后两个维度[197,197]内每个元素都是96个乘积的和，所以需要除√96 ？
        attn = (q @ k.transpose(-2, -1)) * self.scale  # 每个header的q和k相乘，除以√dim_k（相当于norm处理）
        attn = attn.softmax(dim=-1)  # 通过softmax处理（相当于对每一行的数据softmax）[B,8,197,197]，每一行之和为1
        attn = self.attn_drop(attn)  # dropOut层 #将*%的元素置0，其他元素乘上1/*%，保证和不变

        #上一步得到的注意力图attn和v相乘，并转化到和输入一样的形状[B,197,768]（或者说是把8个头合成一个头）
        # @: multiply -> [batch_size, num_heads, num_patches + 1, embed_dim_per_head] = [B,8,197,96]
        # transpose: -> [batch_size, num_patches + 1, num_heads, embed_dim_per_head] = [B,197,8,96]
        # reshape: -> [batch_size, num_patches + 1, total_embed_dim] = [B,197,768]
        x = (attn @ v).transpose(1, 2).reshape(B, N, C)  # 得到的结果和V矩阵相乘（加权求和），reshape相当于把head拼接
        # 此处线性层的作用的是将8个头的特征进行融合，因为上一步reshape相当于concat，各个head的特征图仍然是分离的
        x = self.proj(x)  # 通过全连接进行映射（相当于乘论文中的Wo）
        x = self.proj_drop(x)  # dropOut
        return x