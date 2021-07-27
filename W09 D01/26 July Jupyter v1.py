#!/usr/bin/env python
# coding: utf-8

# In[43]:


import time,csv
visitor = input("welcome! are you a customer? Are you a seller")

if visitor =='c':
    
    print('Hello customer')
    time.sleep(1)
    print('please login to continue')
    time.sleep(1)
    
    user_id = input("please enter your email id:  ")
    time.sleep(1)
    password = input("please enter your password:  ")
    
    time.sleep(1)
    print('Logging in...')
    time.sleep(1)
    
    print('Please select any item from the menu:')                   
    print('press 1 to Create Product')
    time.sleep(1)
    print('press 2 to Update Product')
    time.sleep(1)
    print('press 3 to View Product')
    time.sleep(1)
    print('press 4 to Delete Product')
    
    action= int(input('your input: '))
        
    if action==1:
        time.sleep(1)
        print("please enter the details of the product you want to add")
        productname = input('enter product name:  ')
        time.sleep(1)
        mfname =      input('enter mfname:  ')
        time.sleep(1)
        price =       input('enter price:  ')
        time.sleep(1)
        quantity=     input('enter quantity:  ')
        time.sleep(1)
        
        with open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details.csv','a') as f:
            file= csv.writer(f)
            file.writerow(['PROD',productname,mfname,price,quantity])
            
    if action==2:
        time.sleep(1)
            
        print("please enter the details of the product you want to update")
        prod = input('Product ID:  ')
        
        with open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details.csv','r') as f:
            file= csv.reader(f)
            for row in file:
                if row['Product'] == str(prod):
                    row = {'Product': row['Product'], 'Name': row['Name'], 'Manufacturer': row['Manufacturer'], 'Price': row['Price'],'Quantity': row['Quantity']}
                    writer.writerow(row)
                    
    if action==3:
        time.sleep(1)

        print("please enter the details of the product you want to view")
        prod = input('Product ID:  ')

        with open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details.csv','r') as f:
            file= csv.reader(f)
            for row in file:
                if row[0] == str(prod):
                    print("Product name:  ",row[1])
                    print("Product manufacturer:  ",row[2])
                    print("Product Price:  ",row[3])
                    print("Product Quantity:  ",row[4])
                
                
    if action==4:
        time.sleep(1)
        
        print("please enter the details of the product you want to view")
        prod = input('Product ID:  ')
                
        with open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details.csv') as in_file, open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details_1.csv', 'w',newline='') as out_file:
            reader = csv.reader(in_file)
            writer = csv.writer(out_file)
            for row in reader:
                if row[0]!=str(prod):  # exclude a specific row
                    writer.writerow(row)


    else:
        print('exit')


# In[ ]:



    


# In[ ]:





# In[ ]:





# In[ ]:




