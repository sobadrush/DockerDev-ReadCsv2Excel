#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import codecs
import pandas as pd
from pandas import DataFrame
import os
import xlsxwriter

filePath = input("請輸入要讀取的電文txt檔(不輸入預設為 sample.txt )：") or "./sample.txt" # 讀取的txt檔相對路徑
print("相對本路徑的txt檔名: " + filePath)

if os.path.isfile(filePath) == False:
  print('檔案 {} 不存在！！！'.format(filePath))
  input("按任意鍵離開")
  exit()

dataList = [] # 最後要寫進excel的資料
 
wb = xlsxwriter.Workbook('./result.xlsx')
ws = wb.add_worksheet("電文格式") # sheet

with codecs.open(filePath, "r", "utf-8") as csvFile:
    recordsLevel = 0 # Records 所在的 level
    recordsIdx = float('inf') # Records 所在的 index
    rowIdxSubstract = 0 # 因應skip列，異動 row index
    contentList = [line.strip() for line in csvFile.readlines()]
    for idx, line in enumerate(contentList):
        startColumn = ("A" + str(idx + 1 - rowIdxSubstract))
        line = line.replace("\t", "").replace(",", "，")
        lineArr = line.split(' ')
        tempLine = lineArr
        if len(tempLine) == 1 and tempLine[0] == '':
            rowIdxSubstract = rowIdxSubstract + 1
            continue
        if any('Record' == item for item in lineArr): # 跳過 Record 的列
            rowIdxSubstract = rowIdxSubstract + 1
            continue
        if any('TRANRQ' in item for item in lineArr):
            tempLine = ['1', 'TRANRQ', 'object', '', '']
            ws.write_row(startColumn, tempLine, wb.add_format({'bold': 1, "bg_color": "#2894FF"}))
            print(tempLine)
            continue
        if any('TRANRS' in item for item in lineArr):
            tempLine = ['1', 'TRANRS', 'object', '', '']
            ws.write_row(startColumn, tempLine, wb.add_format({'bold': 1, "bg_color": "#00DB00"}))
            print(tempLine)
            continue
        if any('Records' in item for item in lineArr):
            recordsLevel = int(lineArr[0])
            recordsIdx = idx
        if idx > recordsIdx:
            if int(tempLine[0]) >= recordsLevel + 2:
                tempLine[0] = str(int(tempLine[0]) - 1)
        print(tempLine)
        ws.write_row(startColumn, tempLine)
wb.close()