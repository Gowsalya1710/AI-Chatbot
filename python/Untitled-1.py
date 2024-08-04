""" MEDIGUIDE """
n=input("Enter the disease:",)
a=[" ",
   "fever:",
   "drug:asprin",]

b=[" ",
   "ulcer:",
   "drug:omeprazole,alumina,magnesia syrup",]

c=[" "
   "skin alergy:",
   "drug:caladryl lotion",]
d=[" "
   "headache:",
   "drug:paracetamol",]

e=[" "
   "acidity:",
   "drug:protonix",]

f=["stomach pain:",
   "drug:ioperamide",]

if(n=="fever"):
    for i in a:
        print(i)
    
elif(n=="ulcer"):
    for j in b:
        print(j)

elif(n=="skin alergy"):
    for k in c:
        print(k)

elif(n=="headache"):
    for l in d:
        print(l)

elif(n=="acidity"):
    for m in e:
        print(m)

elif (n=="stomach pain"):
    for h in f:
        print(h)

else:
    print("I dont know")
    