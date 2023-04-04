# -2
图像几何变换 （图像图像平移、镜像、旋转及其复合） 
一、图像平移：图像平移是将图像中的所有像素点按照给定的平移量进行水平或垂直方向上的移动。假设原始像素的位置坐标为（x0，y0），经过平移量（△x，△y）后，坐标变为（x1, y1） ![~RA }E~F9NL0JEP3F`O4YR6](https://user-images.githubusercontent.com/98206033/229677578-865aac4c-d776-490c-8c0d-cb15cba5adf8.png)

如图所示，下图图像平移，它定义了图像平移矩阵M，然后调用warpAffine()函数将原始图像垂直向下平移了100个像素，水平向右平移了200个像素。  
![U2S{Z__T4J`}1 %{$4FJF L](https://user-images.githubusercontent.com/98206033/229677417-30f84581-2921-4f29-a28c-55220cd30f48.png)    
二、图像镜像  
图像镜像是图像旋转变换的一种特殊情况，通常包括垂直方向和水平方向的镜像。水平镜像通常是以原图像的垂直中轴为中心，将图像分为左右两部分进行堆成变换。  
在Python中主要调用OpenCV的flip()函数实现图像镜像变换，函数原型如下：

dst = cv2.flip(src, flipCode)
– src表示原始图像
– flipCode表示翻转方向，如果flipCode为0，则以X轴为对称轴翻转，如果fliipCode>0则以Y轴为对称轴翻转，如果flipCode<0则在X轴、Y轴方向同时翻转。
下图是实现三个方向的镜像  
![G59%~ 4_`8PYWFVYOIZF`76](https://user-images.githubusercontent.com/98206033/229681910-9091650d-32d6-4928-9cff-695565da2ac1.png)
