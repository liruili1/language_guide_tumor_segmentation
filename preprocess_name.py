##This is the file for preprocess

import os
import pandas as pd
import numpy as np

file_path = r'E:\isic216_language_guide\ISBI2016_ISIC_Part3B_Training_GroundTruth.csv'
path = r'E:\isic216_language_guide\ISBI2016_ISIC_Part1_Training_GroundTruth_1'
filelist = os.listdir(path)
count = 1
for file in filelist:
    print(file)
for file in filelist:
    Olddir = os.path.join(path, file)
    file_name = file
    file_name = os.path.join(file_name.replace('.png',''))
    if os.path.isdir(Olddir):
        continue

    df = pd.read_csv(file_path, header=None)

    data = np.array(df)
    print(data)
    for item in data:
        sh = item[0]
        if file_name == sh:
            index = item[1]
            break

    filename = os.path.splitext(file)[0]
    filetype = '.png'
    #Newdir = os.path.join(path, filename.replace('_Segmentation','') + filetype)
    Newdir = os.path.join(path,filename+"_"+str(index)+filetype)
    os.rename(Olddir, Newdir)

    count += 1
