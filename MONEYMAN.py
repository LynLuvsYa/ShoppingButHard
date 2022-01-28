tally = []
names = []
barcode = []
finished = False
def findfood(word): # finds the food based on the 6 digit barcode.
    foods = open("foods.txt", "r")
    data = foods.readline().rstrip()
    found = False
    if data[:6] == word: found = True
    while not found and data != "":
        data = foods.readline().rstrip()
        if word == data[:6]: found = True
    if found: return data[6:]
    
def tallyprice(data, price):
    if data[19:-21] == "pkg": val = float(price) * float(input("how much does this weigh? (in KG) \n"))
    else: val = price
    val = round(val, 2)
    tally.append(val)
    

def ExitOrSee(options):
    if options == "x" or options == "X": return -1
    else:
        for x in range(len(tally)): print(barcode[x], names[x], tally[x])
def choice():
    options = input("input the 6 digit code found underneath the barcode, enter x to exit, enter ? to see the total so far. \n")
    while options == "x" or options == "X" or options == "?":
        if options != "x" and options != "X" and options != "?": ExitOrSee(options)
        options = input("input the 6 digit code found underneath the barcode, enter x to exit, enter ? to see the total so far. \n")
    data = findfood(options)
    while data == None:
        print("invalid barcode.")
        choice()
    return data

print("welcome to (copyright infringement).")
while not finished:
    data = choice()
    price = data[-6:]
    name = data[1:11]
    tallyprice(data, price)
    names.append(name)
    barcode.append(data[:6])
