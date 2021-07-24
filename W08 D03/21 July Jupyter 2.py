#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests as req


# In[ ]:


response.url


# In[ ]:


response.status_code


# In[ ]:


from bs4 import BeautifulSoup


# In[ ]:


import requests as req


# In[ ]:


url = "https://snooplay.in/"
r = req.get(url)


# In[ ]:


r.status_code


# In[ ]:


soup = BeautifulSoup(r.text,"html.parser")


# In[ ]:


print(soup.title).text()


# In[ ]:


##find
##find_all

A = soup.find_all("p")


# In[ ]:


len(A)


# In[ ]:


print(soup.title.text)


# In[ ]:


url1= "https://www.bookdepository.com/bestsellers"


# In[ ]:


R = req.get(url1)


# In[ ]:


soup1 = BeautifulSoup(R.text,"html.parser")


# In[ ]:


print(soup1.title.text)


# In[ ]:


A = soup1.find_all("div",class_ = "item-info")
print(len(A))


# In[ ]:


for h in A:
    B = h.find("p",class_ = "author")
    C = h.find("p",class_ = "published")
    try:
        print(B.get_text(strip =True))
        print(C.get_text(strip =True))
    except:
        print("There was some item with no savings")
        


# In[ ]:


A[0].get_text(strip =True)


# In[ ]:




