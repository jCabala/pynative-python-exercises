if __name__ == "__main__":
    print("Exercise 1")
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    dict = {keys[i] : values[i] for i in range(len(keys))}
    print(dict)

    print("\nExercise 2")
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    dict1.update(dict2)
    print(dict1)

    print("\nExercise 3")
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    print(sampleDict["class"]["student"]["marks"]["history"])

    print("\nExercise 4")
    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}
    print(dict.fromkeys(employees, defaults))

    print("\nExercise 5")
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }

    # Keys to extract
    keys = ["name", "salary"]
    dict = {key: sample_dict[key] for key in keys}
    print(dict)

    print("\nExercise 6")
    # Uses same values as ex 5
    sample_dict = {key: sample_dict[key] for key in sample_dict.keys() - keys}
    print(sample_dict)

    print("\nExercise 7")
    sample_dict = {'a': 100, 'b': 200, 'c': 300} 
    print(200 in sample_dict.values())

    print("\nExercise 8")
    sample_dict = {
        "name": "Kelly",
        "age":25,
        "salary": 8000,
        "city": "New york"
    }
    sample_dict["location"] = sample_dict["city"]
    del sample_dict["city"]
    print(sample_dict)

    print("\nExercise 9")
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }

    print(max(sample_dict.values()))
