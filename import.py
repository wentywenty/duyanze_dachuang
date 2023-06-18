import cv2
import os

def crop_images(input_folder, x, y, width, height):
    #遍历输入文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            #获取图像文件路径
            img_path = os.path.join(root, file)
            
            #读取图像
            img = cv2.imread(img_path)
            
            #裁剪图像
            cropped_img = img[y:y+height, x:x+width]
            
            #删除原始图像
            os.remove(img_path)
            
            #保存裁剪后的图像并重命名为原始图像的文件名
            cv2.imwrite(img_path, cropped_img)
#设置输入文件夹路径
input_folder = '/home/flora/Documents/a'

#设置裁剪区域的起始坐标和宽高
x = 0
y = 0
width = 487
height = 483

#调用函数进行批量裁剪图片
crop_images(input_folder, x, y, width, height)