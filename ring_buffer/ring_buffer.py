from singly_linked_list import LinkedList 

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.element = 0
        self.storage = LinkedList()

    def append(self, item):
        pass
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        else:
            if self.element == None:
                self.element = self.storage.head

            self.element.value = item

            if self.element.next_node:
                self.element = self.element.get_next()
            else:
                self.element = self.storage.head
        

    def get(self):
        buffer = []

        item = self.storage.head

        while item != None:
            buffer.append(item.get_value())
            item = item.get_next()

        return buffer