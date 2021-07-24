#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup as bs
import requests


# In[ ]:


url = "https://www.bookdepository.com/bestsellers"
response = requests.get(url)


# In[ ]:


html = response.content


# In[ ]:


#html


# In[ ]:


soup = bs(html, "lxml")


# In[ ]:


all_h3 = soup.find_all("h3",class_ = "title")
for h3 in all_h3:
    
    print(h3.get_text(strip=True))
    for p in h3.find_all("p",class_ = "price"):
        print(p)


# In[ ]:


a=soup.find_all("div",class_ = "item-info")
for i in a:
    print(i.find("h3",class_ = "title").get_text())
    try:
        print(i.find("p",class_ = "price-save").get_text())
    except:
        print("no savings")
    


# In[ ]:




