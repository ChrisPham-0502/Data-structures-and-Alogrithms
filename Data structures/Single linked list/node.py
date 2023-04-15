class _Node:
    def __init__(self, data, next_item):
        self._data = data
        self._next = next_item

    def display(self):
        print(self._data)
        print(self._next)
