import mysql.connector as mt
con=mt.connect(host="localhost",user="root",passwd="root",database="adib")
# DEFINITON INSERT()
def insert():
 print('*'*60)
 print("NEW CUSTOMER")
 print('*'*60)
 Name=input("ENTER YOUR NAME PLEASE \n")
 Phonenum=int(input("ENTER YOUR PHONE NUMBER PLEASE \n"))
 Address=input("ENTER YOUR DELIVERY ADDRESS PLEASE \n")
 Email=input("ENTER YOUR EMAIL ADRESS PLEASE \n")
 cur=con.cursor()
 cur.execute("insert into Customerinfo values('%s',%s,'%s','%s')"%(Name,Phonenum,Address,Email))
 con.commit()
 print("Logged in successfully......")
 print('*'*60)

# DEFINITION DISPLAY()
def display():
    print('*'*60)
    print("YOUR DETAILS")
    print('*'*60)
    Ph=int(input("Please enter your phone number to continue \n"))
    cur=con.cursor()
    cur.execute("select * from Customerinfo where Phone_no =%s"%(Ph))
    data=cur.fetchall()
    for row in data:
     print(row)
    print('*'*60)
    cur=con.cursor()
    cur.execute("select Phone_no from Customerinfo")
    data=cur.fetchall()
    c=0
    for row in data:
     if row[0]==Ph:
      c=1
      break
    if c==0:
     print("User not found")
     print('*'*60)
# DEFINITION UPDATE()
def update():
 print('*'*60)
 print("UPDATE DETAILS")
 print('*'*60)
 Ph=int(input("Please enter your phone number to continue \n"))
 cur=con.cursor()
 cur.execute("select * from Customerinfo where Phone_no =%s"%(Ph))
 data=cur.fetchall()
 for row in data:
  print(row)
 print('*'*60)
 cur=con.cursor()
 cur.execute("select Phone_no from Customerinfo")
 data=cur.fetchall()
 c=0
 for row in data:
  if row[0]==Ph:
   c=1
   break
 if c==0:
  print("User not found")
 else:
  c1='y'
  while (c1=='y' or c1=='Y'):
   print("1. CHANGE NAME")
   print("2. CHANGE PHONE NUMBER")
   print("3. CHANGE DELIVERY ADDRESS")
   print("4. CHANGE EMAIL ADRESS")
   changechoice=int(input("Enter choice please"))
   if changechoice==1:
    Name=input("Enter new name \n")
    cur=con.cursor()
    cur.execute("update Customerinfo set Name='%s' where Phone_no=%s"%(Name,Ph))
    con.commit()
    print("Details updated successfully...")
    print('*'*60)
   elif changechoice==2:
    Phonenum=int(input("Enter new Phone number \n"))
    cur=con.cursor()
    cur.execute("update Customerinfo set Phone_no=%s where Phone_no=%s"%(Phonenum,Ph))
    con.commit()
    cur.execute("Select Phone_no from Item")
    data=cur.fetchall()
    c=0
    for row in data:
        if row[0]==Ph:
         c=1
         break
    if c==0:
        print('')
    else:
        cur=con.cursor()
        cur.execute("update Item set Phone_no=%s where Phone_no=%s"%(Phonenum,Ph))
        con.commit()
    print("Details updated successfully...")
    print('*'*60)
   elif changechoice==3:
    Address=input("Enter new delivery Address \n")
    cur=con.cursor()
    cur.execute("update Customerinfo set Address='%s' where Phone_no=%s"%(Address,Ph))
    con.commit()
    print("Details updated successfully...")
    print('*'*60)
   elif changechoice==4:
    Email=input("Enter new Email Address \n")
    cur=con.cursor()
    cur.execute("update Customerinfo set Email='%s' where Phone_no=%s"%(Email,Ph))
    con.commit()
    print("Details updated successfully...")
    print('*'*60)
   else:
    print("Please enter a valid choice")
    print('*'*60)
   c1=input("Want to update more details : press y for yes and press n for no \n")
# DEFINITION DELETE()
def delete():
        print('*'*60)
        print("DELETE ACCOUNT")
        print('*'*60)
        Ph=int(input("Please enter your phone number to continue \n"))
        cur=con.cursor()
        cur.execute("select Phone_no from customerinfo")
        data=cur.fetchall()
        c=0
        for row in data:
            if row[0]==Ph:
                c=1
                break
        if c==0:
            print("Record not found")
        else:
            print("Your account details are:")
            cur.execute("Select * from customerinfo where Phone_no=%s"%(Ph))
            data=cur.fetchall()
            for row in data:
                print(row)
            print('*'*60)
            cur.execute("delete from customerinfo where Phone_no=%s"%(Ph))
            con.commit()
            print("Account deleted successfully....")
            cur.execute("Select Phone_no from Item")
            data2=cur.fetchall()
            b=0
            for row in data2:
                if row[0]==Ph:
                 b=1
                 break
            if b==0:
                print('')
                
             
            else:
                cur=con.cursor()
                cur.execute("delete from Item where Phone_no=%s"%(Ph))
                con.commit()
        print("*"*60)
          
# DEFINITION SHOP()
def shop():
 print('*'*60)
 print("LET'S SHOP")
 print('*'*60)
 Ph=int(input("Enter your phone number please to continue \n"))
 print('*'*60)
 cur=con.cursor()
 cur.execute("select Phone_no from Customerinfo")
 data=cur.fetchall()
 c=0
 for row in data:
  if row[0]==Ph:
   c=1
   break
 if c==0:
  print("User not found please create a account first")
 else:
  c1='y'
  while (c1=='y' or c1=='Y'):
   print("1. iPhones")
   print("2. iPads")
   print("3. Watches")
   print("4. Laptops")
   print("5. Desktops")
   print("6. Airpods")
   shopchoice=int(input("Enter choice please \n"))
   if shopchoice==1:
    print('*'*60)
    print("iPhones")
    print('*'*60)
    print("1) iPhone 11 Pro Max : ₹1,23,900")
    print("2) iPhone 11 Pro     : ₹99,900")
    print("3) iPhone 11         : ₹69,900")
    print("4) iPhone XR         : ₹54,900")
    print("5) iPhone XS         : ₹72,999")
    print("6) iPhone X          : ₹71,450")
    print("7) iPhone 8          : ₹36,999")
    Model=int(input("Please enter the model number to buy \n"))
    if Model==1:
        Item="iPhone 11 Pro Max"
        Quantity=int(input("Enter quantity to buy: \n"))
        Price=123900
        Total=Quantity*Price
        cur=con.cursor()
        cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
        con.commit()
    if Model==2:
         Item="iPhone 11 Pro" 
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=99900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    if Model==3:
         Item="iPhone 11"
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=69900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    if Model==4:
         Item="iPhone XR" 
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=54900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    if Model==5:
         Item="iPhone XS" 
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=72999
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    if Model==6:
         Item="iPhone X"
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=71450
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    if Model==7:
         Item="iPhone 8" 
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=36999
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    print("Added to Cart...")
    print('*'*60)
   elif shopchoice==2:
    print('*'*60)
    print("iPads")
    print('*'*60)
    print("1) iPad pro  : ₹1,03,900")
    print("2) iPad Air  : ₹55,900")
    print("3) iPad      : ₹40,900")
    print("4) iPad Mini : ₹45,900")
    Model=int(input("Please enter the model number to buy \n"))
    if Model==1:
         Item="iPad pro"
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=103900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    if Model==2:
         Item="iPad Air" 
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=55900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    if Model==3:
         Item="iPad"
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=40900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    if Model==4:
         Item="iPad Mini"
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=45900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    print("Added to Cart...")
    print('*'*60)
   elif shopchoice==3:
    print('*'*60)
    print("Watches")
    print('*'*60)
    print("1) Series 5  : ₹49,900")
    print("2) Series 3  : ₹29,900")
    Model=int(input("Please enter the model number to buy \n"))
    if Model==1:
         Item="Series 5 Watch"
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=49900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    if Model==2:
         Item="Series 3 Watch"
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=29900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    print("Added to Cart...")
    print('*'*60)
   elif shopchoice==4:
    print('*'*60)
    print("Laptops")
    print('*'*60)
    print("1) MacBook air (Retina) : ₹99,900")
    print("2) MacBook Pro (13in)   : ₹1,19,900")
    print("3) MacBook Pro (16in)   : ₹1,99,900")
    Model=int(input("Please enter the model number to buy \n"))
    if Model==1:
         Item="MacBook air (Retina)"
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=99900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    if Model==2:
         Item="MacBook Pro (13in)" 
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=119900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    if Model==3:
         Item="MacBook Pro (16in)"
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=199900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    print("Added to Cart...")
    print('*'*60)
   elif shopchoice==5:
    print('*'*60)
    print("Desktops")
    print('*'*60)
    print("1) iMac Pro : ₹4,64,900")
    print("2) Mac Mini : ₹75,900")
    print("3) Mac Pro  : ₹4,99,900")
    Model=int(input("Please enter the model number to buy \n"))
    if Model==1:
         Item="iMac Pro"
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=464900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    if Model==2:
         Item="Mac Mini"
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=75900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    if Model==3:
         Item="Mac Pro"
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=499900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    print("Added to Cart...")
    print('*'*60)
   elif shopchoice==6:
    print('*'*60)
    print("Airpods")
    print('*'*60)
    print("1) AirPods Pro : ₹24,900")
    print("2) AirPods     : ₹14,900")
    Model=int(input("Please enter the model number to buy \n"))
    if Model==1:
         Item="Airpods Pro"
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=24900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    if Model==2:
         Item="Airpods"
         Quantity=int(input("Enter quantity to buy: \n"))
         Price=14900
         Total=Quantity*Price
         cur=con.cursor()
         cur.execute("insert into Item values(%s,'%s',%s,%s,%s)"%(Ph,Item,Price,Quantity,Total))
         con.commit()
    print("Added to Cart...")
    print('*'*60)
   else:
    print("Please enter a valid choice")
    print('*'*60)
   c1=input("Want to buy more : press y for yes and press n for no \n")

# DEFINITION RECEIPT()
def receipt():
    print('*'*60)
    print("FINAL RECEIPT")
    print('*'*60)
    Ph=int(input("Please enter your phone number to continue \n"))
    cur=con.cursor()
    print("Your Details are:")
    cur.execute("select * from Customerinfo where Phone_no =%s"%(Ph))
    data=cur.fetchall()
    for row in data:
     print(row)
    cur=con.cursor()
    cur.execute("select Phone_no from Customerinfo")
    data=cur.fetchall()
    c=0
    for row in data:
     if row[0]==Ph:
      c=1
      break
    if c==0:
     print("Not availaible")
    print('*'*60)
    cur=con.cursor()
    print("Your Bill Details are:")
    cur.execute("select Item,Quantity,Total from Item where Phone_no=%s"%(Ph))
    data2=cur.fetchall()
    for row in data2:
     print("Items____________Quantity__Total")   
     print(row)
    cur=con.cursor()
    cur.execute("select Phone_no from Item")
    data2=cur.fetchall()
    c=0
    for row in data2:
     if row[0]==Ph:
      c=1
      break
    if c==0:
     print("Not available")
    print('*'*60)
    


 
###########################################################################################################################################################

    
c='y'
while (c=='y' or c=='Y'):
    print('*'*60)
    print("ADIB ONLINE SHOPPING")
    print('*'*60)
    print("1. NEW CUSTOMER")
    print("2. PRINT YOUR DETAILS")
    print("3. UPDATE YOUR DETAILS")
    print("4. DELETE ACCOUNT")
    print("5. CONTINUE SHOPPING")
    print("6. VIEW RECEIPT")
    ch=int(input("Enter your choice \n"))
    if ch==1:
        insert()
    if ch==2:
        display()
    if ch==3:
        update()
    if ch==4:
        delete()
    if ch==5:
        shop()
    if ch==6:
        receipt()
    if ch>=7:
        print("wrong choice entered")
        print('*'*60)
    c=input("Want to continue on portal: press y for yes and press n for no \n")
else:
    print('*'*60)
    print("Have a nice day!")
    print("Program by ADIB")
    print('*'*60)
