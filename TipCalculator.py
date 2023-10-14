print("Welcome to the tip calaculator.")
totalBill = float(input("What was the total bill? $"))
percentageTip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
splitByHowMany = int(input("How many people to split the bill? "))
calculateTip = round(percentageTip/100,2)
billWithTip = totalBill * (1+calculateTip)
totalPerPerson = "{:.2f}".format(billWithTip/splitByHowMany)

print(f"Each person should pay: ${totalPerPerson}")
