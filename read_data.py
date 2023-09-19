from torch.utils.data import Dataset
#import cv2
from PIL import Image
import os   #用于对路径进行操作

'''
dir_path = "数据集/hymenoptera_data/train/ants"
img_path_list = os.listdir(dir_path)    #把文件路径下的的所有照片文件名做成一个list
print(img_path_list[0])

mg_path = "数据集/hymenoptera_data/train/ants/0013035.jpg"
img = Image.open(img_path)
img.size
img.show()
'''

###以文件名的方式存储lable
class MyDta(Dataset):
    def __init__(self, root_dir, lable_dir):   #为整个class提供全局变量，为后续函数提供变量, root_dir为数据集文件夹路径，lable_dir为文件夹名称(作为lable0
        self.root_dir = root_dir   #吧root_dir做成全局变量(函数内)，让下面的函数可以用
        self.label_dir = lable_dir
        self.path = os.path.join(self.root_dir, self.label_dir)  #拼接地址和文件夹名
        self.img_path_list = os.listdir(self.path)    #把文件路径下的的所有照片文件名做成一个list

    def __getitem__(self, idx):   #idx作图片编号
        img_name = self.img_path_list[idx]        #把文件路径下的的所有照片文件名做成一个list
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)    #把照片名拼接成照片完整路径
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.img_path_list)


root_dir = "数据集/hymenoptera_data/train"
ant_lable_dir = "ants"
ants_dataset = MyDta(root_dir, ant_lable_dir)


bees_lable_dir = "bees"
bees_dataset = MyDta(root_dir, bees_lable_dir)

train_dataset = ants_dataset + bees_dataset
img, label = train_dataset[200]
img.show()








