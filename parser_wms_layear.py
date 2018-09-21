#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import requests

x_min=5220000
y_min=5200000


list=[]
with open("C:/Users/azama//TILES/mygeoserver/newMahackala.txt", "r") as datafile:
    for line in datafile:
        featureline=line.replace('\t', ' ')
        featureline=featureline.replace('\n', '')
        # print(type(featureline))
        feature_list = [int(featureline.split(" ")[0]), int(featureline.split(" ")[1]), int(featureline.split(" ")[0])+10000, int(featureline.split(" ")[1])+10000]
        list.append(feature_list)
count=0

for coord in list:
    count += 1
    x_min=coord[0]
    y_min=coord[1]
    x_max=coord[2]
    y_max=coord[3]
    png_name ='my_server' + str(count)+".png"
    pngw_name= 'my_server' + str(count) + ".pngw"
    link = 'https://localhost/geoserver/=' + str(
        x_min) + '%2C' + str(y_min) + '%2C' + str(x_max) + '%2C' + str(
        y_max) + 'transparent=true&f=image'

    # urllib.urlretrieve(link, png_name)
    # Берем ссылку
    r = requests.get(link)
    # Выполнять функцию столько раз пока статус ответа не будет 200
    while r.status_code !=200:
        link = 'https://localhost/geoserver/=' + str(
            x_min) + '%2C' + str(y_min) + '%2C' + str(x_max) + '%2C' + str(
            y_max) + 'transparent=true&f=image'

        r = requests.get(link)
        print r.status_code


    # Записываем файл
    with open("C:/book/zho/"+ png_name, "wb") as code:
        code.write(r.content)
    f = open('C:/book/zho/'+pngw_name, 'w')
    a = "Gd"
    f.write("5" + '\n')
    f.write("0" + '\n')
    f.write("0" + '\n')
    f.write("-5" + '\n')
    f.write(str(x_min) + '\n')
    f.write(str(y_max))
    f.close()



