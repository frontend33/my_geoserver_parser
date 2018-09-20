#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import requests

x_min=5220000
y_min=5200000

list_coordinat=[[5220000,5200000],[5230000,5210000]]
count=0
for coord in list_coordinat:
    count += 1
    print count
    x_min=coord[0]
    y_min=coord[1]
    x_max=x_min
    y_max=y_min
    png_name ='my_server' + str(count)+".png"
    pngw_name= 'my_server_' + str(count) + ".pngw"
    x_max=x_max+20000
    y_max=y_max+20000
    link = 'https://localhost/geoserver/=' + str(
        x_min) + '%2C' + str(y_min) + '%2C' + str(x_max) + '%2C' + str(
        y_max) + 'transparent=true&f=image'
    print link
    urllib.urlretrieve(link, png_name)
    # Берем ссылку
    r = requests.get(link)
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



