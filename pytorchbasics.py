#!/usr/bin/env python3
import torch
from torch.autograd import Variable
import torch.nn as nn

## Example 1 - variable and grad 
x = variable(torch.IntTorch([4],requires_grad = True)
y = variable(torch.IntTorch([6],requires_grad = True)
             
z = y**2+x+1
z.backward()

print(x.grad)
print(y.grad)
						 
## Example 2 - linear regression
             
