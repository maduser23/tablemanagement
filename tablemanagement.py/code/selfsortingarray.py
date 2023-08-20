import bisect
import pickle

class SelfSortingArray:
    def __init__(self):
        self.array = self.load_array()

    def load_array(self):
        try:
            with open("sorted_array.bin", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    def insert(self, value):
        bisect.insort(self.array, value)
        self.save_array()

    def save_array(self):
        with open("sorted_array.bin", "wb") as file:
            pickle.dump(self.array, file)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.array):
            element = self.array[self.index]
            self.index += 1
            return element
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.array[index]

    def __len__(self):
        return len(self.array)

    def print_array(self):
        print(self.array)

# Create an instance of SelfSortingArray





