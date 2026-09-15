amount = int(input("Enter amount: "))
if amount <= 0:
    print("Enter valid amount")
if amount >=500:
    notes = amount//500
    print("500 X ", notes)
    amount = amount%500
if amount >=200:
    notes = amount//200
    print("200 X ", notes)
    amount = amount%200
if amount >=100:
    notes = amount//100
    print("100 X ", notes)
    amount = amount%100
if amount >=50:
    notes = amount//50
    print("50 X ", notes)
    amount = amount%50
if amount >=20:
    notes = amount//20
    print("20 X ", notes)
    amount = amount%20
if amount >=10:
    notes = amount//10
    print("10 X ", notes)
    amount = amount%10
if amount >=5:
    notes = amount//5
    print("5 X ", notes)
    amount = amount%5
if amount >=2:
    notes = amount//2
    print("2 X ", notes)
    amount = amount%2
if amount >=1:    
    print("1 X ", notes)
