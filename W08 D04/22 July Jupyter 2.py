#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# requets  get post
# post 
# BeautifulSoup
# find_all
# find



#client  and  server
# Request
# Response


#html
#head
#title
#body
#heading
#paragraph <p>  </p>
#bold
#italic
#underline
#anchor tag <a>  </a>


import requests as req
R  = req.get("https://www.google.com/")

R.status_code


# In[ ]:


r= req.get("https://httpbin.org/",data = {'search':'Nanotechmology'})


# In[ ]:


r.status_code


# In[ ]:


#R.text
R.content[:200]



# In[ ]:


R1 = req.get("https://www.bookdepository.com/bestsellers")

from bs4 import BeautifulSoup as BS

soup = BS(R1.text,"html.parser")

print(soup.title)


# In[ ]:


soup.find_all("a")[3]


# In[ ]:


A = soup.find_all('div',class_ = "item-info" )


# In[ ]:


len(A)


# In[ ]:


row1= []
row2= []
for p in A:
    B= p.find("p",class_ = "price-save")
    C = p.find("p",class_ = "published")
    
    try:
        row1.append(B.get_text())
        print(B.get_text())
        row2.append(C.get_text())
        print(C.get_text())
        
    except:
        print("some error in fetching the savings---huh god knows!")


# In[ ]:


import pandas as pd

df = pd.DataFrame()

df["Date"] = pd.Series(row1)
df["Savings"] = pd.Series(row2)

print(df.head(5))


# In[ ]:


df.to_csv("C:\Yogesh_WFM\EDYODA\LIVE_21Jul.csv")


# In[ ]:


import os


# In[ ]:


os.getcwd()


# In[ ]:


list1 = ['x','y','z','x','x','x','y', 'z']


# In[ ]:


Counter(list1)


# In[ ]:


from collections import Counter


# In[ ]:


my_str = {'x': 4, 'y': 2, 'z': 2, 'z': 2}
print(Counter(my_str))


# In[ ]:


counter1 = Counter({'x1': 11, 'y': 12, 'z':2 })
counter1.most_common(2) 


# In[ ]:


counter3 = counter1- counter2
print(counter3)


# In[ ]:


C


# In[ ]:


from collections import OrderedDict
Ordered_dict = OrderedDict({'kiwi': 4, 'apple': 5, 'cat': 3})
Ordered_dict.popitem(True)
print(Ordered_dict)
Ordered_dict.popitem()
print(Ordered_dict)


# In[ ]:


import collections

dic1 = { 'a' : 1, 'b' : 2 }
dic2 = { 'b' : 3, 'c' : 4 }

chain = collections.ChainMap(dic1, dic2)


# In[ ]:


print (chain.maps)
print(chain)


# In[ ]:


print (list(chain.keys()))


# In[ ]:


list(chain.keys())


# In[ ]:


chain.new_child({'z':3,'y':30}).maps


# In[ ]:


list(reversed(chain.maps))


# In[ ]:


chain['b']


# In[ ]:


for key,value in chain.items():
    print(key,value)


# In[ ]:




