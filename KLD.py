import torch
import numpy as np
gt = torch.rand(3)
gt = gt/torch.sum(gt)
pb = torch.rand(3)
pb = pb/torch.sum(pb)

def KLD(gt,pb):
    '''
    :param gt: 真实标签
    :param pb: 预测标签
    :return: kl散度
    '''
    return torch.mean(gt*torch.log(gt/pb))
print(gt)
print(pb)
print(KLD(gt,pb))
