from utility.Timer import Timer
from controllers.Builder import Builder

def run():
    file_name = input('Whats the file name? ')
    sorting_method = input('Sorting method? merge/bubble ').lower()
    sorting_order = input('Sorting order? asc/desc ').lower()

    with PerformanceTimer():
        result = Builder().run(file_name, sorting_method, sorting_order)

    file_name = sorting_order + "_sorted_" + file_name
    Builder().finish(file_name, result)


run()



