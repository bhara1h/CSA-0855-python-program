num=int(input("Enter the number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp=temp//10
    if sum==num:
        print("Armstrong Number")
        else:
            print("not a Armstrong Number")
