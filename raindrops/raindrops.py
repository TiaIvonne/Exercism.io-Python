def convert(number):
    drops = ""
    if number % 3 == 0:
        # operator += a = a+1
        drops += "Pling"
    if number % 5 == 0:
        drops += "Plang"
    if number % 7 == 0:
        drops += "Plong"
    # if drops empty convert int to string
    if drops == "":
        return str(number)
    else:
        return drops 
