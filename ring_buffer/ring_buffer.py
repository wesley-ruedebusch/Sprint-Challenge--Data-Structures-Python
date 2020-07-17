from singly_linked_list_copy import LinkedList
#^grabs the linked list class

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.element = None
        self.storage = LinkedList()

    def append(self, item):
        #check if the buffer is below capacity
        if self.storage.length < self.capacity:
            # add item to the end of the list
            self.storage.add_to_tail(item)
        # buffer is at capacity
        else:
            # set the current element to the head if it hasn't been yet
            if self.element == None:
                self.element = self.storage.head
            
            # reset the value of oldest item in buffer(the head)
            self.element.value = item

            # update pointers
            # check if at end of list
            if self.element.next_node:
                # reset our focus to the new oldest node
                self.element = self.element.get_next()
            # when at tail, bend the list into a ring
            else:
                self.element = self.storage.head

    def get(self):
        # RungBuffer().get returns a list
        buffer = []

        item = self.storage.head

        while item != None:
            buffer.append(item.get_value())
            item = item.get_next()
        
        return buffer