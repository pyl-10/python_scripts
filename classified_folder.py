from genericpath import exists
from shutil import move
import os
import random

from PIL.Image import new

# path = "/Users/xing_zhi/Downloads/files"
# files = os.listdir(path)
# os.getcwd()  # 当前目录
# os.chdir(path)  # 切换目录
# # print(files)
# for f in files:
#     folder_name = "./" + f.split(".")[-1]
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)
#         move(f, folder_name)
#     else:
#         move(f, folder_name)

path = "/Users/xing_zhi/Downloads/网赚最新最全资料300多个"
files = os.listdir(path)
print(os.getcwd())
print(os.chdir(path))
print(os.getcwd())

for file in files:
    if os.path.isdir(file):
        newPath = path + "/" + file
        os.chdir(newPath)
        fileOnSecondFloor = os.listdir(newPath)
        for docFile in fileOnSecondFloor:
            if os.path.isdir(docFile):
                move(newPath + "/" + docFile, path)
            else:
                if (not docFile.endswith(".docx")) and (not docFile.endswith(".doc")) and (not docFile.endswith(".png")):
                    os.remove(docFile)
                else:
                    try:
                        move(newPath + "/" + docFile, path)
                    except Exception as e:
                        print(e)
                        if os.path.exists(docFile):
                            doclist = docFile.split(".")
                            newDocFile = doclist[0] + str(random.randint(1, 50)) + doclist[1]
                            os.rename(docFile, newDocFile)
                            move(newPath + "/" + newDocFile, path)
        os.chdir(path)
        os.removedirs(file)

# # 创建目标文件夹
# if not os.path.exists("image") and not os.path.exists("document"):
#     os.makedirs('image')
#     os.makedirs('document')
# # 将需要处理的后缀名存储到list中
# image_suffix = ['jpg', 'png', 'gif']
# doc_suffix = ['doc', 'docx', 'ppt', 'md']
# # 移动jpg、png、gif文件中的文件
# for i in image_suffix:
#     files = os.listdir(i)
#     for f in files:
#         # 移动文件夹中的文件
#         move(i + "/" + f, "image")
#     # 删除文件夹
#     os.removedirs(i)
# # 移动doc、docx、md、ppt文件夹中的文件，步骤与前面类似
# for d in doc_suffix:
#     files = os.listdir(d)
#     for f in files:
#         move(d + '/' + f, 'document')
#     os.removedirs(d)


