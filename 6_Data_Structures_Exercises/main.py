if __name__ == "__main__":
    print("Exercise 1 (Modified)")
    l1 = [3, 6, 9, 12, 15, 18, 21]
    l2 = [4, 8, 12, 16, 20, 24, 28]
    print(f"L1: {l1}\nL2: {l2}\n")
    
    res = [l1[i] if i % 2 else l2[i] for i in range(len(l1))]
    print(res)

    print("\nExercise 2")
    list1 = [54, 44, 27, 79, 91, 41]
    print(list1)
    list1.insert(2, list1.pop(4))
    print(list1)

    print("\nExercise 3")
    sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    chunks = [sample_list[i * 3 : i * 3 + 3] 
         for i in range(len(sample_list) // 3)]
    
    for chunk in chunks:
        chunk.reverse()

    print(sample_list)
    print(chunks)

    print("\nExercise 4")
    sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    occurences = {}
    
    for elem in sample_list:
        if elem in occurences.keys():
            occurences[elem] += 1
        else:
            occurences[elem] = 1
    
    print(sample_list)
    print(occurences)

    print("\nExercise 5")
    first_list = [2, 3, 4, 5, 6, 7, 8]
    second_list = [4, 9, 16, 25, 36, 49, 64]
    print(set(zip(first_list, second_list)))

    first_set = {23, 42, 65, 57, 78, 83, 29}
    second_set = {57, 83, 29, 67, 73, 43, 48}
    print(f"Intersection: {first_set.intersection(second_set)}")
    print(f"First minus second: {first_set.difference(second_set)}")
