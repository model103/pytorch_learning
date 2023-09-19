import torch.nn as nn
import torch
class BatchNorm2d(nn.Module):
    def __init__(self,c, mount = 0.1):
        '''
        :param c:通道数
        '''
        super(BatchNorm2d,self).__init__()
        self.beta = nn.Parameter(torch.zeros(1,c,1,1))  #初始化科学性参数beta
        self.gama = nn.Parameter(torch.ones(1,c,1,1))
        self.register_buffer('mean', torch.zeros(1,c,1,1)) #初始化滑动平均法的mean,不可学习
        self.register_buffer('var', torch.one(1, c, 1, 1))
        self.mount = mount

    def forward(self,x):
        current_mean = x.mean(dim=(0, 2, 3), keepdim='ture')
        current_var = ((x - current_mean) ** 2).mean(dim=(0, 2, 3), keepdim='ture')
        if self.training:
            self.mean = (1-self.mount)*self.mean + self.mount*current_mean
            self.var = (1-self.var)*self.var + self.mount*current_var
        return (x-current_mean)/torch.sqrt(current_var)
