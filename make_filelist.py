import os
from tqdm import tqdm

file_list = os.listdir("./dataset/train/celeba_train")

with open("./dataset/celeba_train.txt", "w") as f:
    for data in file_list:
        print(data)
        f.write("/dataset/train/celeba_train" + data + "\n")
