class FileHandler:
    def get_data_from_file(self, file_name: str) -> list:
        return self.read_file(file_name)

    def read_file(self, file_name: str) -> list:
        contents = []
        file = './source/data/' + file_name
        try:
            with open(file, 'r') as x:
                content = x.read()
            contents = list(map(int, content.split(' ')))

        except FileNotFoundError:
            print(f'File {file_name} was not found.')
            exit()

        return contents

    def save_data(self, file_name, data):
        file = './source/data/' + file_name
        to_save = " ".join(str(data))
        try:
            with open(file, 'w') as x:
                x.write(to_save)
            print("Saved to a file successfully.")
        except:
            print("Couldn't save to a file.")