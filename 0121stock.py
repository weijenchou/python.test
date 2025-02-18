import pandas as pd
import numpy as np

df_0113= pd.read_csv('20250113上市股盤後 - 工作表1.csv')
df_0114= pd.read_csv('20250114上市股盤後 _20250114.csv')

#print(df_0113.head(10))
#print(df_0114.tail(13))

#df_0113['證券代號']= df_0113[df_0113['證券代號'].str.len()==4]
print(df_0113[df_0113['證券代號'].str[-1].str.isdigit()])
#print(df_0113)

"""
匿名函數 lambda
例如: lambda x:x*2
x是函數變數
冒號後面 *2 就是return的值
"""

fun1= lambda x : x*2
print(fun1(2))
fun2= lambda x,y: x*2 + y*2
print(fun2(2,3))
fun3= lambda x: len(x) == 4

#apply 搭配 lambda篩選資料
df_0113= df_0113[df_0113['證券代號'].apply(lambda x: x[-1].isdigit())]
df_0114= df_0114[df_0114['證券代號'].apply(lambda x: x[-1].isdigit())]
#print(df_0114.tail(50))

#用 .insert 新增欄位到特定位置(index)
#第一個參數:index, 第二個參數:欄位名稱，第三個參數：資料內容
df_0113.insert(0,'交易日期','2025.01.13')
df_0114.insert(0,'交易日期','2025.01.14')

df_1314= pd.concat([df_0113,df_0114],ignore_index= True)
print(df_1314)
#print(df_0113.head(),df_0114.head())

# "1,400".replace(',','')-> "1400"
df_1314[['收盤價','開盤價','最高價','最低價','成交股數']]= df_1314[
    ['收盤價','開盤價','最高價','最低價','成交股數']].apply(lambda x:x.replace(',','',regex= True))

df_1314[['收盤價','開盤價','最高價','最低價','成交股數']]= df_1314[
    ['收盤價','開盤價','最高價','最低價','成交股數']].replace('--',np.nan).astype(float)

df_1314 = df_1314.sort_values(by=['證券代號','交易日期'])
#print(df_1314.isnull().any(axis=1))
df_1314 = df_1314.ffill()
#print(df_1314[df_1314.isnull().any(axis=1)]) #檢查空值

df_1314['收盤開盤價差']= df_1314['收盤價']- df_1314['開盤價']
df_1314['最高最低價差']= df_1314['最高價']- df_1314['最低價']
df_1314['當日漲跌幅']=( df_1314['收盤價']- df_1314['開盤價']) / df_1314['開盤價']
df_1314= df_1314.reset_index(drop=True)
df_1314.to_csv('1314_test.csv')
#print(df_1314[df_1314['成交股數'].apply(lambda x: x.isdigit())])

group_code= df_1314.groupby('證券代號')

#正常迴圈寫法
#code_dict= {}
#for code, data in group_code:
   # code_dict[code]= data.reset_index(drop= True)

#迴圈一行寫法
code_dict= {code: data.reset_index(drop= True) for code, data in group_code}
#code_dict['2330']['成交量變化]']= code_dict['2330']['成交股數'] -code_dict['2330']['成交股數'].shift(1)

#for code, df_data in code_dict:
#    trading_volume= df_data['成交股數'] - df_data['成交股數'].shift(1)

#items() [1:2, 3:4] => [(1,2),(3,4)]
df_collect=[]
for code, df_data in code_dict.items():
    df_data['成交量變化']= (df_data['成交股數'] -df_data['成交股數'].shift(1))
    df_data['成交量變化幅度']= df_data['成交量變化']/df_data['成交股數'].shift(1)
    df_data.dropna(inplace= True)
    if not df_data[df_data['成交量變化幅度']>3].empty:
        #print(df_data)
        df_collect.append(df_data)
    #break

df_volume= pd.concat(df_collect).reset_index(drop=True)
df_volume.to_csv('volume_1314_test.csv')
print(df_volume)

#做純數值的特徵表格，篩選數值資料欄位
#feature_df = df_1314.iloc[:,3:]
feature_df = df_1314.loc[:, '成交股數']
feature_df.to_csv('1314_feature.csv')