import torch
import numpy as np
a = torch.Tensor([1.,2.,3.])
a.requires_grad = True
print(a.requires_grad)
b = a.clone()  #不修改requires_grad属性
print(b.requires_grad)
c = a.detach() #修改修改requires_grad属性为False
print(c.requires_grad)
b+=1  #原位运算不影响被克隆tensor
print(a)
c+=1  #原位运算影响被克隆tensor,以及之前克隆出的tensor
print(a)
print(b)

cat = torch.cat((a.unsqueeze(0),b.unsqueeze(0)),dim = 0)
del a,b #cat后可以删除被cat的tensor
print(cat)

name = str(np.random.randint(0,100))
print(name)
