import json
import os
import shutil


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        # print("---  new folder...  ---")
    # print("---  OK  ---")
    # else:
    # print("---  There is this folder!  ---")


source_dir = './images/'
img = os.listdir(source_dir)  # 得到文件夹下所有文件名称

with open("AgriculturalDisease_train_annotations.json", 'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)

for pop_dict in load_dict:
    path = "./class/" + str(pop_dict['disease_class'])
    mkdir("./class/" + str(pop_dict['disease_class']))  # 根据类别创建文件夹
    # print(path)
    for fileNum in img:
        if not os.path.isdir(fileNum):  # 判断是否是文件夹,不是文件夹才打开
            if fileNum == pop_dict['image_id']:
                print(fileNum)  # 打印出文件名
                imgname = os.path.join(source_dir, fileNum)
                shutil.copy(source_dir + fileNum, path)  # 复制蹄片到class文件夹