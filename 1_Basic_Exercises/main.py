def getEvenChars(str1):
    return str1[::2]

def popChars(str1, n):
    assert(n >= 0 and n < len(str1))
    return str1[n:]

def filterDiv(arr, n):
    return list(filter(lambda a : not (a % n), arr))

def printPyramid(n):
    for i in range(n):
        for j in range(i):
            end = "\n" if j + 1 == i else " "
            print(i, end=end)

def firstOddSecondEven(list1, list2):
    filteredL1 = list (filter(lambda a: a % 2, list1))
    filteredL2 = list (filter(lambda a: not (a % 2), list1))

    filteredL1.extend(filteredL2)
    return filteredL1

firstTaxRatio = 0.1
restTaxRatio = 0.2
freeAmount = 10000
firstTaxAmount = 10000

def taxFrom(n):
    firstTax = min(firstTaxAmount, max(0, n - firstTaxAmount)) * firstTaxRatio

    restTax = max(0, n - freeAmount - firstTaxAmount) * restTaxRatio

    return  firstTax + restTax

def printMulTable(n):
    assert(n > 0)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            end = "\n" if j == n else " "

            print(i * j, end=end)

def printStarPyramid(n):
    assert(n > 0)
    for i in range(n, 0, -1):
        for j in range(i):
            end = "\n" if j == i - 1 else " "
            print("*", end=end)



if __name__ == '__main__':
    
    print("Exercise 3")
    str1 = "123456789"
    print(getEvenChars(str1))

    print("\nExercise 4")
    str1 = "1111222222222"
    n = 4
    print(popChars(str1, n))

    print("\nExercise 6")
    arr = [10, 11, 15, 16, 20, 21, 25, 26]
    n = 5
    print(filterDiv(arr, n))

    print("\nExercise 7")
    str1 = "Emma is good developer. Emma is a writer"
    sub = "Emma"
    print(f"{sub} appeard {str1.count(sub)} times")

    print("\nExercise 8")
    n = 7
    printPyramid(n)

    print("\nExercise 10")
    list1 = [10, 20, 25, 30, 35]
    list2 = [40, 45, 60, 75, 90]
    print(firstOddSecondEven(list1, list2))

    print("\nExercise 11")
    n = 7536
    print(f"Reversed {n} is {str(n)[::-1]}")
    
    print("\nExercise 12")
    n = 45000
    print(f"Tax from {n}$ is {taxFrom(n)}$")

    print("\nExercise 13")
    n = 10
    printMulTable(n)

    print("\nExercise 14")
    n = 7
    printStarPyramid(n)