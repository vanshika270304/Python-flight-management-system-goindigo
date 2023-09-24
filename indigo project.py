import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import random
import string
from tkinter import *
from datetime import date

ans="y"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
while ans=="y":
    print("\n*******************************************************************************************************\n                                               GOINDIGO.IN\n                                             www.goindigo.in\n*******************************************************************************************************")
    print("\n------------------------\n       MAIN MENU\n------------------------\n1. About Us\n2. Flight\n3. Bags And Meals\n4. Offers\n5. Baggage Information\n6. Feedback\n7. Contact Us\n8. Progress\n9. Exit")
    i=input("Enter your choice number: ")
    print()
    if i=="1":
        print("ABOUT US")
        print("\nIndiGo is India’s largest passenger airline with a market share of 55.5% as\nof October, 2020. We primarily operate in India’s domestic air travel market\nas a low-cost carrier with focus on our three pillars – offering low fares,\nbeing on-time and delivering a courteous and hassle-free experience. IndiGo\nhas become synonymous with being on-time.")
        print("\nIndiGo is not only the most efficient low fare operator domestically but is\nalso comparable with global low cost airlines. We are constantly enhancing our\nengagement with our passengers to augment their travel experience. From multichannel\ndirect sales (including online flight booking, call centers and airport counters),\nto online flight status checking, an exclusive IndiGo app for Android, we have\ntransformed air travel in India. Today, we are India’s most preferred airline.\nAt IndiGo, low fares come with high quality.\n")
        print("Our Corporate Social Responsibility (CSR) initiative IndiGoReach focuses on three\nbroad themes: Children and Education, Women Empowerment and Environment. We work\ntowards upliftment of communities not just around us but also far-flung areas in\nthe country. After all, India’s holistic progress is rooted in the collective\naspirations of its people.")
              
    elif i=="2":
        print("FLIGHT\n1. Book Flight\n2. View Booking Details\n3. Cancel Booking\n4.Main Menu")
        a=int(input("Enter your choice number: "))
        if a==1:
            f={"BOOKING CODE":[241,356,367,457,854,884,754,355,643,251,246,469,769,654,375,247,257,567,270,213,464,287,352,583,358,425,197,235,699,435],"FLIGHT NO.":["6E2345","6E5467","6E5698","6E2865","6E9423","6E3209","6E4560","6E872","6E927","6E9235","6E398","6E8745","6E3987","6E5498","6E2985","6E2543","6E7329","6E4034","6E3762","6E3402","6E5438","6E2387","6E456","6E329","6E4098","6E465","6E765","6E3854","6E3219","6E4076"],"ORIGIN":["AHMEDABAD","AHMEDABAD","AHMEDABAD","BENGALURU","BENGALURU","BENGALURU","CHENNAI","CHENNAI","CHENNAI","DELHI","DELHI","DELHI","GUWAHATI","GUWAHATI","GUWAHATI","HYDERABAD","HYDERABAD","HYDERABAD","KOLKATA","KOLKATA","KOLKATA","MUMBAI","MUMBAI","MUMBAI","PUNE","PUNE","PUNE","VISAKHAPATNAM","VISAKHAPATNAM","VISAKHAPATNAM"],"DESTINATION":["MUMBAI","PUNE","VISAKHAPATNAM","GUWAHATI","HYDERABAD","KOLKATA","BENGALURU","CHENNAI","DELHI","PUNE","VISAKHAPATNAM","AHMEDABAD","HYDERABAD","KOLKATA","MUMBAI","CHENNAI","DELHI","GUWAHATI","VISAKHAPATNAM","AHMEDABAD","BENGALURU","KOLKATA","MUMBAI","PUNE","DELHI","GUWAHATI","HYDERABAD","AHMEDABAD","BENGALURU","CHENNAI"],"DAY":["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY","MONDAY","TUESDAY"],"DEPARTURE TIME":["10:30","13:20","12:30","11:25","10:15","13:45","14:15","11:30","10:10","16:20","9:25","10:50","11:40","9:30","10:10","18:45","14:20","10:05","9:20","12:30","14:05","10:05","11:40","9:35","15:05","17:25","11:35","20:15","10:40","11:05"],"ARRIVAL TIME":["11:50","15:05","14:10","12:50","11:20","14:45","16:10","13:05","11:15","17:10","10:40","11:55","12:50","11:10","11:30","20:05","15:35","11:40","10:45","14:10","15:35","11:35","12:55","10:55","16:50","18:45","12:50","21:35","11:55","12:40"],"ECONOMY CLASS":[4500,3500,5500,4500,5000,3500,4500,5000,4500,4000,4500,5000,4000,4500,5000,4000,4500,5000,3500,5000,4500,3500,4000,5000,3500,4000,4500,3500,4500,5000],"BUSINESS CLASS":[7000,7500,8000,8000,6500,7000,7500,8000,7500,8000,8500,7000,7500,8000,7500,7000,7500,8000,8500,7000,7500,8000,8500,7500,7000,7500,8000,7500,8000,7500],"FIRST CLASS":[9000,9500,10000,11500,9500,9000,10500,11000,9500,9150,10500,11000,9500,9000,10000,11000,9500,10500,11000,9500,9000,10500,11000,11500,9500,9000,11000,9500,10000,10500]}
            df=pd.DataFrame(f)
            print(df)
         
            d={}
            l=[]
            l1=[]
            print("BOOK YOUR FLIGHTS HERE \n ")
            t=int(input("Enter the number of travellers: "))
            for i in range(t):
                n=input("Enter full name: ")
                l.append(n)
                ag=int(input("Enter the age: "))
                l1.append(ag)
                print()
                d["NAME"]=l
                d["AGE"]=l1
            d["CONTACT NO."]=int(input("Enter contact number: "))
            d["EMAIL ID"]=input("Enter email id: ")

            z=int(input("\nEnter the booking code of the flight you want to book: "))
            for a,k in df.iterrows():
                if k["BOOKING CODE"]==z:
                    d["FLIGHT NO."]=k["FLIGHT NO."]
                    d["ORIGIN"]=k["ORIGIN"]
                    d["DESTINATION"]=k["DESTINATION"]
                    o=input('Enter a date in YYYY-MM-DD format: ')
                    d["DATE"]=o
                    d["DAY"]=k["DAY"]
                    N=6
                    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
                    PNR=str(res)
                    d["PNR"]=PNR
                    print("\nSPECIAL ASSISTANCE\n\nIf you need some help along your journey, we’ll make sure you’re safe and comfortable all the way. Let us know the type of assistance you need at the airport and during your flight.No extra fee is charged.\n\n1.Passengers using wheelchairs (mobility assistance)\n2.Passengers travelling with crutches/ braces/ other prosthetic devices\n3.Passengers with Visual Impairment\n4.Passengers Travelling with Certified Guide Dogs\n5.Passengers with Hearing Impairment\n6.Passenger travelling with spinal support\n7.Passenger travelling with an assistant for medical purposes\n8.Passengers with intellectual/ developmental/ learning disabilities\n9.Passengers travelling with Internal Medical Devices\n10.Passengers who require a stretcher\n11.Passengers requiring oxygen aid")
                    w=input("\nIf you require any special assistance, you will be contacted on the contact number provided by you shortly.\nDo you require any special assistance(y/n)?")
                    if w=="y":
                        d["SPECIAL ASSISTANCE"]="YES"
                    else:
                        d["SPECIAL ASSISTANCE"]="NO"
                        
                    print("\nClASS:\n1. Economy\n2. Business Class\n3. First Class")
                    cl=int(input("Enter the class number in which you would like to travel:"))
                    if cl==1:
                        price=(k["ECONOMY CLASS"])*t
                    if cl==2:
                        price=(k["BUSINESS CLASS"])*t
                    if cl==3:
                        price=(k["FIRST CLASS"])*t

            print("\nChoose the offer applicable (if any)\nDISCLAIMER: Only 1 offer applicable.\n")
            co={"PROMO CODE":["TH45U","SE3721","KI764F","TDF34F","EG43SD"],"OFFER NAME":["INDUSLND BANK OFFER","STUDENT FARE","SENIOR CITIZEN","ARMED FORCES","TOUGH COOKIE DISCOUNT"],"DESCRIPTION":["Enjoy 12% Discount.Pay using IndusInd Bank Credit Cards.","Applicable for students, above the age of 12 years. A valid student ID is mandatory at the time of check-in for verification. This discount entitles you with 6% off on base fare and an extra baggage allowance of 10kg (for bookings made 7 days in advance). Failure in producing relevant ID will result in charging prevailing fares.","Senior citizens above the age of 60 will get 6% off on the base fare.","10% discount on base fare is provided for bookings made under Defence category and is open to serving and retired Defence and paramilitary personnel.","Applicable for doctors and nurses, this Tough Cookie discount entitles up to 25% off. A valid ID is mandatory."]}
            of=pd.DataFrame(co)
            print(of)
            pr=input("Enter the promo code (press enter to skip): ")
            if pr=="TH45U" or pr=="th45u":
                price=price-(0.12*price)
            if pr=="SE3721" or pr=="se3721":
                price=price-(0.06*price)
            if pr=="KI764F" or pr=="ki764f":
                price=price-(0.06*price)
            if pr=="TDF34F" or pr=="tdf34f":
                price=price-(0.10*price)
            if pr=="EG43SD" or pr=="eg43sd":
                price=price-(0.25*price)
            print("\nTOTAL AMOUNT TO BE PAID INCLUSIVE OF ALL TAXES IS",price)
            d["TOTAL AMOUNT"]=price

            an="y"
            while an=="y":
                print("\nPAYMENT METHODS: \n1. Credit Card/Debit Card\n2. Internet Banking\n3. Wallet\n4. Unified Payment Interface(UPI)\n5. Credit Shell")
                pa=int(input("\nEnter the choice number of your payment mode: "))
                if pa==1:
                    print("\nCREDIT/DEBIT CARD")
                    cardno=int(input("Enter the card number: "))
                    month=int(input("Enter the expiry month: "))
                    year=int(input("Enter the expiry year: "))
                    nam=input("Enter the card holder's name: ")
                    cvv=int(input("Enter cvv: "))
                    break
                if pa==2:
                    print("\nINTERNET BANKING")
                    user=input("Enter the User ID: ")
                    pas=input("Enter the password: ")
                    break
                if pa==3:
                    print("\nWALLET")
                    mobile=int(input("Enter the mobile number: "))
                    otp=int(input("Enter the OTP: "))
                    break
                if pa==4:
                    print("\nUNIFIED PAYMENT INTERFACE")
                    upi=input("Enter your UPI ID: ")
                    pas=input("Enter the password: ")
                    break
                if pa==5:
                    count=0
                    c=pd.read_csv("c:/ip/creditshell.csv")
                    p=input("Enter the PNR: ")
                    for i in c.index:
                        if c.PNR[i]==p:
                        #count=count+1
                            a=c.CREDIT[i]
                            print("You have INR",a,"IN YOUR CREDIT SHELL")
                            t=a-price
                            if t>0 or t==0:
                                print("INR",t,"is left in your credit shell")
                                c.CREDIT[i]=t
                                print(c.CREDIT[i])
                                print(c)
                                c.to_csv("c:/ip/creditshell.csv")
                                continue
                            
                            else:
                                print("INSUFFICIENT AMOUNT IN YOUR CREDIT SHELL")
                            an=input("Please enter 'y' to see other payment options:")
                            break

                        else:
                            print("\nINVALID PNR\n")   

            u=pd.DataFrame(d)
            s=u[["PNR","NAME","AGE","CONTACT NO.","EMAIL ID","FLIGHT NO.","ORIGIN","DESTINATION","DATE","DAY","TOTAL AMOUNT","SPECIAL ASSISTANCE"]]
            v=u[["NAME","CONTACT NO.","FLIGHT NO.","ORIGIN","DESTINATION","DATE"]]            
           
            con=int(input("\nEnter contact number again: "))
            print("\n**********PAYMENT DONE SUCCESSFULLY**********\n---------------------------------------------\n**************BOOKING COMPLETED**************\n")
           
           
            print("DETAILS OF THE BOOKING:\n ")
            for i,j in s.iterrows():
                if j["CONTACT NO."]==con:
                    print(j)
           
            for i,j in v.iterrows():
                if j["CONTACT NO."]==con:
                    class Flight:
                        def __init__(self,root):
                            self.root=root
                            self.root.geometry("1350x700+0+0")
                            self.root.title("flight")
                            title=Label(self.root,text="IndiGo",bd=5,bg="blue",relief=GROOVE,fg="white",font=("oswald",50,"bold"),pady=2).pack(fill=X)
                            t1=Text(root)
                            t1.pack()
                            t1.insert("end",s)
                           
                    root=Tk()
                    obj=Flight(root)
                    root.update()
              
            s.to_csv("c:/ip/flight.csv",mode="a")
            print("\n*********************************************\n--------------THANK YOU SO MUCH--------------")
               
        if a==2:
            count=0
            s=pd.read_csv("flight.csv")
            p=input("Enter the PNR: ")
            for i,j in s.iterrows():
                if j["PNR"]==p:
                    print("\nDETAILS OF THE BOOKING:\n ")
                    count=count+1
                    print(j)
                    class Flight:
                        def __init__(self,root):
                            self.root=root
                            self.root.geometry("1350x700+0+0")
                            self.root.title("flight")
                            title=Label(self.root,text="IndiGo",bd=5,bg="blue",relief=GROOVE,fg="white",font=("oswald",50,"bold"),pady=2).pack(fill=X)
                            t1=Text(root)
                            t1.pack()
                            t1.insert("end",s)
                           
                    root=Tk()
                    obj=Flight(root)
                    root.update()
       
            if count==0:
                print("\nINVALID PNR\n")
               
        if a==3:
            print("\nTERMS AND CONDITIONS:\n1.You can cancel your flight booking online and get a refund depending on the date of your cencellation.\n2.In case the ticket is not cancelled within the stipulated time,no refund will be given.\n3.When cancelling a flight 3 or less days prior, you will be charged INR 1,500 as cancellation fee and the balance amount will be refunded.\n4.When cancelling a flight 4 or more days prior, you will be charged INR 2,000 as cancellation fee and the balance amount will be refunded.\n")            
            count=0
            s=pd.read_csv("flight.csv")
            p=input("Enter the PNR: ")
            for i,j in s.iterrows():
                if j["PNR"]==p:
                    count=count+1
                    o=j["DATE"]
                    pr=j["TOTAL AMOUNT"]
                    year, month, day = map(int, o.split('-'))
                    date1 =date(year, month, day)
                    v=date.today()
                    n=abs((v-date1).days)
                    print()
                    if n>3:
                        print(n,"DAYS ARE LEFT FOR THE CANCELLATION.\nHENCE,YOU WILL CHARGED INR 2,000 AS CANCELLATION FEES AND THE BALANCE AMOUNT WILL BE REFUNDED.\n")
                        t=pr-2000
                        print("TOTAL AMOUNT THAT WILL BE REFUNDED INCLUSIVE OF ALL TAXES= INR",t)
                    else:
                        print(n,"DAYS ARE LEFT FOR THE CANCELLATION.\nHENCE,YOU WILL CHARGED INR 1,500 AS CANCELLATION FEES AND THE BALANCE AMOUNT WILL BE REFUNDED.\n")
                        t=pr-1500
                        print("TOTAL AMOUNT THAT WILL BE REFUNDED INCLUSIVE OF ALL TAXES= INR",t)


                    a=input("\nDo you want to cancel your flight booking(y/n)?")
                    if a=="y" or a =="Y":
                         print("\nChoose Preferred Option:\n1.Avail refund to my card/bank account.\n2.Avail refund to my credit shell for future reservations.")
                         ch=int(input("Enter your choice number: "))
                         if ch==1:
                             print("\nINR",t,"would be credited to your card/bank account within 7 days.")
                         elif ch==2:
                             d1={"PNR":p,"CREDIT":t}
                             d2=pd.DataFrame(d1,index=[1])
                             d2.to_csv("c:/ip/creditshell.csv",mode="a")
                             
                             print("\nINR",t,"has been credited to your credit shell. The credit shell is valid to book until 1 year from today. You may choose your travel date as per your convenience.")
                         else:
                             print("INVALID CHOICE")
                               
                    print("\n\n********************************************************************\n---------------YOUR FLIGHT BOOKING HAS BEEN CANCELLED---------------")

            if count==0:
                print("\nINVALID PNR\n")
           
    elif i=="3":
        print("BAGS AND MEALS")
        print("1. Excess Baggage\n2. 6E Tiffin\n3. Fast Forward\n4. Blanket,Pillow and Eye shade\n5. Main Menu")
        A=int(input("Enter your choice number: "))
        if A==1:
            print("EXCESS BAGGAGE")
            print()
            print("Pre book additional baggage on your booking.")
            print()
            print("Travel with us seamless even while you have excess baggage.It costs ₹500 per excess kilogram")
            print()           
        if A==2:
            print("6E TIFFIN")
            print("Our lean, clean flying machine is ready to serve you your favourite from 6E Tiffin, available on flights. In order to minimise contact, snacks are open for pre-booking only purchase of the same on board is currently not permitted. Choose from a range of delectables and get snacking!")
            D={"BOOKING CODE":["CFDG","GERD","TSHF","UFYD","JSHG","PDHT","JDGS","DTJG","JDKG","BXED","FTAS","BKDS"],"MENU":["Paneer Tikka Sandwich","Chicken Tikka Sandwich","Chicken Keema With Kulcha","Kadhai Paneer Naan","Veg Trio Sandwich","Non-Veg Trio Sandwich","Cashew Nuts","Chocolate Chip Cookies","2 Dips with Baked Pita","Diabetic Non-Veg","Jain Meal","Chicken Supreme Salad"],"PRICE":["₹350","₹375","₹400","₹450","₹450","₹450","₹200","₹150","₹450","₹450","₹350","₹450"]}
            E=pd.DataFrame(D)
            print(E)
        if A==3:
            print("FAST FORWARD")
            print()
            print("CHECK IN FIRST AND GET YOUR BAG(s) BEFORE ANYONE ELSE")
            print()
            print("Saving time and making your flying experience seamless is our priority.")
            print()
            print("IT COSTS ₹450 PER PERSON")
            print()
            print("Booking a flight with INDIGO entitles the passengers to priority check-in, priority baggage-drop at a separate FFWD counter at the airport and priority baggage pick-up for travel.")
        if A==4:
            print("BLANKET, PILLOW AND EYE SHADE")
            print()
            print("Night flight or day trip, afternoon meeting or evening red-eye return, a blanket, pillow eye shade and a dental kit is all you need to hit afresh")
            print()
            print("IT COSTS ₹200 PER PERSON")
        if A==5:
            continue
        
        count=0
        s=pd.read_csv("flight.csv")
        p=input("Enter the PNR: ")
        e=input("enter mail: ")
        for i,j in s.iterrows():
            if j["PNR"]==p and j["EMAIL ID"]==e:
                count=count+1
                      
        if count>0:
            if A==1:
                B=int(input("Enter the excess kilogram: \n"))
                C=B*500
                print("\nTOTAL AMOUNT TO BE PAID FOR THE EXCESS BAGGAGE IS",C)
            if A==2:
                T=input("\nEnter the booking code of the food you want to book: ")
                for A,Y in E.iterrows():
                    if Y["BOOKING CODE"]==T:
                        R=Y["MENU"]
                        V=Y["PRICE"]
                print("YOU HAVE BOOKED",R)
                print("TOTAL AMOUNT TO BE PAID FOR FOOD IS",V)
            if A==3:
                W=len(s)
                Q=450*W
                print("TOTAL AMOUNT TO BE PAID FOR FAST FOWARD SERICE IS",Q)
            if A==4:
                 H=int(input("Enter no. of kits you wil need (only one available per person): \n"))
                 print()
                 G=200*H
                 print("TOTAL AMOUNT TO BE PAID FOR THE BLANKET,PILLOW AND EYE SHADE IS",G)
             
            print("\nPAYMENT METHODS: \n1. Credit Card/Debit Card\n2. Internet Banking\n3. Wallet\n4. Unified Payment Interface(UPI)")
            pa=int(input("\nEnter your the choice number of your payment mode: "))
           
            if pa==1:
                print("\nCREDIT/DEBIT CARD")
                cardno=int(input("Enter the card number: "))
                month=int(input("Enter the expiry month: "))
                year=int(input("Enter the expiry year: "))
                nam=input("Enter the card holder's name: ")
                cvv=int(input("Enter cvv: "))
            if pa==2:
                print("\nINTERNET BANKING")
                user=input("Enter the User ID: ")
                pas=input("Enter the password: ")
            if pa==3:
                print("\nWALLET")
                mobile=int(input("Enter the mobile number: "))
                otp=int(input("Enter the OTP: "))
            if pa==4:
                print("\nUNIFIED PAYMENT INTERFACE")
                upi=input("Enter your UPI ID: ")
                pas=input("Enter the password: ")
            con=int(input("\nEnter contact number again: "))
            print("\n-------------PAYMENT DONE SUCCESSFULLY-------------\n-------------BOOKING COMPLETED-------------\n-------------THANK YOU SO MUCH-------------")

        else:
            print("\nINVALID PNR\n")
   

    elif i=="4":
        print("OFFERS")
        print("\n*DISCLAIMER*\nAPPLICABLE ONLY WHILE BOOKING A FLIGHT!")
        print()
        co={"PROMO CODE":["TH45U","SE3721","KI764F","TDF34F","EG43SD"],"OFFER NAME":["INDUSLND BANK OFFER","STUDENT FARE","SENIOR CITIZEN","ARMED FORCES","TOUGH COOKIE DISCOUNT"],"DESCRIPTION":["Enjoy 12% Discount.Pay using IndusInd Bank Credit Cards.","Applicable for students, above the age of 12 years. A valid student ID is mandatory at the time of check-in for verification. This discount entitles you with 6% off on base fare and an extra baggage allowance of 10kg (for bookings made 7 days in advance). Failure in producing relevant ID will result in charging prevailing fares.","Senior citizens above the age of 60 will get 6% off on the base fare.","10% discount on base fare is provided for bookings made under Defence category and is open to serving and retired Defence and paramilitary personnel.","Applicable for doctors and nurses, this Tough Cookie discount entitles up to 25% off. A valid ID is mandatory."]}
        of=pd.DataFrame(co)
        print(of)
               
    elif i=="5":
        print("BAGGAGE INFORMATION")
        print("\nHAND BAGGAGE\nOne hand bag up to 7 kgs and 115 cms, shall be allowed per customer. For contactless travel we recommend to place it under the seat in front, on board.")
        print()
        print("CHECK-IN BAGGAGE\n15 Kgs per person (One piece only). Baggage in excess of 15 kgs will be subject to additional charges of ₹500 per kg.\nExcess Baggage charges are non-refundable in case of no shows and gate no shows.\nIn addition to the one piece of Hand Baggage permitted to be carried in accordance with the above, IndiGo will permit a Customer to carry one additional personal article such as ladies’ purse or a small bag containing laptop not weighing more than 3 kgs.\nItems determined by us to be of an offensive nature, will not be permitted on board.\nSubject to the prevalent applicable local laws and regulations, Customers may carry liquids in their Hand Baggage, subject to screening and security checks, and provided they meet the following restrictions:\nAny liquid is in a container with a maximum volume of 100ml")
        print("\nPLEASE NOTE\nJEWELRY: IndiGo does not hold any liability on carrying cash or jewellery but it is subject to clearance by the airport regulatory authorities.\nMUSICAL INSTRUMENTS:Carriage of musical instruments is allowedat no additional cost. Guitars, if packed in soft cases, can be carried in hand baggage, however, other instruments have to be properly packed and can be carried in Check-in baggage only.")
        print()
        print("DANGEROUS GOODS\n\nPROHIBITED GOODS IN CHECK-IN BAGGAGE:\n1. Compressed gases - deeply refrigerated, flammable, non-flammable and poisonous such as butane oxygen, liquid nitrogen, aqualung cylinders and compressed gas cylinders.\n2.Corrosives such as acids, alkalis, mercury and wet cell batteries and apparatus containing mercury.\n3.Flammable liquids and solids such as lighter refills, lighter fuel, matches, paints, thinners, fire-lighters, lighters that need inverting before ignition, matches (these may be carried on the person), radioactive material, briefcases and attache case with installed alarm devices.\n4.Explosives, munitions, fireworks and flares, ammunition including blank cartridges, handguns, fire works, pistol caps.\n\nPROHIBITED GOODS IN CABIN BAGGAGE:\n1.Dry cell batteries.\n2.Knives, scissors, Swiss army knives and other sharp instruments.\n3.Weapons such as whips, nan-chakus, baton, or stun gun.\n4.Any other items which are deemed security hazards by local law")

    elif i=="6":
        print("FEEDBACK")
        p=input("Enter your PNR:")
        a=int(input("\nHow would you rate your overall experience with us?\n1. Excellent\n2. Good\n3. Satisfactory\n4. Bad\nChoose the appropriate number:"))
        b=int(input("\nDid we meet your expectations?\n1. Excellent\n2. Good\n3. Satisfactory\n4. Bad\nChoose the appropriate number:"))
        c=int(input("\nHow would you rate your interaction with our employees?\n1. Excellent\n2. Good\n3. Satisfactory\n4. Bad\nChoose the appropriate number:"))
        d=int(input("\nWas it easy to find what you were looking for?\n1. Excellent\n2. Good\n3. Satisfactory\n4. Bad\nChoose the appropriate number:"))
        e=int(input("\nHow easy is it to navigate our website?\n1. Excellent\n2. Good\n3. Satisfactory\n4. Bad\nChoose the appropriate number:"))
        f=int(input("\nHow likely are you to recommend our company to a friend or colleague?\n1. Excellent\n2. Good\n3. Satisfactory\n4. Bad\nChoose the appropriate number:"))
        g=int(input("\nIs our pricing clear?\n1. Excellent\n2. Good\n3. Satisfactory\n4. Bad\nChoose the appropriate number:"))
        h=int(input("\nHow would you rate our service?\n1. Excellent\n2. Good\n3. Satisfactory\n4. Bad\nChoose the appropriate number:"))
        i=input("\nIs there anything you would like to add or suggest?")
        d={"QUESTION 1":a,"QUESTION 2":b,"QUESTION 3":c,"QUESTION 4":d,"QUESTION 5":e,"QUESTION 6":f,"QUESTION 7":g,"QUESTION 8":h,"QUESTION 9":i}
        df=pd.DataFrame(d,index=[p])
        df.to_csv("C:/ip/feedback.csv",mode="a")
        print("\n--------THANK YOU SO MUCH FOR YOUR FEEDBACK!--------\n--------WE ONLY HOPE TO MAKE YOUR EXPERIENCE BETTER!--------\n--------WE HOPE YOU FLY WITH US SOON!--------")


        print("\n--------THANK YOU SO MUCH FOR YOUR FEEDBACK!--------\n--------WE ONLY HOPE TO MAKE YOUR EXPERIENCE BETTER!--------\n--------WE HOPE YOU FLY WITH US SOON!--------")

    elif i=="7":
        print("CONTACT US")
        print("\nREGISTERED OFFICE\nCIN : L62100DL2004PLC129768\nUpper Ground Floor, Thapar House, Gate No. 2, Western Wing, 124 Janpath, New Delhi – 110001 India.\nFax : +91 11-43513200")
        print("\nCORPORATE OFFICE\nLevel 1, Tower C, Global Business Park, Mehrauli-Gurgaon Road, Gurgaon – 122 002, Haryana, India.\nTel : +91 (0)124 435 2500\nFax : +91 (0)124 406 8536")
        print("\nCUSTOMER SUPPORT\nIndia : 0124-6173838, 0124-4973838\nChina : +86-4006063838")

    elif i=="8":
        a=["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
        b=[16,12,15,15,18,12,12,11,24,21,7]
        pl.bar(a,b)
        pl.ylabel("INCOME(IN CRORES)")
        pl.xlabel("PROGRESSIVE YEARS")
        pl.title("INCOME DURING THE YEARS")
        pl.show()
        m=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
        u=[14.3,14.6,16,16.8,19.1,18,16,18.6,19.1,18.9,19.7,23.2]
        v=[22.8,22.3,22.9,24.8,27.7,25.4,24.2,23.9,24.3,25.9,26,27.4]
        w=[27.26,27.54,30.23,30.67,33.37,30.23,28.9,33.3,32.90,33.9,37.73,38.9]
        y=[34.5,36.5,37.9,2,2.3,1.9,2.9,5.5,6.2,7.6,8.9,10]
        pl.plot(m,u,linewidth=5,marker="o",markerfacecolor="black",markersize=8,label="2017",color="red")
        pl.plot(m,v,linewidth=5,marker="o",markerfacecolor="black",markersize=8,label="2018",color="blue")
        pl.plot(m,w,linewidth=5,marker="o",markerfacecolor="black",markersize=8,label="2019",color="green")
        pl.plot(m,y,linewidth=5,marker="o",markerfacecolor="black",markersize=8,label="2020",color="yellow")
        pl.legend()
        pl.ylabel("NO. OF PASSENGERS(IN LAKHS)")
        pl.title("PASSENGERS CARRIED BY INDIGO OVER THE YEARS")
        pl.show()
        z=[55.5,14.3,12.9,10.3,7]
        name=["INDIGO","JET AIRWAYS","SPICEJET","AIR INIDA","GO AIR"]
        pl.pie(z,labels=name,autopct="%1.1f%%")
        pl.title("INDIGO'S CURRENT MARKET SHARE")
        pl.show()
        print("HAPPY TO HELP YOU!")
        print("HAPPY TO HELP YOU!")
   
    elif i=="9":
        print("********************************************************************************************************\n                                           THANK YOU SO MUCH\n********************************************************************************************************")
        break
   
    else:
        print("INVALID CHOICE NUMBER")
    ans=input("\n\nDO YOU WANT TO RETURN TO THE MAIN MENU(y/n)?: ")
