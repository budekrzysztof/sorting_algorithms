class FileHandler:

    def get_data(self, path: str) -> list:
        contents = []
        try:
            with open(path, 'r') as x:
                content = x.read()
            contents = list(map(int, content.split(' ')))
        except FileNotFoundError:
            if path:
                print(f"File at location '{path}' was not found.")
            else:
                print("You haven't choose any file.")
            exit()
        return contents

    def save_data(self, file_path, data):
        try:
            to_save = " ".join(str(data))
            with open(file_path, 'w') as x:
                for row in data:
                    row = str(row) + " "
                    x.write(row)
            print("Saved to a file successfully.")
        except:
            print("Couldn't save to a file.")
