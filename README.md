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
图像旋转是指图像以某一点为中心旋转一定的角度，形成一幅新的图像的过程。图像旋转变换会有一个旋转中心，这个旋转中心一般为图像的中心，旋转之后图像的大小一般会发生改变。图6-8表示原始图像的坐标(x0, y0)旋转至(x1, y1)的过程。
![V5{4S F9GGK39DXFHMK3X56](https://user-images.githubusercontent.com/98206033/229684421-f543b883-c709-47c9-8b92-e6fed15efd25.png)
图像旋转变换主要调用getRotationMatrix2D()函数和warpAffine()函数实现，绕图像的中心旋转，函数原型如下：

M = cv2.getRotationMatrix2D(center, angle, scale)
– center表示旋转中心点，通常设置为(cols/2, rows/2)
– angle表示旋转角度，正值表示逆时针旋转，坐标原点被定为左上角
– scale表示比例因子  

rotated = cv2.warpAffine(src, M, (cols, rows))
– src表示原始图像
– M表示旋转参数，即getRotationMatrix2D()函数定义的结果
– (cols, rows)表示原始图像的宽度和高度  
图像效果如图所示，绕图像中心点逆时针旋转30度。
![C_%J}J ACO P0W3LBKQAK8Y](https://user-images.githubusercontent.com/98206033/229684537-ead6ca7a-867d-4592-96e5-fe7da693f9d0.png)


