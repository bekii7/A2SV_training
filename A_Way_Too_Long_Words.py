word = input()

if type(word) == str and len(word) > 10:
    print(word[0] + str(len(word) - 2) + word[-1])
    
elif type(word) == str and len(word) <= 10:
    print(word)
else:
    print()