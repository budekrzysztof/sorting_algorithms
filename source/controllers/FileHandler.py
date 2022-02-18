class FileHandler:
    def get_data(self, path: str):
        contents = []
        try:
            with open(path, 'r') as x:
                content = x.read().strip()
            contents = list(map(int, content.split(' ')))
        except FileNotFoundError:
            if path:
                print(f"File at location '{path}' was not found.")
            else:
                print("You must choose a file first.")
        except:
            print("File contains unrecognized characters.")
        return contents

    def save_data(self, file_path: str, data: list):
        try:
            to_save = " ".join(str(data))
            with open(file_path, 'w') as x:
                for row in data:
                    if row != str(data[-1]):
                        row = str(row) + " "
                    else:
                        row = str(row)
                    x.write(row)
            print("Saved to a file successfully.")
        except:
            print("Couldn't save to a file.")
