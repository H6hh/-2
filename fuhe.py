from PIL import Image
import math

# 打开图像
img = Image.open("njust.png")

# 定义平移距离和镜像轴
tx, ty = 20, 30
axis = "x"

# 定义旋转角度
theta = 20

# 构造变换矩阵
translation_matrix = (1, 0, tx, 0, 1, ty)
if axis == "x":
    mirror_matrix = (-1, 0, img.width, 0, 1, 0)
else:
    mirror_matrix = (1, 0, 0, 0, -1, img.height)
rotation_matrix = (
    math.cos(math.radians(theta)),
    -math.sin(math.radians(theta)),
    0,
    math.sin(math.radians(theta)),
    math.cos(math.radians(theta)),
    0,
)

# 应用变换矩阵
img = img.transform(
    img.size, Image.AFFINE, translation_matrix, resample=Image.BICUBIC
)
img = img.transform(
    img.size, Image.AFFINE, mirror_matrix, resample=Image.BICUBIC
)
img = img.transform(
    img.size, Image.AFFINE, rotation_matrix, resample=Image.BICUBIC
)

# 保存结果图像
img.save("transformed_image.jpg")

