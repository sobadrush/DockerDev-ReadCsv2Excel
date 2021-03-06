#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import codecs
import pandas as pd
from pandas import DataFrame
import os
import xlsxwriter

import utils as myUtils

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
    recordsIdx = float('inf') # Records 所在的 index (預先設為python最大值)
    rowIdxSubstract = 0 # 因應skip列，異動 row index
    contentList = [line.strip() for line in csvFile.readlines()]
    for idx, line in enumerate(contentList):
        startColumn = ("A" + str(idx + 1 - rowIdxSubstract))
        line = line.replace("\t", "").replace(",", "，")
        lineArr = line.split(' ')
        myUtils.handleMemo(lineArr) # 替換說明中的空白為"，"
        tempLine = lineArr
        if len(tempLine) == 1 and tempLine[0] == '':
            rowIdxSubstract = rowIdxSubstract + 1
            continue
        if any('Record' == item for item in lineArr): # 跳過 Record 的列
            rowIdxSubstract = rowIdxSubstract + 1
            continue
        if any('TRANRQ' in item for item in lineArr):
            tempLine = ['1', 'TRANRQ', 'object', '0', 'N', '欄位名稱及說明']
            ws.write_row(startColumn, tempLine, wb.add_format({'bold': 1, "bg_color": "#2894FF"}))
            print(tempLine)
            continue
        if any('TRANRS' in item for item in lineArr):
            tempLine = ['1', 'TRANRS', 'object', '0', 'N', '欄位名稱及說明']
            ws.write_row(startColumn, tempLine, wb.add_format({'bold': 1, "bg_color": "#00DB00"}))
            print(tempLine)
            continue
        if any('Records' in item for item in lineArr):
            ws.write_row(startColumn, tempLine, wb.add_format({'bold': 1, "bg_color": "#9999CC"}))
            recordsLevel = int(lineArr[0])
            recordsIdx = idx
            print(tempLine)
            continue
        if idx > recordsIdx: # 讀到的列index超過Records的index
            if int(tempLine[0]) >= recordsLevel + 2: # 讀到的level ≥ Records 的 level+2
                tempLine[0] = str(int(tempLine[0]) - 1)
        print(tempLine)
        ws.write_row(startColumn, tempLine)
wb.close()

print("... Start Transfer xlsx to csv ...")
df = pd.read_excel(r'./result.xlsx')
# df = df.loc[:, ~df.columns.str.contains('Unnamed')]
df.to_csv(r'./result.csv', index=None, header=True, encoding='utf-8-sig')
print("... Finished Transfer xlsx to csv ...")
