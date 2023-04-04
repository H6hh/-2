# -2
图像几何变换 （图像图像平移、镜像、旋转及其复合） 
图像平移：图像平移是将图像中的所有像素点按照给定的平移量进行水平或垂直方向上的移动。假设原始像素的位置坐标为（x0，y0），经过平移量（△x，△y）后，坐标变为（x1, y1） ![~RA }E~F9NL0JEP3F`O4YR6](https://user-images.githubusercontent.com/98206033/229677578-865aac4c-d776-490c-8c0d-cb15cba5adf8.png)

如图所示，下图图像平移，它定义了图像平移矩阵M，然后调用warpAffine()函数将原始图像垂直向下平移了100个像素，水平向右平移了200个像素。  
![U2S{Z__T4J`}1 %{$4FJF L](https://user-images.githubusercontent.com/98206033/229677417-30f84581-2921-4f29-a28c-55220cd30f48.png)  

