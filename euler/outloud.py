words = ["",]*1001
words[1] = "one"
words[2] = "two"
words[3] = "three"
words[4] = "four"
words[5] = "five"
words[6] = "six"
words[7] = "seven"
words[8] = "eight"
words[9] = "nine"
words[10] = "ten"
words[11] = "eleven"
words[12] = "twelve"
words[13] = "thirteen"
words[14] = "fourteen"
words[15] = "fifteen"
words[16] = "sixteen"
words[17] = "seventeen"
words[18] = "eighteen"
words[19] = "nineteen"
words[20] = "twenty"
words[30] = "thirty"
words[40] = "forty"
words[50] = "fifty"
words[60] = "sixty"
words[70] = "seventy"
words[80] = "eighty"
words[90] = "ninety"

for tens in xrange(2,10,1):
    for units in xrange(1,10,1):
        words[tens*10 + units] = words[tens*10] + words[units]

for hundreds in xrange(1,10,1):
    for tens in xrange(0,10,1):
        for units in xrange(0,10,1):
            i = hundreds*100 + tens*10 + units
            words[i] = words[hundreds] + "hundred"
            if tens > 0 or units > 0:
                words[i] += "and" + words[tens*10 + units]

words[1000] = "onethousand"

acc = 0
for i in xrange(1001):
    print words[i]
    acc += len(words[i])
print acc