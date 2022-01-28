def sixlen():
    with open('foods.txt', 'r') as f: # reads the last line of the text file
        lines = f.read().splitlines()
        ll = lines[-1]
        ll = int(ll[:6]) + 1
        num = str(ll)
    array = []
    barcode = ""
    temp = num
    for x in range(len(num)): array.append(num[x])
    while len(array) != 6: array.append("0")
    for x in range(len(array)): barcode += array[-1-x]
    return barcode

def pricelen(price): # makes sure it follows the same format as the rest of the prices within the foods text file (3 digits before the decimal, 2 after)
    price = round(price, 2)
    strprice = str(price)
    end = strprice[-3:]
    strprice = strprice[:-3]
    array = []
    newprice = ""
    for x in range(len(strprice)): array.append(strprice[-1-x])
    while len(array) != 3: array.append("0")
    for x in range(len(array)): newprice += array[-1-x]
    newprice += end
    return newprice

def namelen(name):
    while len(name) != 10: name += " "
    return name

def append(data):
    with open("foods.txt", "a") as f:
        f.write(data)
    
finished = False
while not finished:
    name = input("input name, enter x to exit. \n")
    if name == "x" or name == "X": finished = True
    if not finished: # checks it twice so it doesn't ask everything even if the user said that they were finished
        while len(name) > 10 and name != "x" and name != "X": name = input("please input a name which is 10 letters or less, or enter x to exit. \n")
        if name != "x" and name != "X":# checks it again if they change their mind
            price = float(input("input price, with a decimal (eg: 16.05) \n"))
            while price > 999.99 and price < 0: price = float(input("invalid price. Make sure it is less than £999.99. \n"))
            k = int(input("is this a product with a price per kg? type 1 for yes, 2 for no \n"))
            while k != 1 and k != 2: k = int(input("please use 1 for yes, or 2 for no in terms of price per kilo. \n"))
            if k == 1: k = "pkg"
            else: k = ""
            name = namelen(name)
            price = pricelen(price)
            barcode = sixlen()
            data = barcode +" " + name + " " + k + " " + price + " " + "\n" # concatenates
            append(data)
        else: finished = True
