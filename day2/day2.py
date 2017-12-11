def calculateSpreadsheetPartOne(data):
    result = 0
    for row in data:
        numbers = map(int, row.split())
        result += max(numbers) - min(numbers)

    print "Sum of spreadsheet part 1: ", result

def calculateSpreadsheetPartTwo(data):
    result = 0
    for row in data:
        numbers = sorted(map(int, row.split()), key=int, reverse=True)
        i = 0
        while i < len(numbers):
            j = i + 1
            while j < len(numbers):
                if (numbers[i] % numbers[j] == 0):
                    result +=  numbers[i] / numbers[j]
                j += 1
            i += 1

    print "Sum of spreadsheet part 2: ", result


f = open('input.txt', 'r')
content = f.read().splitlines()
f.close()

calculateSpreadsheetPartOne(content)
calculateSpreadsheetPartTwo(content)
