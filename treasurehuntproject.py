teaasures=[0,1,0,1,-1,1,1,-1,1,1]
chance=1
while chance<6:
    print("this is your chance ",chance)
    slots=input("Enter your 4 slot choice :")
    print("you entered ",slots)
    
    s1=int(slots[0])
    s2=int(slots[2])
    s3=int(slots[4])
    s4=int(slots[6])
    s1, s2, s3, s4 = map(int, slots.split(","))
    t1=teaasures[s1]
    t2=teaasures[s2]
    t3=teaasures[s3]
    t4=teaasures[s4]
    if t1==-1 or t2==-1 or t3==-1 or t4==-4:
           print("Game over\n --**-- You hit BOMB --**--")
    elif t1+t2+t3+t4==4:   
          print("you won the match")
          chance=chance+1
    
else:
    print("you losed")        