def add(a,b):
    answer = a+b
    print(f'{a} + {b} = {answer} \n')

def sub(a,b):
    answer = a-b
    print(f'{a} - {b} = {answer} \n')

def mul(a,b):
    answer = a-b
    print(f'{a} * {b} = {answer} \n')

def div(a,b):
    answer = a / b
    print(f'{a} / {b} = {answer} \n')

while True:
    
    print('-------------------------')
    print('A --> Addition')
    print('B --> Subtraction')
    print('C --> Multiplication')
    print('D --> Division')
    print('E --> Exit')
    
    choice = input('Enter your choice : ')

    if choice =='a' or choice == 'A':
        print('Addition')    
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        add(a,b)

    if choice =='b' or choice == 'B':
        print('Subtraction')    
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        sub(a,b)

    if choice =='c' or choice == 'C':
        print('Multiplication')    
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        mul(a,b)

    if choice =='d' or choice == 'D':
        print('Division')    
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        div(a,b)

    if choice =='e' or choice == 'E':
        print('Program ended')
        quit()