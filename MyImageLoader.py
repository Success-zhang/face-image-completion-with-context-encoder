import torch.utils.data as data
from PIL import Image
import os
import os.path
import torch
import torchvision.transforms as transforms
import torchvision.datasets as dset


def default_loader(path):
    return Image.open(path).convert('RGB')


class MyDataset(torch.utils.data.Dataset):
    def __init__(self, txt, transform=None, target_transform=None, loader=default_loader):
        fh = open(txt, 'r')
        imgs = []
        for line in fh:
            line = line.strip('\n')
            line = line.rstrip()
            words = line.split()
            imgs.append(words[0])
        self.imgs = imgs
        self.transform = transform
        self.target_transform = target_transform
        self.loader = loader

    def __getitem__(self, index):
        fn = self.imgs[index]
        # print(fn)
        img = self.loader(fn)
        if self.transform is not None:
            img = self.transform(img)
        return img

    def __len__(self):
        return len(self.imgs)


train_data = MyDataset(txt='dataset/celeba_test.txt', transform=transforms.ToTensor())
data_loader = torch.utils.data.DataLoader(train_data, batch_size=1, shuffle=True)
print(len(data_loader))
for i, data in enumerate(data_loader, 0):
    print(i)
    print(data)



