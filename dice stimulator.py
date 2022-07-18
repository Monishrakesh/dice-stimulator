import random
ch = 'r'
while ch == 'r':
    num = random.randint(1,6)
    
    if num == 1:
        print("---------------")
        print("|             |")
        print("|             |")
        print("|      O      |")
        print("|             |")
        print("|             |")
        print("---------------")
        
    if num == 2:
        print("---------------")
        print("|  O          |")
        print("|             |")
        print("|             |")
        print("|             |")
        print("|          O  |")
        print("---------------")
        
    if num == 3:
        print("---------------")
        print("|  O          |")
        print("|             |")
        print("|      O      |")
        print("|             |")
        print("|          O  |")
        print("---------------")
        
    if num == 4:
        print("---------------")
        print("|  O       O  |")
        print("|             |")
        print("|             |")
        print("|             |")
        print("|  O       O  |")
        print("---------------")
    
    if num == 5:
        print("---------------")
        print("|  O       O  |")
        print("|             |")
        print("|      O      |")
        print("|             |")
        print("|  O       O  |")
        print("---------------")
        
    if num == 6:
        print("---------------")
        print("|  O       O  |")
        print("|             |")
        print("|  O       O  |")
        print("|             |")
        print("|  O       O  |")
        print("---------------")
        
    ch = input("Press r to roll the die again..")
