代码地址：https://github.com/Success-zhang/face-image-completion-with-context-encoder.git

代码运行说明
环境：Ubantu 16.04, python 3.5以上
1.将数据集放入dataset文件夹下
运行python make_filelist.py

2.训练
python train.py --cuda --niter 200

3.测试
python test.py --nteG model/Your_netGmodel.pth --dataroot dataset/test --batchSize 100
