#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import codecs
import pandas as pd
from pandas import DataFrame
import os
import xlsxwriter

filePath = input("請輸入要讀取的電文txt檔：") or "./sample.txt" # 讀取的txt檔相對路徑
print("相對本路徑的txt檔名(不輸入預設為sample.txt): " + filePath)

if os.path.isfile(filePath) == False:
  print('檔案 {} 不存在！！！'.format(filePath))
  exit()

dataList = [] # 最後要寫進excel的資料
 
wb = xlsxwriter.Workbook('./result.xlsx')
ws = wb.add_worksheet("電文格式") # sheet

with codecs.open(filePath, "r", "utf-8") as csvFile:
    contentList = [line.strip() for line in csvFile.readlines()]
    for idx, line in enumerate(contentList):
        startColumn = ("A" + str(idx + 1))
        lineArr = line.split(' ')
        tempLine = lineArr
        if any('TRANRQ' in item for item in lineArr):
            tempLine = ['1', 'TRANRQ', '', '', '']
            ws.write_row(startColumn, tempLine, wb.add_format({'bold': 1, "bg_color": "#2894FF"}))
            continue
        if any('TRANRS' in item for item in lineArr):
            tempLine = ['1', 'TRANRS', '', '', '']
            ws.write_row(startColumn, tempLine, wb.add_format({'bold': 1, "bg_color": "#00DB00"}))
            continue
        print(tempLine)
        ws.write_row(startColumn, tempLine)
wb.close()