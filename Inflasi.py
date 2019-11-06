#import library
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
    
#import data
data_inflasi=pd.read_excel(r'E:\\Internship\\inflasi.xlsx')
    
#memisahkan data yang ada dalam kolom 'month' menjadi 'bulan dan 'tahun'
data=data_inflasi["Month"].str.split(" ",n=1,expand=True)
data.columns=['Bulan','Tahun']
data_inflasi=data_inflasi.drop(['Month'],axis=1)
data['Tahun']=pd.to_datetime(data['Tahun'])
data['Tahun']=pd.Series(pd. DatetimeIndex(data['Tahun']).year)
    
#mengubah format bulan dari bahasa Indonesia ke bahasa Inggris agar dapat diubah dalam format tanggal
data.loc[(data['Bulan'] == 'Januari' ),'Bulan'] = 'January'
data.loc[(data['Bulan'] == 'Februari' ),'Bulan'] = 'February'
data.loc[(data['Bulan'] == 'Maret' ),'Bulan'] = 'March'
data.loc[(data['Bulan'] == 'April' ),'Bulan'] = 'April'
data.loc[(data['Bulan'] == 'Mei' ),'Bulan'] = 'May'
data.loc[(data['Bulan'] == 'Juni' ),'Bulan'] = 'June'
data.loc[(data['Bulan'] == 'Juli' ),'Bulan'] = 'July'
data.loc[(data['Bulan'] == 'Agustus' ),'Bulan'] = 'August'
data.loc[(data['Bulan'] == 'September' ),'Bulan'] = 'September'
data.loc[(data['Bulan'] == 'Oktober' ),'Bulan'] = 'October'
data.loc[(data['Bulan'] == 'Nopember' ),'Bulan'] = 'November'
data.loc[(data['Bulan'] == 'Desember' ),'Bulan'] = 'December'
    
#mengkombinasikan data bulan dan tahun
tanggal = data['Bulan']+" "+data['Tahun'].map(str)
    
#menggabungkan dataframe
dataset_inflasi = pd.DataFrame(tanggal).join(data_inflasi['Inflasi'])
dataset_inflasi.columns = ['Tanggal','Inflasi']
dataset_inflasi['Tanggal']=pd.to_datetime(dataset_inflasi['Tanggal'])
    
#menampilkan beberapa dataset
dataset_inflasi.head()
print(dataset_inflasi.head())
     Tanggal  Inflasi
0 2019-06-01   0.0328
1 2019-05-01   0.0332
2 2019-06-01   0.0283
3 2019-03-01   0.0248
4 2019-02-01   0.0257
    
#mengurutkan data
dataset_inflasi = dataset_inflasi.sort_values(by='Tanggal', ascending=True).reset_index( drop=True)
    
#memperoleh deskriptif statistik
dataset_inflasi.describe()
print(dataset_inflasi.describe())
          Inflasi
count  199.000000
mean     0.063147
std      0.033162
min      0.000000
25%      0.038550
50%      0.060400
75%      0.072850
max      0.183800
print (np.var(dataset_inflasi))
Inflasi    0.001094
dtype: float64
    
#plot data inflasi dalam bentuk boxplot
plt.figure(figsize=(4,7))
sns.boxplot( x= 'Inflasi',  data=dataset_inflasi, orient='v');
plt.show()
print(plt.show())
![Boxplot](https://user-images.githubusercontent.com/57424014/68320038-d9d5b080-00f1-11ea-9596-261f655c5583.png)

#plot data inflasi dalam bentuk grafik
register_matplotlib_converters()
plt.figure(figsize=(10,6))
plt.plot(dataset_inflasi['Tanggal'],dataset_inflasi['Inflasi'])
plt.title('Inflasi')
plt.ylabel('Inflasi')
plt.xlabel('Tahun')
plt.show()
print(plt.show())    
![Grafik](https://user-images.githubusercontent.com/57424014/68320185-130e2080-00f2-11ea-96b7-259938dcaffe.png)
