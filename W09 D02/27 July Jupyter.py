#!/usr/bin/env python
# coding: utf-8

# In[9]:



import time,csv
class Product:
   'Common base class for all Product'
   prodCount = 0
   prod_list=[] 
   
   H =[] 

   def __init__(self, PROD, MANF, PRICE, QUAN):
      self.PROD = PROD
      self.MANF = MANF
      self.PRICE = PRICE
      self.QUAN = QUAN
        
      Product.prodCount += 1
    
      Product.prod_list.append([self.PROD, self.MANF, self.PRICE, self.QUAN])  
   
   def displayCount(self):
     print("Total Product %d" % Product.prodCount)

   def displayProduct(self):
      print("PROD : ", self.PROD,  " MANF: ", self.MANF, " PRICE: ", self.PRICE , " QUAN: ", self.QUAN)
      print(Product.prod_list)
        
   def deleteProduct(self):
    
      PROD = input('enter the product you want to Delete\n\n')
      for i in range(len(Product.prod_list)):
            if Product.prod_list[i][0] == PROD:
                Product.prod_list.pop(i)
                H.append('Delete')
                break
      print(Product.prod_list)
    
      
    
   def CreateProduct(self):
      print('Enter the below details\n\n')
        
      pn= input('enter product name:  ')
      time.sleep(1)
      mf= input('enter mfname:  ')
      time.sleep(1)
      price =   input('enter price:  ')
      time.sleep(1)
      qn=input('enter quantity:  ')

      Product.prod_list.append([pn,mf,price,qn])

      print(Product.prod_list)
      H.append('Create')
        
        
   def ViewProduct(self):
    
      PROD = input('enter the product you want to View\n\n')
      print('showing details for: ',PROD)
      
      for i in range(len(Product.prod_list)):
            if Product.prod_list[i][0] == PROD:
                print("PROD :     ",Product.prod_list[i][0])
                print("MANF:      ", Product.prod_list[i][1])
                print("PRICE:     ", Product.prod_list[i][2])
                print("QUANTITY:  ", Product.prod_list[i][3])
                
                break
      H.append('View')


# In[1]:


class Signup:
    
    def __init__(self):
        self.cred = {}
    def reg(self, user, passw):
        self.cred[user] = passw

    def check(self, user, pas):
        print(self.cred )
        if user in self.cred.keys() and pas == self.cred[user] :
            
            print("Successful! Welcome to amazon")
            
        else:
            print('Incorrect Entry!')

        


# In[ ]:


s = Signup()

refresh = False

while refresh == False:
    action = (input('What would you like to do? enter Reg  Login  exit \n'))

    if action == 'Reg':
        
        Name = (input('Please enter username '))
        passw= (input('Please enter password '))
        s.reg(Name, passw)

    if action == 'Login':
        
        Name1 = (input('Please enter Username '))
        passw1 = (input('Please enter Password '))
        s.check(Name1,passw1)
        refresh =True
        
    if action == 'exit':
        
        print("See you later!")
        refresh =True
        
    


# In[4]:



P =Product('PROD','MANF','PRICE','QUAN')

print(P.prod_list)

P.CreateProduct()
P.CreateProduct()
P.CreateProduct()
P.CreateProduct()







# 

# In[10]:


P =Product('PROD','MANF','PRICE','QUAN')

print(P.prod_list)

P.CreateProduct()
P.CreateProduct()
P.CreateProduct()
P.CreateProduct()

P.ViewProduct()

P.deleteProduct()


# In[6]:





# In[ ]:





# In[ ]:




