
|  參考   | 連結  |
|  ----  | ----  |
|Python PIP 使用 requirements.txt 管理套件相依性|https://blog.longwin.com.tw/2019/03/python-pip-requirements-txt-management-package-2019/|
|【Python】使用 PyInstaller 將 Python打包成 exe 檔|https://medium.com/pyladies-taiwan/python-%E5%B0%87python%E6%89%93%E5%8C%85%E6%88%90exe%E6%AA%94-32a4bacbe351|
|轉換xlsx為csv|https://datatofish.com/excel-to-csv-python/|

## 注意：不可用 Python3.10版(有lib pip安裝不到)

0. 可使用docker虛擬python環境 open this folder
1. 安裝套件: pip install -r ./requirements.txt
2. 輸出exe:  pyinstaller.exe -F .\ReadCsv2Excel_xlsxwriter.py 
3. 要讀取的原始檔: sample.txt
