# eniguma_sim
This is 3 rotors eniguma simulater

```python

import string
import random
import sys

class enigma():
  c1,c2,c3 = 0,0,0
  
  def __init__(self, s1, s2, s3, seed = 100):
    self.s1, self.s2, self.s3 = s1, s2, s3
    self.seed = seed

    alpha = list(string.ascii_uppercase)
    random.seed(a=self.seed, version=2)
    self.R1 = random.sample(alpha, 26)
    self.R2 = random.sample(alpha, 26)
    self.R3 = random.sample(alpha, 26)
    self.ref = random.sample(list(string.ascii_uppercase)[0:13]*2, 26)
    self.inout = alpha.copy()

    self.i1, self.i2, self.i3 = alpha.copy(), alpha.copy(), alpha.copy()
    self.r1 = self.R1.copy()
    self.r2 = self.R2.copy()
    self.r3 = self.R3.copy()
    for _ in range(alpha.index(self.s1)): self.r1.append(self.r1.pop(0)), self.i1.append(self.i1.pop(0))
    for _ in range(alpha.index(self.s2)): self.r2.append(self.r2.pop(0)), self.i2.append(self.i2.pop(0))
    for _ in range(alpha.index(self.s3)): self.r3.append(self.r3.pop(0)), self.i3.append(self.i3.pop(0))

  def rotation(self):
    self.c3 += 1
    self.r3.append(self.r3.pop(0))
    self.i3.append(self.i3.pop(0))
    if self.c3 >= 26:
      self.c3 = 0
      self.c2 += 1
      self.r2.append(self.r2.pop(0))
      self.i2.append(self.i2.pop(0))
      if self.c2 >= 26:
        self.c2 = 0
        self.c1 += 1
        self.r1.append(self.r1.pop(0))
        self.i1.append(self.i1.pop(0))

  def typing(self,strings):
    self.rotation()
    self.str1 = strings
    #print(str1)
    if (len(self.str1) != 1):
      print("error")
      sys.exit()
    ##forword
    self.x_f3 = self.r3[self.inout.index(self.str1)]
    self.y_f3 = self.i3.index(self.x_f3)
    #print(self.x_f3)
    self.x_f2 = self.r2[self.y_f3]
    self.y_f2 = self.i2.index(self.x_f2)
    #print(self.x_f2)
    self.x_f1 = self.r1[self.y_f2]
    self.y_f1 = self.i1.index(self.x_f1)
    #print(self.x_f1)
    ##refrector
    self.x_r = self.ref[self.y_f1]
    self.y_r = [n for n, v in enumerate(self.ref) if (v == self.x_r)&(n != self.y_f1)][0]
    #print(self.x_r)
    ##backword
    self.x_b1 = self.i1[self.y_r]
    self.y_b1 = self.r1.index(self.x_b1)
    #print(self.x_b1)
    self.x_b2 = self.i2[self.y_b1]
    self.y_b2 = self.r2.index(self.x_b2)
    #print(self.x_b2)
    self.x_b3 = self.i3[self.y_b2]
    self.y_b3 = self.r3.index(self.x_b3)
    #print(self.x_b3)
    ##output
    self.x_o = self.inout[self.y_b3]
    return(self.x_o)

  def print(self,ptype = 0):
    if ptype == 0:
      print(self.str1,"->",self.x_f3,"->",self.x_f2,"->",self.x_f1,"->",self.x_r,"->",self.x_b1,"->",self.x_b2,"->",self.x_b3,"->",self.x_o)
    else:
      print(self.str1,"->",self.x_o)


```
