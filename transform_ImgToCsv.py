import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import pandas as pd  

f = [x[0] for x in os.walk(".")]
y = []
for x in f[12::]:
    if not ("validation" in x or "training" in x or "test" in x):
        y.append(x.replace(".\\", ""))
print(y)
listafinal = []
i = 0
j = 0
for x in y[::2]:
    for file in os.listdir(x):
        try:
            my_img = cv2.imread(x + '/' + file, 0) 
            inverted_img = (255.0 - my_img)  
            final = resized = cv2.resize(inverted_img, (24, 24))
            elemento = final.flatten().tolist()
            elemento.append(x)
            listafinal.append(elemento)
            i +=1
            print(i)
            if(i > 10000):
                j +=1
                np.savetxt("file"+str(j)+".csv", listafinal, delimiter=",", fmt='%s')
                i =0
                listafinal = []
        except:
            print("EXCEPTION: " + x + '/' + file)

np.savetxt("file"+str(j)+".csv", listafinal, delimiter=",", fmt='%s')