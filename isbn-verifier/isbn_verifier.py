def is_valid(isbn):
    counter = 1
    total = 0
    for digits in reversed(isbn):
        if digits is 'X':
            if counter != 1:
                return False
            digits = '10'
        if digits.isdigit():
            total += int(digits) * counter
            counter += 1
    return counter == 11 and total % 11 == 0
    