from controllers.FileHandler import FileHandler
from controllers.SortingChoose import SortingChoose

class Builder:
    def run(self, file_name, sorting_method, sorting_order):
        data = FileHandler().get_data_from_file(file_name)
        sorted_data = SortingChoose().choose_method(data, sorting_method, sorting_order)
        return sorted_data

    def finish(self, file_name, data):
        save_flag = input('Want to save results? yes to proceed: ').lower()

        if(save_flag == 'y' or save_flag == 'yes'):
            FileHandler().save_data(file_name, data)

        exit()