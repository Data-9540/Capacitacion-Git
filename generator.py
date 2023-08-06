from random import randint
from random import random
import numpy as np
import cv2

ext = ["js","txt","c","cpp","php","tex","py"]
comment = ["//","*","//","//","//","% ","#"]
for i in range(60000):
  j = randint(0, 6)
  with open("file"+str(i)+"."+ext[j], 'w') as f:
      f.write(comment[j]+"Hola soy un comentario con id:"+str(i)+"!")

img = cv2.imread("lena.jpg", cv2.IMREAD_COLOR)
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2=np.zeros_like(RGB_img)
for i in range(2000):
    a = random()
    b = random()
    c = random()
    img2[:,:,0] = a*RGB_img[:,:,0] + b*RGB_img[:,:,1] + RGB_img[:,:,2]
    img2[:,:,1] = a*RGB_img[:,:,0] + RGB_img[:,:,1] + c*RGB_img[:,:,2]
    img2[:,:,2] = RGB_img[:,:,0] + b*RGB_img[:,:,1] + c*RGB_img[:,:,2]
    cv2.imwrite("lena"+str(i)+".jpg",img2)
