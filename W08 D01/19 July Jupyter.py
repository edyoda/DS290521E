#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ValueError ModuleNotFoundError NameError IndexError


# In[ ]:


#example of type error
a="one"
b=2

print(b+a)


#example of ZeroDivisionError error
for i in [5,4,3,2,1]:
    
    print(i/0)
    
#example of ModuleNotFoundError error   
import numpie


#one more

import numpie as np


# In[ ]:


#Broad Ctegories    #Syntax   #Logical    #Runtime


# In[ ]:


# Exception handling


def divide(x,y):
    try:
        "CRITICAL statement"
        result =x/y
        print("your answerr is",result)
    except:
        "NORMAL statement"
        print("You are making a mistake")
        list.append(product_name)
        
   



# In[ ]:


# two more blocks--------------else finally

amount = 3000

try:
	
	if amount < 2999:
		
		# raise the ValueError
		print("Recharge Required")
	else:
		print("You are eligible to purchase DSA Self Paced course")
			
# if false then raise the value error
except:
		print("Please try after somr time")
            
        
else: 
    print("please select the course")

finally:
     print("HAGD")


# In[ ]:


#Generators ---iterators
#next
#instead of return you write yield

def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30

x=mygenerator
x.next()


a=[1,2,3,4,5]

#example of generator expressions
y=(x*x for x in a)

next(y)


# In[ ]:


def POT():
    n=1
    print("First number")
    yield n
    
    n+=1
    print("S number")
    yield n
    
    n+=1
    print("T number")
    yield n
    
x = POT()


# In[ ]:


next(x)


# In[ ]:


def FS(nums):
    x,y=0,1
    for i in range(nums):
        x,y = y,x+y
        yield x
        

y=FS(10)


next(y)

def square(nums):
    for num in nums:
        yield num**2


# In[ ]:


print(sum(square(FS(10000))))


# In[ ]:


[x**x for x in [1,2,3]]


# In[ ]:


def GF(max):
    n=1
    while n< max:
        yield n+1
        n+=1

        

x=GF(25)
next(x)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




