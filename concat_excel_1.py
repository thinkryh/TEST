import pandas as pd

data = pd.read_excel(r'C:\Users\thinkryh\Desktop\2000-2014各省能源强度、能源结构(1).xls',sheet_name='2014')
data.drop(data.index[29:],inplace=True)
data.insert(0,'年份',2014)
print(data)

i = 2013
while i >= 1990:
    print (i)
    data1 = pd.read_excel(r'C:\Users\thinkryh\Desktop\2000-2014各省能源强度、能源结构(1).xls',sheet_name='%s' %i)
    data1.drop(data1.index[29:],inplace=True)
    data1.insert(0, '年份', i)
    data1.drop(data1.index[0], inplace=True)
    print(data1)
    # data2 = pd.concat([data,data1])
    data2 = data.append(data1,ignore_index=True,sort=False)
    i -= 1
    data = data2
final_data = data[['Unnamed: 0','年份','不平减能源强度(tons tce/10,002 yuan)']]
print(final_data.columns)
final_data = final_data.rename(index=str,columns={'Unnamed: 0':'地区'})
final_data.set_index('地区',inplace=True)
print(final_data.columns)
final_data.drop(['全国'],inplace=True)
final_data.to_excel(r'C:\Users\thinkryh\Desktop\111.xls')
