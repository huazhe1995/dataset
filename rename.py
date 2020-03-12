import os

path = '/home/huazhe/dataset'  # 文件夹路径
filelist = os.listdir(path)  # 文件夹下所有文件
count = 0
for file in filelist:
    olddir = os.path.join(path, file)
    if os.path.isdir(olddir):  # 是文件夹则跳过
        continue
    filename = os.path.splitext(file)[0]
    filetype = os.path.splitext(file)[1]
    newdir = os.path.join(path, str(count).zfill(7) + filetype)  # zfill()用0补全位数
    os.rename(olddir, newdir)
    count += 1
    print(newdir)
print('over!')
