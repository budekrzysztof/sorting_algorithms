import random

def read_file(file_name: str) -> list:
        contents = []
        file = './data/' + file_name
        numbers = []

        for i in range(10000):
            numbers.append(str(random.randint(0, 10000)))

        with open(file, 'w') as x:
            x.write(" ".join(numbers))



data = read_file('numbers.txt')

