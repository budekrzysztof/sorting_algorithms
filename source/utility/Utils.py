import random

class Utils:
    def generate_random_numbers_to_file(self, file_name: str):
            try:
                file = './data/' + file_name
                numbers = []

                for i in range(1000):
                    numbers.append(str(random.randint(0, 1000)))

                with open(file, 'w') as x:
                    x.write(" ".join(numbers))
            except:
                print("An error occurred while trying to generate random numbers into that location.")

    def generate_random_numbers(self, min, max, q):
        numbers = []

        for i in range(q):
            numbers.append(int(random.randint(min, max)))

        return numbers
