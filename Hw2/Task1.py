n = int(input('Введите число n: '))
print(n)

def multiply_table(value:int):
    for i in range(1, n + 1):
        print("\n")
        for j in range(1, n +1):
            print(f'{j} * {i} = {j * i}')

multiply_table(n)