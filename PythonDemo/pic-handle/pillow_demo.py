from PIL import Image, ImageDraw
import os.path
import glob
import sys
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

# python 函数
# 功 能：将一张 jpg文件转pgm格式文件
# 参 数：jpg_file : 欲转换的jpg文件名
# pgm_dir  : 存放 pgm 文件的目录
def jpg2pgm( jpg_file , pgm_dir ):
    # 首先打开jpg文件
    jpg = Image.open( jpg_file )
    # resize to 200 * 250 , 双线性插值
    jpg = jpg.resize( jpg.size , Image.BILINEAR )
    # 调用 python 函数 os.path.join , os.path.splitext , os.path.basename ，产生目标pgm文件名
    name =(str)(os.path.join( pgm_dir , os.path.splitext( os.path.basename(jpg_file) )[0] ))+".pgm"
    # 创建目标pgm 文件
    jpg.save( name )

# 将所有的jpg文件放在当前工作目录，或者 cd {存放jpg文件的目录}
# for jpg_file in glob.glob("./*.jpg"):
#     jpg2pgm( jpg_file , "./" )


im = Image.open("./man-face.pgm")

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128, width=4)
draw.arc((0, 0, 200, 200), 0, 200, fill=50)
del draw

# write to stdout
im.save("man-face-png.png", "png")
del im

im = Image.open('./man-face.jpg')
im.thumbnail([225, 150], Image.ANTIALIAS)
im.save('man-face-thumbnail.jpg', 'JPEG')


n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2*X)

plot (X, Y+1, color='blue', alpha=1.00)
plot(X, Y, color='red')
plot (X, Y-1, color='blue', alpha=1.00)
show()

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 10
x = np.linspace(-3,3,4*n)
y = np.linspace(-3,3,3*n)
X,Y = np.meshgrid(x,y)
imshow(f(X,Y)), show()

fig = figure()
ax = Axes3D(fig)
X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
show()