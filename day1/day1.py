def calculateCaptchaPartOne(data):
    if (len(data) == 0):
        return 0

    counter = 0
    result = 0
    first = int(data[0])
    
    while (counter < len(data)):
        current = int(data[counter])
        
        # When on last element -> next = first element
        if (counter == len(data) - 1):
            next = first;
        else:
            next = int (data[counter + 1])

        if (current == next):
            result += current
        
        counter += 1

    print "Result of Captcha Ont: ", result

def calculateCaptchaPartTwo(data):
    if (len(data) == 0):
        return 0

    counter = 0
    result = 0
    steps = len(data) / 2
    
    while (counter < len(data)):
        current = int(data[counter])

        # When past last element -> next = index - steps
        if (counter + steps > len(data) - 1):
            circularCounter = counter-steps
            next = int(data[circularCounter])
        else:
            next = int (data[counter + steps])

        if (current == next):
            result += current
        
        counter += 1

    print "Result of Captcha Two: ", result

f = open('input.txt', 'r')
content = f.read()
f.close()

calculateCaptchaPartOne(content)
calculateCaptchaPartTwo(content)

