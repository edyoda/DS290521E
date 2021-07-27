#!/usr/bin/env python
# coding: utf-8

# In[71]:


import time,csv

visitor = input("Welcome visitor! are you a customer? Are you a seller? \n")
if visitor =='seller':
    print('Hello Seller!')
    time.sleep(1)
    print('please login to continue')
    time.sleep(2)
    
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

################################################################    
    
    if action==3:
        
        time.sleep(1)

        print("please enter the details of the product you want view")
        prod = input('Product ID:  ')
        
        with open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details.csv','r') as f:
            file= csv.reader(f)
            for row in file:
                if row[0] == str(prod):
                    print("Below are the details of product you are looking for: \n")
                    time.sleep(1)
                    print("Product name:      ",row[1])
                    print("Manufacturer:      ",row[2])
                    print("Product Price:     ",row[3])
                    print("Product Quantity:  ",row[4])
 



################################################################    
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
        time.sleep(2)

        print("Congrats!   Successfully addded the product")

        with open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details.csv','a') as f:

            file= csv.writer(f)
            file.writerow(['PROD' ,productname , mfname , price , quantity])
        
################################################################            
    
    if action==4:
    
        time.sleep(1)

        print("please enter the details of the product you want to delete")
        prod = input('Product ID:  ')

        with open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details.csv') as in_file, open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details_1.csv', 'w',newline='') as out_file:
            reader = csv.reader(in_file)
            writer = csv.writer(out_file)
            for row in reader:
                if row[0] != prod:

                    writer.writerow(row)

        time.sleep(1)
        print("You have successfully removed the product ")

    
    
################################################################    



    if action==2:

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

        #UP2[str(I)] = I

        with open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details.csv') as in_file, open('C:\Yogesh_WFM\EDYODA\M BATCH\W09 D01\Product_details_1.csv', 'w',newline='') as out_file:
            reader = csv.reader(in_file)
            writer = csv.writer(out_file)
            for row in reader:
                if row[0]==prod:
                    print('updating row for PROD_ID ', row[0]," and ", row[1])
                    row[int(I)]= U
                writer.writerow(row)

        time.sleep(2)
        print('\nSuccessfully updated the product!')
    
    
print('\nPlease visit again')    
   


# In[ ]:




