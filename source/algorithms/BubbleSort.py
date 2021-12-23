class BubbleSort:
    def Sort(self, data):
            sorted = False
            size = len(data) - 1

            while not sorted:
                sorted = True
                for i in range(size):
                    if data[i] > data[i+1]:
                        sorted = False
                        data[i], data[i+1] = data[i+1], data[i]

            return data