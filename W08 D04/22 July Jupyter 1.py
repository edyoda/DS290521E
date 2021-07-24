#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# COLLECTIONS

#deque
#counter
#OrderdDict
#Chainmap

#Datetime

# append()
# appendleft()
# extend
# extendleft
# insert
# pop
# popleft



#1. DeQUE
#2. Counter
#3. OrderedDict


dq = collections.deque([4,5,6])

print(dq)
dq.append([7,3])
print(dq)
dq.appendleft(300)
print(dq)
dq.insert(5,-10)
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)


# In[ ]:


import numpy
dir(numpy)


# In[ ]:


from collections import Counter 
list1 = ['x','x','y','y','z','z','z']
#print(Counter(list1))

str1 = "I am in a live session on EDYODA"
print(Counter(str1[:9]))


# In[ ]:


C =Counter()
C.update((1,2,3,4,4,4,4,4,'x','x'))

print(C)
del C['x']
print(C)


# In[ ]:


for i in C.elements():
    print(i)


# In[ ]:


a = 'aabcdefghojnklcnknvkndvnvslsd'

print(Counter(a))

A =Counter(a)
for i in A.elements():
    print(i)

from collections import OrderedDict
# In[ ]:


OD = collections.OrderedDict({'a':1,'b':2,'c':3})


D ={}
D[''] = 1
D['b'] = 2
D['c'] = 3

print(D)


# In[ ]:


OD -----available 3.7
D
{'aa': 'First number', 'bb': 'Second number', 'cc': 'Third number'}

D
{'aa': 'First number', 'cc': 'Third number', 'bb': 'Second number'}


# In[ ]:


#Chainmap



OI = {'TV':1,'Batteries':2}
FMCG = {'soap':3,'shampoo':4}
PANTRY = {'floor':5,'lentils':6}

C = collections.ChainMap(OI,FMCG,PANTRY)
print(C)


# In[ ]:


list(reversed(C.maps))


# In[ ]:


C.maps


# In[ ]:


#datetime

import datetime as dt

x = dt.datetime.now()
print(x)

y = dt.date.today()
print(y)

from datetime import time
z = time(21,8,50)
z1 = time()



from datetime import datetime

z2 = datetime(2021,7,21,21,9,30)
print(z,z1,z2)


# In[ ]:


#now = dt.datetime.now()

#print(now.strftime("%B"))


TS = "12-11-2020 09:18:35"
print(TS)

datetime.strptime(TS,"%d-%m-%Y %H:%M:%S")


# In[ ]:


dir(datetime)


# In[ ]:


import random
A = random.choice([1,2,3,4,5])
print(A)

def sq(x):
    if x==4:
        yield yes
    else:
        True
        
        
next(sq(A))


# In[ ]:


#mport pandas as pd
#f = pd.read_csv('http://winterolympicsmedals.com/medals.csv')
#f.head()


with open('http://winterolympicsmedals.com/medals.csv','r') as f:
    print(f.readline())


# In[ ]:


import requests as r
A = r.get('https://www.aljazeera.com/news/2020/06/03/coronavirus-travel-restrictions-border-shutdowns-by-country/')
A.status_code


# In[ ]:


import requests as r
from bs4 import BeautifulSoup
wiki = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"
page = r.get(wiki)
soup = BeautifulSoup(page.text,'html.parser')


# In[ ]:





# In[ ]:


A = soup.find_all('div',class_= "lister-item mode-advanced")
len(A)

for i in A:
    x=i.find_all('h3')
    for j in x:
        print(j.find('a').get_text())
    


# In[ ]:


right_table


# In[ ]:


right_table=soup.find('table', class_='wikitable sortable plainrowheaders')


# In[ ]:


for row in right_table.find_all("tr"):
    cells = row.find_all('td')
    states=row.find_all('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
df


# In[ ]:


row = right_table.find("tr")


# In[ ]:


cells = row.find_all('td')


# In[ ]:


cells


# In[ ]:




