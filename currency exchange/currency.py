# the currency convertor
with open("currencyData.txt") as f:
    lines = f.readlines()

currencyDic = {}

for line in lines:
    parsed = line.split("\t")
    currencyDic[parsed[0]] = parsed[1]

print("Enter the name of currency you want to convert.\n\nAvailable Options :")
[print(items) for items in currencyDic.keys()]

inputkey = input("Enter the currency name : ")
amount = int(input("Enter the amount : "))

print(f"Currency exchange value:\n{amount} INR : {float(currencyDic[inputkey])*amount} {inputkey}")



