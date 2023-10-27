if __name__ == "__main__":
    print("Exercise 1 (Modified)")
    l1 = [3, 6, 9, 12, 15, 18, 21]
    l2 = [4, 8, 12, 16, 20, 24, 28]
    print(f"L1: {l1}\nL2: {l2}\n")
    
    res = [l1[i] if i % 2 else l2[i] for i in range(len(l1))]
    print(res)

    print("\nExercise 2")