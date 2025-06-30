base=float(input("Base Salary: "))
hra=float(input("HRA: "))
epf=float(input("EPF Deduction: "))
ppf=float(input("PPF Deduction: "))
salary=base+hra-epf-ppf
print("Gross Salary is:", salary)
tax_rate=float(input("Tax Rate(%): "))/100
tax_amount=salary*tax_rate
print("Tax amount is: ",tax_amount)
in_hand=salary - tax_amount
print("In hand salary is: ",in_hand)