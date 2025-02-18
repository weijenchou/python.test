import numpy as np
import cv2
"""
pip install opencv-python
"""
#print(cv2.__version__)

#取自己的圖片(JPG/PNG)
img = cv2.imread(r"C:\Users\user\Desktop\AI Python\dumplings.jpg")
#cv2.imshow('Usagi',img) #用OpenCV顯示，放視窗標題跟圖片物件

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#resized_image= cv2.resize(gray_img, (int(gray_img.shape[1]*0.5),int(gray_img.shape[1]*0.5)))
cv2.imshow('Usagi_gray', gray_img) 

kernel = np.array(([0, 0, 0],
                   [0, 1.4, 0],
                   [0, 0, 0],))

#filter_img = cv2.filter2D(gray_img, -1, kernel)
#cv2.imshow('Usagi_gray_filter', filter_img)

cv2.waitKey(0) #按任一鍵後才執行下一輪
cv2.destroyAllWindows() #關閉所有視窗

import matplotlib.pyplot as plt
from scipy import signal

#matrix_img = np.array(img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_RGB2RGB)
plt.imshow(matrix_img)
plt.show()

kernels = np.array([
   [[-1,-1,-1],
    [1, 1, 1],
    [0, 0, 0]],
   [[-1, 1, 0],
    [-1, 1, 0],
    [-1, 1, 0]],
])

#設定圖片大小
plt.figure(figsize= (12,8))

#設定圖片放置規則
plt.subplot(1, 5, 1)
"""
圖片排列方式及圖片位置:
座位有1列 5個位置 此img要放在第1張的位置 -> (1,5,1)
+-------+-------+-------+-------+-------+
|  Img1 |  Img2 |  Img3 |  Img4 | Img5
+-------+-------+-------+-------+-------+

"""
plt.imshow(img_rgb)
plt.axis('off')
plt.title('Origin')
img_gray= cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

for i in range(len(kernels)):
    plt.subplot(1, 5 ,i+2)
    filter_img= signal.convolve2d(img_gray, kernels[i]) #做濾波
    plt.imshow(filter_img, cmap= 'gray')
    plt.axis('off')
    plt.title(f'filter{i+1}')


plt.show()