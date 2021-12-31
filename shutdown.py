import os

#List of options
print("1. shutdown ")
print("2. hibernate")
print("3. restart")
print("4. lock")
print("5. exit")

#input choice
choice = int(input("Input option : "))
#choice selected from option menu
if(choice>=1 and choice<=4):
    if choice==1:
        os.system("shutdown /s /t 2")
    if choice==2:
        os.system("shutdown /h")
    if choice==3:
        os.system("shutdown /r /t 2")
    if choice==4:
        os.system("shutdown /l")
else:
    exit()
