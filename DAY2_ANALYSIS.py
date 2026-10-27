Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/vamsi/OneDrive/Desktop/Project Folder/Python/day1_analysis.py
  Order_ID                 Date Customer_ID  ...     City Payment      Sales
0  ORD0119  2025-01-01 00:00:00        C083  ...  Chennai     UPI  108911.98
1  ORD0556  2025-01-01 00:00:00        C067  ...  Kolkata     UPI  117351.18
2  ORD0803  2025-01-01 00:00:00        C057  ...   Mumbai    Cash    4805.26
3  ORD0010  2025-01-02 00:00:00        C081  ...     Pune    Card    4646.27
4  ORD0303  2025-01-02 00:00:00        C087  ...  Kolkata     UPI    8186.38

[5 rows x 10 columns]
(1000, 10)
Success Manasa!

= RESTART: C:/Users/vamsi/OneDrive/Desktop/Project Folder/Python/day1_analysis.py
  Order_ID                 Date Customer_ID  ...     City Payment      Sales
0  ORD0119  2025-01-01 00:00:00        C083  ...  Chennai     UPI  108911.98
1  ORD0556  2025-01-01 00:00:00        C067  ...  Kolkata     UPI  117351.18
2  ORD0803  2025-01-01 00:00:00        C057  ...   Mumbai    Cash    4805.26
3  ORD0010  2025-01-02 00:00:00        C081  ...     Pune    Card    4646.27
4  ORD0303  2025-01-02 00:00:00        C087  ...  Kolkata     UPI    8186.38

[5 rows x 10 columns]
(1000, 10)
Success Manasa!
<class 'pandas.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 10 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   Order_ID     1000 non-null   str    
 1   Date         1000 non-null   str    
 2   Customer_ID  1000 non-null   str    
 3   Product      1000 non-null   str    
 4   Category     1000 non-null   str    
 5   Quantity     1000 non-null   int64  
 6   Price        1000 non-null   float64
 7   City         1000 non-null   str    
 8   Payment      1000 non-null   str    
 9   Sales        1000 non-null   float64
dtypes: float64(2), int64(1), str(7)
memory usage: 78.3 KB
None

= RESTART: C:/Users/vamsi/OneDrive/Desktop/Project Folder/Python/day1_analysis.py
  Order_ID                 Date Customer_ID  ...     City Payment      Sales
0  ORD0119  2025-01-01 00:00:00        C083  ...  Chennai     UPI  108911.98
1  ORD0556  2025-01-01 00:00:00        C067  ...  Kolkata     UPI  117351.18
2  ORD0803  2025-01-01 00:00:00        C057  ...   Mumbai    Cash    4805.26
3  ORD0010  2025-01-02 00:00:00        C081  ...     Pune    Card    4646.27
4  ORD0303  2025-01-02 00:00:00        C087  ...  Kolkata     UPI    8186.38

[5 rows x 10 columns]
(1000, 10)
Success Manasa!
<class 'pandas.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 10 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   Order_ID     1000 non-null   str    
 1   Date         1000 non-null   str    
 2   Customer_ID  1000 non-null   str    
 3   Product      1000 non-null   str    
 4   Category     1000 non-null   str    
 5   Quantity     1000 non-null   int64  
 6   Price        1000 non-null   float64
 7   City         1000 non-null   str    
 8   Payment      1000 non-null   str    
 9   Sales        1000 non-null   float64
dtypes: float64(2), int64(1), str(7)
memory usage: 78.3 KB
None
Order_ID       0
Date           0
Customer_ID    0
Product        0
Category       0
Quantity       0
Price          0
City           0
Payment        0
Sales          0
dtype: int64
          Quantity         Price          Sales
count  1000.000000   1000.000000    1000.000000
mean      2.353000   6836.676550   16522.054460
std       1.415767  12993.550185   38737.535043
min       1.000000    108.750000     108.750000
25%       1.000000   1121.382500    1664.627500
50%       2.000000   2256.900000    4385.385000
75%       3.000000   4667.865000   11412.662500
max       5.000000  60458.790000  300616.100000

print(df.duplicated().sum())
0
print(df.columns)
Index(['Order_ID', 'Date', 'Customer_ID', 'Product', 'Category', 'Quantity',
       'Price', 'City', 'Payment', 'Sales'],
      dtype='str')
print(df.dtypes)
Order_ID           str
Date               str
Customer_ID        str
Product            str
Category           str
Quantity         int64
Price          float64
City               str
Payment            str
Sales          float64
dtype: object

df['Date']=pd.to_datetime(df['Date'])
print(df.dtypes)
Order_ID                  str
Date           datetime64[us]
Customer_ID               str
Product                   str
Category                  str
Quantity                int64
Price                 float64
City                      str
Payment                   str
Sales                 float64
dtype: object

print(df['Quantity'].min())
1
print(df['Price'].min())
108.75
print(df['Sales'].min())
108.75
print(df['Category'].value_Counts())
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(df['Category'].value_Counts())
  File "C:\Users\vamsi\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'value_Counts'. Did you mean: 'value_counts'?
print(df['Category'].value_counts())
Category
Home & Kitchen    262
Electronics       252
Fashion           240
Stationery        134
Furniture         112
Name: count, dtype: int64
print(df['product'].nunique())
Traceback (most recent call last):
  File "C:\Users\vamsi\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'product'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(df['product'].nunique())
  File "C:\Users\vamsi\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\vamsi\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'product'
print(df['Product'].nunique())
16
print(df['City'].nunique())
8
print("Total Sales:", df['Sales'].sum())
Total Sales: 16522054.459999999
print("Total Quantity Sold:", df['Quantity'].sum())
Total Quantity Sold: 2353
print("Total Orders:", df['Order_ID'].nunique())
Total Orders: 1000
print("Average Order Value:", df['Sales'].sum() / df['Order_ID'].nunique())
Average Order Value: 16522.05446
print("Average Quantity per Order:", df['Quantity'].sum() / df['Order_ID'].nunique())
Average Quantity per Order: 2.353
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(category_sales)
SyntaxError: multiple statements found while compiling a single statement
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(category_sales_pct)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(category_sales_pct)
NameError: name 'category_sales_pct' is not defined. Did you mean: 'category_sales'?
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(category_sales)
Category
Electronics       12164626.02
Furniture          1864029.71
Home & Kitchen     1488329.29
Fashion             961953.21
Stationery           43116.23
Name: Sales, dtype: float64
category_sales_pct = (category_sales / df['Sales'].sum()) * 100
print(category_sales_pct)
Category
Electronics       73.626594
Furniture         11.282070
Home & Kitchen     9.008137
Fashion            5.822237
Stationery         0.260962
Name: Sales, dtype: float64
product_sales=df.groupby('Product')
product_sales=df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print(product_sales.head(5))
Product
Laptop           8088473.34
Smartphone       3254870.04
Office Chair      963403.01
Study Table       900626.70
Mixer Grinder     630355.85
Name: Sales, dtype: float64
City_sales=df.groupby('City')['Sales'].sum().sort_values(ascending=False)
print(city_sales)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(city_sales)
NameError: name 'city_sales' is not defined. Did you mean: 'City_sales'?
print(City_sales)
City
Chennai      2633779.17
Bangalore    2129909.84
Mumbai       2052861.21
Kolkata      1991885.53
Pune         1974104.02
Hyderabad    1937431.19
Ahmedabad    1914222.91
Delhi        1887860.59
Name: Sales, dtype: float64
Payment_sales=df.groupby('Payment')['Sales'].sum().sort_values(ascending=False)
print(Payment_sales)
Payment
Net Banking    4416551.51
Cash           4177941.84
Card           3968105.01
UPI            3959456.10
Name: Sales, dtype: float64
print(df['Payment'].value_counts())
Payment
Cash           266
Net Banking    248
UPI            244
Card           242
Name: count, dtype: int64
df['Month'] = df['Date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Sales'].sum()
SyntaxError: multiple statements found while compiling a single statement
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()
SyntaxError: multiple statements found while compiling a single statement
df['Month'] = df['Date'].dt.to_period('M')monthly_sales = df.groupby('Month')['Sales'].sum()
SyntaxError: invalid syntax


df['Month'] = df['Date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Sales'].sum()
SyntaxError: multiple statements found while compiling a single statement



df['Month'] = df['Date'].dt.to_period('M')



df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()
print(monthly_sales)
Month
2025-01    1335469.74
2025-02    1263737.66
2025-03    1198677.69
2025-04    1247966.99
2025-05    1866429.67
2025-06    1172620.08
2025-07    2012527.97
2025-08     962899.06
2025-09    1391750.40
2025-10    1424343.77
2025-11    1286905.90
2025-12    1358725.53
Freq: M, Name: Sales, dtype: float64
customer_sales = df.groupby('customer_Id')['Sales'].sum().sort_values(ascending=False)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    customer_sales = df.groupby('customer_Id')['Sales'].sum().sort_values(ascending=False)
  File "C:\Users\vamsi\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\util\_decorators.py", line 336, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\vamsi\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 10833, in groupby
    return DataFrameGroupBy(
  File "C:\Users\vamsi\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\groupby\groupby.py", line 1095, in __init__
    grouper, exclusions, obj = get_grouper(
  File "C:\Users\vamsi\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\groupby\grouper.py", line 901, in get_grouper
    raise KeyError(gpr)
KeyError: 'customer_Id'
>>> customer_sales = df.groupby('Customer_Id')['Sales'].sum().sort_values(ascending=False)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    customer_sales = df.groupby('Customer_Id')['Sales'].sum().sort_values(ascending=False)
  File "C:\Users\vamsi\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\util\_decorators.py", line 336, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\vamsi\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 10833, in groupby
    return DataFrameGroupBy(
  File "C:\Users\vamsi\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\groupby\groupby.py", line 1095, in __init__
    grouper, exclusions, obj = get_grouper(
  File "C:\Users\vamsi\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\groupby\grouper.py", line 901, in get_grouper
    raise KeyError(gpr)
KeyError: 'Customer_Id'
>>> customer_sales = df.groupby('Customer_ID')['Sales'].sum().sort_values(ascending=False)
>>> print(customer_sales.head(5))
Customer_ID
C043    550181.32
C026    513908.35
C029    370535.68
C117    344192.02
C041    340360.61
Name: Sales, dtype: float64
>>> df.to_csv("ecommerce_cleaned.csv",index=False)
>>> 
>>> print(df.shape)
(1000, 11)
>>> print(df.head())
  Order_ID       Date Customer_ID  ... Payment      Sales    Month
0  ORD0119 2025-01-01        C083  ...     UPI  108911.98  2025-01
1  ORD0556 2025-01-01        C067  ...     UPI  117351.18  2025-01
2  ORD0803 2025-01-01        C057  ...    Cash    4805.26  2025-01
3  ORD0010 2025-01-02        C081  ...    Card    4646.27  2025-01
4  ORD0303 2025-01-02        C087  ...     UPI    8186.38  2025-01

[5 rows x 11 columns]
