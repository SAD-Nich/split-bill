billcount = float(input("Enter bill total:"))
tipcount = int(input("How generous are the diners?:"))
peoplecount = int(input("Enter Diners Amount:"))
payment = (round(float(((tipcount/100 +1)*billcount)/peoplecount),2))
print(f"Each person has to pay: ${payment}")
tippay =float((tipcount/1)/peoplecount)
print(f"each person tips ${tippay}")