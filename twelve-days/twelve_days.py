def recite(start_verse, end_verse):
    days = ['none','first','second','third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
  
    gifts = [
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, and ",
        "a Partridge in a Pear Tree.",
    ]
    # declare empty list, and fill with append method
    verse = []
    for i in range(start_verse, end_verse +1):
        # i: index of array
        # : indicates a range
        verse.append("On the {} day of Christmas my true love gave to me: ".format(days[i])+ "".join(gifts[-i:]))
    return verse


