#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s1 = 'ABCDCDC'
s2 = 'CDC'

s1.count('CD')


# In[ ]:


#datetime.date(year, month, day)
#datetime.time(hour=0, minute=0, second=0, microsecond=0)
#datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0


from datetime import time
  
Time = time(11, 34, 56)
  
print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)


# In[ ]:





import datetime

x = datetime.datetime(2018, 6, 1,12,30,30)
print(x)
print(x.strftime("%A"))


# In[ ]:


get_ipython().run_line_magic('a', 'Weekday, short version\tWed')
get_ipython().run_line_magic('A', 'Weekday, full version\tWednesday')
get_ipython().run_line_magic('w', 'Weekday as a number 0-6, 0 is Sunday\t3')
get_ipython().run_line_magic('d', 'Day of month 01-31\t31')
get_ipython().run_line_magic('b', 'Month name, short version\tDec')
get_ipython().run_line_magic('B', 'Month name, full version\tDecember')
get_ipython().run_line_magic('m', 'Month as a number 01-12\t12')
get_ipython().run_line_magic('y', 'Year, short version, without century\t18')
get_ipython().run_line_magic('Y', 'Year, full version\t2018')


# In[ ]:


#strftime(datestamp, format)
#strptime(date_string, format)


import datetime 
from datetime import datetime
now = datetime.now()
print(now)
now.strftime("%Y-%m-%d %H:%M:%S")
now.strftime("%Y-%b-%d %H:%M:%S")
now.strftime("%Y/%b/%A %H:%M:%S")


# In[ ]:


#strptime to parse strings
#strftime to parse format

x = "23/2020/September 8:28"


import datetime
datetime.datetime.strptime(x,"%d/%Y/%B %H:%M")


# In[ ]:


try:
    #CRITICAL---probability of error occurring is high
    x = float(input("Your number: "))
    inverse = 1.0 / x
    
except ValueError:
    #Normal STATEMENT PROB is LESS
    print("You should have given either an int or a float")
    
except ZeroDivisionError:
    print("Infinity")
    

finally:
    print("There may or may not have been an exception.")


# In[ ]:


#anonymous gen functions gen expression (wo yield and def)
A = (x**2 for x in [10,20,30])


# In[ ]:


next(A)


# In[ ]:


#two methods to read csv:- 1. open and csv reader 2. 
#Pandas and read_csv
#pandas deals with dataframes (a table structure)


import pandas as pd
df = pd.read_csv('C:\Yogesh_WFM\EDYODA\medals.csv')
print(df.head(2))


import csv
with open('C:\Yogesh_WFM\EDYODA\medals.csv',"r") as f:
    file  = csv.reader(f) 
    for row in file:
        print(row)
        



# In[ ]:


# xml parsing with ElementTree (find, findall)
# BeautifulSoup was for html parsing (find, find_all)
#Company > EMPLOYEE > Details


import xml.etree.ElementTree as ET
tree = ET.parse('C:\Yogesh_WFM\EDYODA\TEST3.xml')
base  = tree.getroot()



for e in base.findall('employee'):
    print(e.find('name').text)
    print(e.find('phone').text)
    print(e.find('email').text)
    print(e.find('date').text)



# In[ ]:



base.find('employee')


# In[ ]:


#server (facebook data store) and client (your personal computer) communicate
# client makes a request
# server responds

import requests as r
r.get('https://www.aljazeera.com/news/2020/06/03/coronavirus-travel-restrictions-border-shutdowns-by-country/')


# In[ ]:


#from collections import Counter
# in delhi string elh, del, hi are a substring
# overlapping substrings


str1 = 'ABCDCDC'
print(str1.count('CDC'))


# In[ ]:


import re 
str1 = 'CDCD'

len(re.findall('(?=CD)', str1))


# In[ ]:





pos = s1.find(s2, 5) 
pos


#find(substring,start)


# In[ ]:





# In[ ]:


s1 = 'ABCDCDC'
s2 ="CDC"
pos = s1.find(s2, 0) 
print(pos)

pos = pos+pos
print(s1.find(s2, pos))

pos = pos+pos
print(s1.find(s2, pos))


# In[ ]:


s1 = 'ABCDCDC'
s1.count("CDC")


# In[ ]:


s1 = 'ABCDCDC'
s2 ="CDC"
pos = s1.find(s2, 6) 
print(pos)


# In[ ]:




