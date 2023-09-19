
import torch
import torch.nn.functional as F


def forward_fuse(feats):
    feats = list(feats)
    feats[0] = feats[0].unsqueeze(1)
    for i in range(1, len(feats)):
        feats[i] = F.interpolate(feats[i], scale_factor=2 ** i, mode='nearest')
        feats[i] = feats[i].unsqueeze(1)
        print(feats[i].shape)
    feats = torch.cat(feats, dim=1)
    feats = feats.mean(dim=1)
    return feats

a = torch.rand((2,5,3,3)).cuda()

forward_fuse(a)