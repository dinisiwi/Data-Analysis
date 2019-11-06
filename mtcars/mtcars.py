Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> #import library
... import pandas as pd
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> import numpy as np
>>>
>>> #import dataset mtcars
... data_mtcars=pd.read_excel(r'E:\\Internship\\mtcars.xlsx')
>>>
>>> #membuat variabel baru dengan klasifikasi yang sudah ditentukan
... data_mtcars.loc[(data_mtcars['mpg'] < 20 ),'mpg_level'] = 'low'
>>> data_mtcars.loc[(data_mtcars['mpg'] >= 20 )&(data_mtcars['mpg'] <= 30 ),'mpg_level'] = 'medium'
>>> data_mtcars.loc[(data_mtcars['mpg'] > 30 ),'mpg_level'] = 'hard'
>>>
>>> #menampilkan data
... data_mtcars.head()
                Cars   mpg  cyl   disp  ...  am  gear  carb  mpg_level
0          Mazda RX4  21.0    6  160.0  ...   1     4     4     medium
1      Mazda RX4 Wag  21.0    6  160.0  ...   1     4     4     medium
2         Datsun 710  22.8    4  108.0  ...   1     4     1     medium
3     Hornet 4 Drive  21.4    6  258.0  ...   0     3     1     medium
4  Hornet Sportabout  18.7    8  360.0  ...   0     3     2        low

[5 rows x 13 columns]
>>>
>>> #mendapatkan statistika deskriptif dari dataset mtcars
... data_mtcars.describe()
             mpg        cyl  ...       gear     carb
count  32.000000  32.000000  ...  32.000000  32.0000
mean   20.090625   6.187500  ...   3.687500   2.8125
std     6.026948   1.785922  ...   0.737804   1.6152
min    10.400000   4.000000  ...   3.000000   1.0000
25%    15.425000   4.000000  ...   3.000000   2.0000
50%    19.200000   6.000000  ...   4.000000   2.0000
75%    22.800000   8.000000  ...   4.000000   4.0000
max    33.900000   8.000000  ...   5.000000   8.0000

[8 rows x 11 columns]
>>>
>>> #plot mpg_level
... sns.countplot(x='mpg_level', data=data_mtcars)
<matplotlib.axes._subplots.AxesSubplot object at 0x08B7AE70>
>>> plt.show()
>>>
>>> #mencari nilai korelasi antar variabel dalam dataset mtcars
... correlation = data_mtcars.corr()
>>> plt.figure(figsize=(14, 8))
<Figure size 1400x800 with 0 Axes>
>>> sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")
<matplotlib.axes._subplots.AxesSubplot object at 0x08D95430>
>>> plt.show()
