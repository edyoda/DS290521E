#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# try and exception with multiple exceptions


try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except Exception as e:
    print("Unexpected error occurred---please try after some time")
finally:
    print("Bye")



    


# In[ ]:


try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except ZeroDivisionError:
    print("No zero please")  
except ValueError:
    print("no strings please")
finally:
    print("Bye")


# In[ ]:


# Pipelines Generators

def FS(nums):
    x,y= 0,1
    for i in range(nums):
        x,y = y, x+y
        yield x

result = FS(15)


# In[ ]:



def S(nums):
    for num in nums:
        yield num**2
        
result2 = S([1,2,3,4])


# In[ ]:


next(result2)


# In[ ]:


print(sum(S(FS(10))))


# In[ ]:


list1 = [1,2,3,4]
A = (x**2 for x in list1)


# In[ ]:


next(A)


# In[ ]:


import pandas as pd
df = pd.read_csv('C:\Yogesh_WFM\EDYODA\medals.csv')

print(df.head(2))


# In[ ]:


import csv
with open('C:\Yogesh_WFM\EDYODA\medals.csv',"r") as f:
    f = csv.reader(f)
    for row in f:
        print(row)
    

    
    


# In[ ]:


len(df.columns)


# In[ ]:


import xml.etree.ElementTree as ET

NAME = []
PHONE = []
EMAIL =[]
DATE = []

DICT =dict()

t = ET.parse('C:\Yogesh_WFM\EDYODA\TEST3.xml')
base = t.getroot()

print(base)

for e in base.findall('employee'):
    
    name = e.find('name').text
    NAME.append(name)
    
    phone =  e.find('phone').text
    PHONE.append(phone)
    
    email =  e.find('email').text
    EMAIL.append(email)
    
    date =  e.find('date').text
    DATE.append(date)
    
print(NAME,PHONE,EMAIL,DATE)

df= pd.DataFrame()
df['COMPANY'] =['EDYODA','EDYODA','EDYODA']
df['NAME'] = NAME
df['PHONE'] = PHONE
df['EMAIL'] = EMAIL
df['DATE'] = DATE


df.to_csv('C:\Yogesh_WFM\EDYODA\EDYODA_LIVE_XML_to_CSV.csv',index=False)


# In[ ]:


t = ET.parse('C:\Yogesh_WFM\EDYODA\TEST3.xml')


# In[ ]:





# In[ ]:


t.getroot()


# In[ ]:


base = t.getroot()
E = base.findall('employee')


# In[ ]:


NAME = []

for e in E:
    print(e.find('name').text)
    NAME.append(e.find('name').text)
    print(NAME)
    
    


# In[ ]:


import requests as r

R = r.get('https://www.aljazeera.com/news/2020/06/03/coronavirus-travel-restrictions-border-shutdowns-by-country/')
print(R.status_code)


# In[ ]:


#block1 = lister-item mode-advanced

#block2 = lister-item-content

#Anchor tag ----<a></a>


import requests as r
R = r.get('https://www.imdb.com/search/title/?groups=top_250&sort=user_rating')
from bs4 import BeautifulSoup as bs
soup = bs(R.text, 'html.parser')


# In[ ]:


#MOV =soup.find_all('div',class_ ='lister-item mode-advanced')

mov = soup.find('div',class_ ='lister-item mode-advanced')


# In[ ]:



    


# In[ ]:


A = soup.find_all('div',class_= "lister-item mode-advanced")
len(A)

for i in A:
    x=i.find_all('h3')
    for j in x:
        print(j.find('span',class_= 'lister-item-year text-muted unbold').get_text())


# In[ ]:


df = pd.read_csv('C:\Yogesh_WFM\EDYODA\medals.csv')
#print(df.head())
#print(df.tail(10))
#print(df.shape)
#print(df.columns)
#print(df[['Year','Sport']])
#df['Year_short'] = df['Year']/100
print(df)
df['City'].value_counts()


# In[ ]:





# In[ ]:




