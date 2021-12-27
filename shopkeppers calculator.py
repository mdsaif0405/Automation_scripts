print("the calculator")
sum = 0
while(True):
    num = input("Enter the amount")
    if(num!='q'):
        sum += int(num)
        print(f"amount is {sum}")
    else:
        print(f"billing amount : {sum}")
        break
