import random

class Utils:
    """
    as an input parameters it takes filename in format 'name.extension',
    min and max for range of numbers for generator
    and q for a quantity of generated numbers
    output is saved as ./data/name.extension
    """
    def generate_random_numbers_to_file(self, file_name: str, min: int, max: int, q: int) -> list:
        try:
            file = './data/' + file_name
            numbers = []

            for i in range(q):
                numbers.append(str(random.randint(min, max)))

            with open(file, 'w') as x:
                x.write(" ".join(numbers))
        except:
            print("An error occurred while trying to generate random numbers into that location.")

    def generate_random_numbers(self, min: int, max: int, q: int) -> list:
        numbers = []

        for i in range(q):
            numbers.append(int(random.randint(min, max)))

        return numbers
