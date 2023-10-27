import os
folderPath = "/home/jcabala/pynative-python-exercises/2_IO_Exercises/"

def ex1():
    print("\nExercise 1")
    a = int(input("Input a: "))
    b = int(input("Input b: "))

    print(f"a * b = {a * b}")

def ex3():
    print("\nExercise 3")
    a = int(input("Enter a number: "))
    print(oct(a))

def ex4():
    print("\nExercise 4")
    a = float(input("Enter a float: "))
    print(f"{a:.2f}")

# Let user input something like [1, 2, 3, 4] and we will extract the values to the list
def ex5Modified():
    print("\nExercise 5")
    arrStr = input("Input your list of numbers: ")

    if(arrStr[0] != '[' or arrStr[len(arrStr) - 1] != ']'):
        print("Error: List should start with '[' and end with ']'")
        return

    arrStr = arrStr[1:-1]

    res = []
    for valStr in arrStr.split(","):
        val = int(valStr)
        res.append(val)

    print(res)

def ex6():
    print("\nExercise 6")
    with open(f"{folderPath}test.txt") as inputFile:
        lines = inputFile.readlines()
        for i in range(len(lines)):
            if i == 5:
                continue
            print(lines[i], end="")

    print("")

def ex9():
    print("\nExercise 9")
    filePath = folderPath + "test.txt"
    if os.stat(filePath).st_size == 0:
        print("Empty!")
    else:
        print("Not empty!")

def ex10():
    filePath = folderPath + "test.txt"
    with open(filePath) as inputFile:
        print(inputFile.readlines()[3])

if __name__ == "__main__":
    # ex1()
    # ex3()
    # ex4()
    # ex5Modified()
    # ex6()
    # ex9()
    ex10()