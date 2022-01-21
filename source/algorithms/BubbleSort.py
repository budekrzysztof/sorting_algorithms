class BubbleSort:
    def sort_asc(self, data):
        if len(data) < 1:
            return []
        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(data) - 1):
                if data[i] > data[i+1]:
                    sorted = False
                    data[i], data[i+1] = data[i+1], data[i]
        return data

    def sort_desc(self, data):
        if len(data) < 1:
            return []
        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(data) - 1):
                if data[i] < data[i+1]:
                    sorted = False
                    data[i], data[i+1] = data[i+1], data[i]
        return data