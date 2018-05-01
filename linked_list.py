class Node:

    def __init__(self, item, link):
        self.item = item
        self.next = link
        
class LinkedListIterator:

    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            item = self.current.item
            self.current = self.current.next
            return item
   
class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def __len__(self):
        return self.count

    def __contains__(self, value):
        current = self.head
        while current is not None:
            if current.item == value:
                return True
            current = current.next
        return False

    def get_node(self, index):
        assert -len(self) <= index < len(self), "Index out of range"
        if index < 0:
            index += len(self)
        i = 0
        current = self.head
        while i < index:
            current = current.next
            i += 1
        return current

    def __getitem__(self, index):
        my_node = self.get_node(index)
        return my_node.item
    
    def __setitem__(self, index, value):
        my_node = self.get_node(index)
        my_node.item = value

    def get_index(self, value):
        current = self.head
        i = 0
        while current is not None:
            if current.item == value:
                return i
            i += 1
        raise ValueError
        

    def insert(self, item, index):
        assert -len(self) <= index < len(self), "Index out of range"
        if index == 0:
            self.head = Node(item, self.head)
        else:
            if index < 0:
                index += len(self)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = Node(item, current.next)
        self.count += 1

    def append(self, item):
        if self.head is None:
            self.head = Node(item, None)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(item, None)
        self.count += 1

    def shift(self):
        assert len(self) > 0, "Cannot shift from empty list"
        value = self.head.item
        self.head = self.head.next
        self.count -= 1
        return value
    
    def pop(self):
        assert len(self) > 0, "Cannot pop from empty list"
        if len(self) == 1:
            value = self.head.item
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            value = current.next.item
            current.next = None
        self.count -= 1
        return value
        
    def delete(self, index):
        assert -len(self) <= index < len(self), "Index out of range"
        assert len(self) > 0, "Cannot delete from empty list"
        if len(self) == 1:
            self.head = None
        elif index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.count -= 1

    def __str__(self):
        if self.head is None:
            return "[]"
        current = self.head
        my_string = "["
        while current.next is not None:
            my_string += str(current.item) + ", "
            current = current.next
        my_string += str(current.item) + "]"
        return my_string

    def __iter__(self):
        return LinkedListIterator(self.head)
    
    
        
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)
    my_list.insert(2, -1)
    my_list[2] = 10
    print(my_list[3])
    print(str(my_list))
    print([item for item in my_list if item < 10])



    
