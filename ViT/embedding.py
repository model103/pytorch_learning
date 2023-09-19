# Embedding层代码解读
#把image转成一个个token
class PatchEmbed(nn.Module):
    """
    2D Image to Patch Embedding
    """

    def __init__(self, img_size=224, patch_size=16, in_c=3, embed_dim=768, norm_layer=None):
        super().__init__()
        img_size = (img_size, img_size)
        patch_size = (patch_size, patch_size)
        self.img_size = img_size=224
        self.patch_size = patch_size  # 每个patch的大小=16
        self.grid_size = (img_size[0] // patch_size[0], img_size[1] // patch_size[1])  # 224/16 -> 14*14
        self.num_patches = self.grid_size[0] * self.grid_size[1]  # patches(token)的数目
        #直接用步长=kerbel_size的卷积把全部patch映射成[B,768,14,14],即14*14个token，每个token长768
        self.proj = nn.Conv2d(in_c, embed_dim, kernel_size=patch_size, stride=patch_size)  # 卷积核大小和patch_size都是16*16
        self.norm = norm_layer(embed_dim) if norm_layer else nn.Identity()  # 如果没有传入norm层，就使用identity

    def forward(self, x):
        B, C, H, W = x.shape  #[B,3,224,224] 注意，在vit模型中输入大小必须是固定的，高宽和设定值相同
        assert H == self.img_size[0] and W == self.img_size[1], \
            f"Input image size ({H}*{W}) doesn't match model ({self.img_size[0]}*{self.img_size[1]})."

        # flatten: [B, C, H, W] -> [B, C, HW]
        # transpose: [B, C, HW] -> [B, HW, C]
        x = self.proj(x).flatten(2).transpose(1, 2)
        x = self.norm(x)
        return x