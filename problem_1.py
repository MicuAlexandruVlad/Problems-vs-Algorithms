

def findBound(number):
    i = 0

    if number < 0:
        return -1
    elif number == 0 or number == 1:
        return number
    else:
        while True:
            if i ** 2 <= number <= (i + 1) ** 2:
                break
            else:
                i += 1

    if abs(i ** 2 - number) < abs((i + 1) ** 2 - number):
        return i
    
    return i + 1

def sqrt(number):
    lowerBound = findBound(number)
    if lowerBound < 0:
        return -1
    if lowerBound > 0:
        s1 = number / lowerBound
        s2 = (s1 + lowerBound) / 2

        return int(s2 // 1)
    
    return 0

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print(sqrt(-3))


