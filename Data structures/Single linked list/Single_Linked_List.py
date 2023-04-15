import node


class Single_List_Array:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        if self._head is None:
            return True
        return False

    def remove_head(self):
        if self.is_empty():
            print('SLL is empty')
            return

        self._head = self._head._next

        if self.is_empty():
            self._tail = None

    def add_tail(self, new_data):
        new_item = node._Node(new_data, None)

        if self.is_empty():
            self._head = new_item
        else:
            self._tail._next = new_item

        self._tail = new_item

    def traversal(self):
        if self.is_empty():
            print('SLL is empty')
            return
        current = self._head
        while current is not None:
            print(current._data)
            current = current._next
