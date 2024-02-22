wt=int(input("Enter Weight: "))
unit=input("Enter unit of weight: ")
con_unit=input("Enter unit to convert to: ")
if unit == "kg":
    if con_unit == "lbs":
        wt*=2.204623
        print("Weight in LBS is: " +str(wt))
    elif con_unit == "grams":
        wt=wt*1000
        print("Weight in grams is: " +str(wt))
    else:
        print("Enter Appropriate conversion unit")
elif unit == "grams":
    if con_unit == "kg":
        wt=wt/1000
        print("Weight in Kg is: " +str(wt))
    elif con_unit == "lbs":
        wt=wt*0.002204623
        print("Weight in lbs is: " +str(wt))
    else:
        print("Enter appropriate conversion unit")
elif unit == "lbs":
    if con_unit == "kg":
        wt=wt*2.204623
        print("Weight in Kgh is: "+str(wt))
    elif con_unit == "grams":
        wt=wt/0.002204623
        print(" Weight in Grams is: "+str(wt))
    else:
        ("Enter valid conversion unit")
else:
    print("Enter Appropriate unit")