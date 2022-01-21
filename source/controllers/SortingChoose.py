from algorithms.MergeSort import MergeSort
from algorithms.BubbleSort import BubbleSort
from utility.Timer import Timer

class SortingChoose:
    def choose_method(self, data: list) -> list:
        sorted_numbers = []
        sorting_method = input('Sorting method? merge/bubble ').lower()
        sorting_order = input('Sorting order? asc/desc ').lower()

        if sorting_method == 'merge':
            if sorting_order == 'asc':
                with Timer():
                    sorted_numbers = MergeSort().sort_asc(data)
            elif sorting_order == 'desc':
                with Timer():
                    sorted_numbers = MergeSort().sort_desc(data)
        elif sorting_method == 'bubble':
            if sorting_order == 'asc':
                with Timer():
                    sorted_numbers = BubbleSort().sort_asc(data)
            elif sorting_order == 'desc':
                with Timer():
                    sorted_numbers = BubbleSort().sort_desc(data)
        else:
            print('Something went wrong. Make sure to choose correct sorting method again.')

        return sorted_numbers