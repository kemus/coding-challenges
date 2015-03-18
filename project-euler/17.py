ones={
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    }
teens={
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen'
    }
tens = {
    10:'ten',
    20:'twenty',
    30: 'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety'
    }

words = ""
for i in range(1,1000):
    s = str(i).zfill(3)
    h,t,o = int(s[0]), int(s[1]), int(s[2])
    if h>0:
        words+=ones[h]+"hundred"
        if t>0 or o>0:
            words+="and"
    if t>1:
        words+=tens[10*t]
        if o>0:
            words+=ones[o]
    elif t==1:
        if o>0:
            words+= teens[10+o]
        else:
            words+=tens[10*t]
    else:
        if o>0:
            words+=ones[o]
words+="onethousand"
print len(words)
