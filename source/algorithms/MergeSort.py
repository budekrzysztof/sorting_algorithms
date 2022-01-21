class MergeSort:
    def merge_asc(self, new_nums: list, first_half_nums: list, second_half_nums: list):
        pos1, pos2 = 0, 0
        len1, len2 = len(first_half_nums), len(second_half_nums)

        while pos1 < len1 and pos2 < len2:
            if first_half_nums[pos1] < second_half_nums[pos2]:
                new_nums.append(first_half_nums[pos1])
                pos1 += 1
            else:
                new_nums.append(second_half_nums[pos2])
                pos2 += 1

        while pos1 < len1:
            new_nums.append(first_half_nums[pos1])
            pos1 += 1
        while pos2 < len2:
            new_nums.append(second_half_nums[pos2])
            pos2 += 1

    def sort_asc(self, nums: list):
        size = len(nums)
        if size <= 1:
            return []

        first_half_nums = []
        second_half_nums = []

        for i in range(0, size):
            if i < size / 2:
                first_half_nums.append(nums[i])
            else:
                second_half_nums.append(nums[i])

        self.sort_asc(first_half_nums)
        self.sort_asc(second_half_nums)
        nums.clear()
        self.merge_asc(nums, first_half_nums, second_half_nums)
        return nums

    def merge_desc(self, new_nums: list, first_half_nums: list, second_half_nums: list):
        pos1, pos2 = 0, 0
        len1, len2 = len(first_half_nums), len(second_half_nums)

        while pos1 < len1 and pos2 < len2:
            if first_half_nums[pos1] > second_half_nums[pos2]:
                new_nums.append(first_half_nums[pos1])
                pos1 += 1
            else:
                new_nums.append(second_half_nums[pos2])
                pos2 += 1

        while pos1 < len1:
            new_nums.append(first_half_nums[pos1])
            pos1 += 1
        while pos2 < len2:
            new_nums.append(second_half_nums[pos2])
            pos2 += 1

    def sort_desc(self, nums: list):
        size = len(nums)
        if size <= 1:
            return []

        first_half_nums = []
        second_half_nums = []

        for i in range(0, size):
            if i < size / 2:
                first_half_nums.append(nums[i])
            else:
                second_half_nums.append(nums[i])

        self.sort_desc(first_half_nums)
        self.sort_desc(second_half_nums)
        nums.clear()
        self.merge_desc(nums, first_half_nums, second_half_nums)
        return nums
