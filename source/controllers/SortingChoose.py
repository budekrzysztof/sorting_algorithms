from algorithms.MergeSort import MergeSort
from algorithms.BubbleSort import BubbleSort

class SortingChoose:
    def choose_method(self, data: list, sorting_method: str, sorting_order: str) -> list:
        sorted_numbers = []

        if sorting_method == 'merge':
            if sorting_order == 'asc':
                sorted_numbers = MergeSort().Sort(data)
            elif sorting_order == 'desc':
                sorted_numbers = MergeSort().Sort(data)
                sorted_numbers.reverse()
            else:
                print('Something went wrong. Make sure to input correct sorting order again.')
        elif sorting_method == 'bubble':
            if sorting_order == 'asc':
                sorted_numbers = BubbleSort().Sort(data)
            elif sorting_order == 'desc':
                sorted_numbers = BubbleSort().Sort(data)
                sorted_numbers.reverse()
            else:
                print('Something went wrong. Make sure to input correct sorting order again again.')
        else:
            print('Something went wrong. Make sure to choose correct sorting method again.')

        return sorted_numbers