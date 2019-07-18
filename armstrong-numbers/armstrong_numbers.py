def is_armstrong_number(number):
    # transform number int to string (iterate word in for loop)
    word = str(number)
    result = sum([pow(int(i), len(word)) for i in word])
    return result == number
    
