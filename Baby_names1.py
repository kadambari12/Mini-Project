"""
Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made 
    available data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that 
    particular data. 
    
    Concatinate all the data to form single dataframe 
    using pandas concat method.
    
    Display the top 5 male and female baby names of 2010.
    
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas groupby method).
    
    Plot the results of the above activity to show total births 
    by sex and year.
 """
 
 import pandas as pd
 import re
 from glob import glob

 filename = glob('baby_names/*.txt')
 main_list = []
 for file in filenames:
     temp_df = pd.read_csv(file, names =['names','sex','count'])
     # to extract year from file
     year = int(re.findall('\d\d\d\d',file)[0])
     
     if year > 2010:
         break
     
     temp_df['year'] = year
     main_list.append(temp_df)
len(main_list)
# 131
# original dataset file contain 138 years (from year 1880 to year 2017)  
# from year 1880 to year 2010 contain 131 years

# 2. Concatinate all the data to form single dataframe using pandas concat method.
final = pd.concat(main_list, axis = 0, ignore_index = True)
final.shape #(1691987, 4)
final.columns # ['names', 'sex', 'count', 'year']
final.head()
final['year'].value_counts()
final.isnull().sum() # NO NULL VALUES

# 3. Display the top 5 male and female baby names of 2010.
df_2010 = final[final['year'] == 2010]
female_names = df_2010[df_2010['sex'] == 'F']
female_names_sort_by_count = female_names.sort_values('count', ascending = False, ignore_index = True)
female_names_sort_by_count.head() 
# another way
female_names_sort_by_count['names'][0:5]

# 3.Display the top 5 male baby names of 2010.
df_2010 = final[final['year'] == 2010]
male_names = final[final['sex'] == 'M']
male_names_sort_by_count = male_names.sort_values('count', ascending = False, ignore_index = True)
male_names_sort_by_count.head()
# Another way
male_names_sort_by_count['names'][0:5]

# 4. Calculate sum of the births column by sex as the total number of births 
    # in that year(use pandas groupby method).
    
group_by = final.groupby(['year','sex']).agg({'count':['sum']})
print(group_by)

# 5.  Plot the results of the above activity to show total births by sex and year.
group_by.plot(kind='bar')
group_by[0:10].plot(kind ="bar")





# You can also use below code for better visualization
# Getting the year list

import numpy as np
import matplotlib.pyplot as plt

x_val = []
for i in group_by.index:
    if i[0] not in x_val:
        x_val.append(i[0])
#Getting the count
yval = list(group_by['count']['sum'])


#Female count are on even place
y_val_f = [yval[i]  for i in range(0,len(yval)) if i%2==0]
#Male count are on odd place

y_val_m = [yval[i]  for i in range(0,len(yval)) if i%2!=0]


  
X_axis = np.arange(len(x_val[0:10]))
  
plt.bar(X_axis - 0.2, y_val_f[0:10], 0.4, label = 'Female')
plt.bar(X_axis + 0.2, y_val_m[0:10], 0.4, label = 'Male')
  
plt.xticks(X_axis, x_val[0:10])
plt.xlabel("Year, Sex")
plt.ylabel("Count")
plt.legend()
plt.show()
