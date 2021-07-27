#!/usr/bin/env python
# coding: utf-8

# In[20]:


import time,csv,random


def Signup(v):


    if v == "Y":
        
        time.sleep(1)
        print('please login to continue')
        time.sleep(2)

        user_id = input("please enter your email id:  ")
        time.sleep(1)
        password = input("please enter your password:  ")
        time.sleep(1)
        print('Logging in...')
        time.sleep(1)

        
    elif v =="N":
        
        time.sleep(1)
        print('please register to continue')
        
        
        time.sleep(1)
        
        FN = input('Enter your Full Name\n')
        CN = input('Enter your Contact Number\n')
        Email= input('Enter your Email\n')
        Address = input('Enter your Address\n')
        time.sleep(1)
        
        print('Sccessfully Registered! Please Refresh and login to continue\n')
        time.sleep(1)
        user_id = input("please enter your email id:  ")
        time.sleep(1)
        password = input("please enter your password:  ")
        time.sleep(1)
        print('Logging in...')
        time.sleep(1)
        
    else:
        print('Looking for an appropriate input from you. lets create an account for you')
        Signup("N")
        
        
#option()
        
       


# In[13]:


def S_action(a):
    
    import time,csv
    

    if a==1:
        time.sleep(1)
        print("please enter the details of the product you want to add")
        productname = input('enter product name:  ')
        time.sleep(1)
        mfname =      input('enter mfname:  ')
        time.sleep(1)
        price =       input('enter price:  ')
        time.sleep(1)
        quantity=     input('enter quantity:  ')
        time.sleep(2)

        print("Congrats! Successfully addded the product")


        with open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details.csv','a') as f:
            file= csv.writer(f)
            file.writerow(['PROD' ,productname , mfname , price , quantity])

    ###########################################################################################################            

    elif a==2:
        UP2 =  {}
        time.sleep(1)

        print("please enter the ID of the product you want to update")
        prod = input('Product ID:  ')


        time.sleep(1)
        print("press 2 to change Manufacturer")
        print("press 3 to change Price")
        print("press 4 to change Quantity")
        time.sleep(1)

        I = input('What property do you want to change/update? ')
        U = input('Please write the updated entry ')

        UP2[str(I)] = I

        with open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details.csv') as in_file, open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details_1.csv', 'w',newline='') as out_file:
            reader = csv.reader(in_file)
            writer = csv.writer(out_file)
            for row in reader:
                if row[0]==prod:
                    print('updating row for PROD_ID ', row[0]," and ", row[1])
                    row[int(I)]= U
                writer.writerow(row)

        time.sleep(2)
        print('Update completed')


    ###########################################################################################################        

    elif a==3:
        time.sleep(1)

        print("please enter the details of the product you want view")
        prod = input('Product ID:  ')

        with open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details.csv','r') as f:
            file= csv.reader(f)
            for row in file:
                if row[0] == str(prod):
                    print("Below are the details of product you are looking for: \n")
                    time.sleep(1)
                    print("Product name:  ",row[1])
                    print("Product manufacturer:  ",row[2])
                    print("Product Price:  ",row[3])
                    print("Product Quantity:  ",row[4])


    ###########################################################################################################                    

    elif a==4:
        time.sleep(1)

        print("please enter the details of the product you want to delete")
        prod = input('Product ID:  ')

        with open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details.csv') as in_file, open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details_1.csv', 'w',newline='') as out_file:
            reader = csv.reader(in_file)
            writer = csv.writer(out_file)
            for row in reader:
                if row[0]!=prod:
                    writer.writerow(row)

            time.sleep(1)
            print("You have successfully removed the product ")
            
    else:
        print('expecting better input')
        


# In[17]:


def option():
    import time
    print('press 1 to Create Product')
    time.sleep(1)
    print('press 2 to Update Product')
    time.sleep(1)
    print('press 3 to View Product')
    time.sleep(1)
    print('press 4 to Delete Product')
    action= int(input('your input: '))
    
    return action
    


# In[21]:


visitor = input("Welcome visitor! are you a customer? Are you a seller? \n")
print('Hello there! ')
user = input("Do you already have an account?")
    

Signup(user)

S_action(option())


# In[38]:


#OOP

# collection of object
# car is an object
# attributes : model, brand, color, height
# underscore

class car:
    pass

O = car()

#constructor

class car:
    def __init__(self,name,color):
                 self.name =name
                 self.color = color 
    
    type = "hatchback"
    
    #method
    
    def aboutme(self):
        return f"the {self.name} has a {self.color} color"
    
    for i in range(10):
        x = i+10
    

    
    
    
# above i =9, x=19            
# self : parameter
# color : attribute



#class : 4 tyres----class attributes
# color red ----    instance attribute
        

#methods ---- a function defined as an attribute 


#aboutme: instance method


# In[39]:


C = car('maruti','wine red')

print(C.i,C.x)


# In[ ]:




