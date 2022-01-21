from controllers.FileHandler import FileHandler
from controllers.SortingChoose import SortingChoose

class Builder:

    def run(self, file_path):
        data = FileHandler().get_data(file_path)
        return SortingChoose().choose_method(data)

    def finish(self, file_path, data):
        save_flag = input('Want to save results? yes to proceed: ').lower()

        if(save_flag == 'y' or save_flag == 'yes'):
            try:
                save_path = file_path.split(".")[0] + "_sorted" + ".txt"
                FileHandler().save_data(save_path, data)
            except:
                print(f"An error occurred while trying to save data into a {file_path}.")

        exit()
