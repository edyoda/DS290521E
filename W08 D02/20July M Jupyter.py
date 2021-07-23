#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
    print(2+"a")
except NameError:
    print("exception")
except ZeroDivisionError:
    print("exception2")
except:
    print("3rd error")
else:
    print("4th error")


# In[ ]:


import pandas as pd
import numpy


# In[ ]:


def all_even():
    n=2
    while True:
        yield n
        n+=2


# In[ ]:


x = all_even()


# In[ ]:


next(x)


# In[ ]:


#f.read(10)
#f.readline()
#f.close()
#f.read()

#change current directory


import os
os.chdir("C:\Yogesh\EDYODA")
#C
#mode  r w a x
# two main arguments


# open (arguments,mode)

with open("Text.txt", "w")   as f:
    f.write("if you want to Overwrite something")


# In[ ]:


f  = open("Text.txt","w")    
f.read()


# In[ ]:


f.write("overwrite")
f.close()


# In[ ]:


finally: 
    f.close()


# In[ ]:


import csv


# In[ ]:


with open ("IRIS.csv","r") as file:
    f = csv.reader(file)
    for row in f:
        print(row[])


# In[ ]:


# reading csv with Pandas
import pandas as pd


# In[ ]:


df = pd.read_csv("IRIS.csv")


# In[ ]:


df.head(5)


# In[ ]:


#Writing /downloading a csv

data = [["TOM",10],["Jerry",5],["MINI",3]]
type(data)
df1 = pd.DataFrame(data,columns=["CHAR","RATING"])
df1.head()
df1.to_csv("LIVE2.csv",index=False)


# In[ ]:


#JSON

data = {"size":"medium",
       "price": 15,
        "topping" : ['mushroom',"olive","basil"],
        "extra_cheese":False
       }


# In[ ]:


data
import json


# In[ ]:


with open("TEXT1.json","r") as file:
    data = json.load(file)
    print(data['orders'][1]['client'])


# In[ ]:


df = pd.read_json("TEXT1.json")
df


# In[ ]:


with open("TEXT_new.json","w") as file:
    json.dump(data,file)


# In[ ]:


import xml.etree.ElementTree as ET


# In[ ]:


tree =  ET.parse("movies.xml")


# In[ ]:


root = tree.getroot()


# In[ ]:


for child in root:
    print(child.tag)


# In[ ]:


for elem in root:
    for subelem in elem:
        print(subelem.attrib)


# In[ ]:


# JSON CSV XML
# open (filename, mode)
#mode = r w a x
#import json-----json.load()
#import csv------csv.reader()
#import ET from XML parse ...for loops

#.txt -----read(5), readlines(), 
#f.close()------use finally:



# In[ ]:


# to get through the hierarchy
for i in root:
    row=[]
    name = i.find("name").text
    phone = i.find("phone").text
    
    row.append({"name":name,"phone":phone})
    
    print(row)
    
    
column = ["name","phone"]

df = pd.DataFrame(row,columns=column)

df.to_csv("LIVE20-E.csv")

