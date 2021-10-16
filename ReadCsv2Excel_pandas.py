#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import codecs
import pandas as pd
from pandas import DataFrame
import os

filePath = input("請輸入要讀取的電文txt檔：") or "./sample.txt" # 讀取的txt檔相對路徑
print("相對本路徑的txt檔名(不輸入預設為sample.txt): " + filePath)

if os.path.isfile(filePath) == False:
  print('檔案 {} 不存在！！！'.format(filePath))
  exit()

dataList = [] # 最後要寫進excel的資料

with codecs.open(filePath, "r", "utf-8") as csvFile:
    contentList = [line.strip() for line in csvFile.readlines()]
    for idx, line in enumerate(contentList):
        lineArr = line.split(' ')
        tempLine = lineArr
        if any('TRANRQ' in item for item in lineArr):
            tempLine = ['1', 'TRANRQ', '', '', '']
        if any('TRANRS' in item for item in lineArr):
            tempLine = ['1', 'TRANRS', '', '', '']
        dataList.append(tempLine)
    print("dataList = ", dataList)
    df = pd.DataFrame(dataList)

    df.to_excel(r'./result.xlsx', index=False, header=False)



