
"""
Pandas 是一個數據分析工具，提供高效能，易於操作的數據結構
適用於資料處理與分析，表格處理模組
"""
import pandas as pd
#主要物件
#pd 的 series

s=pd.Series([10,20,30])
print(s)

s=pd.Series([10,20,30], index=['a','b','c'])
print(s)

#取得Series數據
print(s.values, type(s.values))
print(s['c'])

#用字典創建 Series
dict1= {
    'a':1,
    'b':2,
    'c':3
}
s2= pd.Series(dict1)
print(s2)
print(s+s2)

#DataFrame: 二維數據結構，類似於Excel表格

#方法1.使用字典轉換表格(df)
data= {
    'Name':['Alice',"Bob"],
    'Age':[26,30]
}
df= pd.DataFrame(data)
print(df)

#方法2.先設定欄位名稱再塞入資料(資料用list)
columns_name=['Name','Age']
data_list = [
    ['Alice',25],
    ['Bob',30],
    ['Charlie',38]
]
df2= pd.DataFrame(data_list, columns=columns_name)
print(df2)

#創建新蘭位新資料
df['id']=[1,2]
print(df)

#轉換型態
#df['Age'] = df['Age'].astype(str)
#print(type(df['Age'][0])) #str

#使用索引搜尋表格範圍(.loc, iloc)

print(df.loc[0,'Name']) #使用標籤索引
print(df.iloc[1,0]) #使用整數索引
print(df.loc[0])
print(df.iloc[0])

#切片索引搜尋
print(df.loc[:,'Name'])
print(df.loc[0,:])
print(df.loc[:,'Age':'id'])

import numpy as np

df['Age']= np.log(df['Age']) #底數預設
#庫存新數值，要再賦值給原表格，類似修改後存檔
print(df)

data_nan= {
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[25,np.nan, 40,38],
    'City':['New York','Los Angeles', np.nan, 'Chicago'],
    'Salary':[30000,8000,10000,np.nan]
}

#創建 Dataframe
df_nan= pd.DataFrame(data_nan)
#print(df_nan)
#df_nan= df_nan.dropna() #預設刪除有空值的列資料
#df_nan= df_nan.dropna(axis='columns') 
#df_nan= df_nan.dropna(axis='columns',how='all') #刪除所有資料都是空值的資料
#df_nan= df_nan.dropna(thresh=2).reset_index(drop=True)
#列資料空值超過2個才會刪除該列，並重置index順序

#df_nan.dropna(inplace=True)
#inplace=True 從根本修改原資料表，不用回傳
print(df_nan)


### 判定缺失值

#print(df_nan.isnull())
#print(df_nan.notnull())
#print(df_nan.notnull().astype(int)) #布林值轉換1 or 0

###填補缺失數據

#寫法1
#df_nan = df_nan.fillna(0) #用0補空值

#寫法2
#df_nan.fillna(0, inplace= True)
#print(df_nan)

#填補缺失數據的其他方法
#使用平均值填補
#df_nan['Age']= df_nan['Age'].fillna(df_nan['Age'].mean())

#使用眾數填補
#print(df_nan['City].mode()[0])
#df_nan['City']= df_nan['City'].fillna(df_nan['City'].mode()[0])

#使用中位數填補
#df_nan['Salary']= df_nan['Salary'].fillna(df_nan['Salary'].median())

#使用前一項數據補值
df_nan= df_nan.ffill()

#使用後一項數據補值
df_nan= df_nan.bfill()

print(df_nan)

#設定不同欄位不同填充值
df_nan.fillna(
    {
        'Age':df_nan['Age'].mean(),
        'City':df_nan['City'].mode()[0],
        'Salary':df_nan['Salary'].median(),
    }
    )
print()
print(df_nan)

#表格合併

#相同欄位沿著 axis=0 方向合併 並忽略原有index
#df_1=pd.DataFrame({'A':[1,2]})
#df_2=pd.DataFrame({'A':[3,4]})
#df_12=pd.concat([df_1, df_2],ignore_index=True)
#print(df_12)

#不同欄位沿著 axis=1 方向合併
#df_3=pd.DataFrame({'B':[3,4]})
#df_13=pd.concat([df_1, df_3],axis=1)
#print(df_13)


data={
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[19,35, 26,38],
    'City':['New York','Los Angeles', 'Texas', 'Chicago'],
    'Salary':[30000,8000,10000,5000]
}

df= pd.DataFrame(data)
groupby_name= df.groupby('Name')
#print(groupby_name)
#print(list(groupby_name))
group_dict={}
for name, data in groupby_name:
    group_dict[name]= data
print(group_dict)

#高效數據查詢與計算
# &:and, |:or
age_20_to_30 = df[(df['Age']>=20)&(df['Age']<=30)]
#print(df[(df['Age']>=20) &(df['Age']<=30)])
#print(df[df['Name'].str.len()== 5]) #名字字串長度為5的資料

#使用 .query('')在字串裡寫python條件判斷
print(df.query('20<=Age<=30'))
print(df.query('Name == "Alice"'))

#用原有的資料創建新資料欄位
df['New_Age']= df['Age'] +5
df['New_Salary']=np.sqrt(df['Salary']) *200
print(df)