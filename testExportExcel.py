import pandas as pd

# data = {
#     'Product': ['Desktop Computer', 'Printer', 'Tablet', 'Monitor'],
#     'Price': [1200, 150, 300, 450]
# }

data = [['1', 'TRANRQ', 'object', '0', 'N'], ['2', 'IdNo', 'string', '12', 'Y', '身分證字號'], ['1', 'TRANRS', 'object', '0', 'N'], ['2', 'BankId', 'BankId', 'object', '0', 'N', '行庫代號'], ['2', 'BankAcnt', 'object', '0', 'N', '自扣帳號'], ['2', 'AcntId', 'object', '0', 'N', '自扣帳號ＩＤ']]

df = pd.DataFrame(data)

df.to_excel(r'./test.xlsx', index=False, header=False)



