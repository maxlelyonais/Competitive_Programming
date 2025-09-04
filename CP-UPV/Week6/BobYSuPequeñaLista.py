
class Node:    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:

    def __init__(self):
        self.current = None
        self.aux = None
        self.head = Node("")
        self.selected = False

    def move_left(self):

        if self.current.prev:
            self.current = self.current.prev

        if not self.selected:
            self.aux = self.current

    def move_right(self):

        if self.selected and self.aux.next:
            self.aux = self.aux.next

        elif not self.selected and self.current.next:
            self.current = self.current.next
            self.aux = self.current

    def select(self):

        if self.selected:
            self.selected = False
            self.aux = self.current
        else:
            self.selected = True

    def insert(self, data):

        new_node = Node(data)

        if self.current == None:
            self.current = new_node
            self.aux = new_node
            self.head.next = new_node
            new_node.prev = self.head
        else:
            self.aux = self.aux.next
            new_node.next = self.aux

            if self.aux != None:
                self.aux.prev = new_node

            self.current.next = new_node   
            new_node.prev = self.current
            self.current = new_node
            self.aux = self.current

        self.selected = False


    def delete(self):

        if self.current == None:
            return
        
        if self.current == self.aux:

            if self.current.prev != self.head:
                self.current = self.current.prev
                self.aux = self.aux.next
                self.current.next = self.aux

                if self.aux != None:
                    self.aux.prev = self.current
            else:
                self.current = None
                self.aux = None

        elif self.selected:

            self.aux = self.aux.next
            self.current.next = self.aux

            if self.aux:
                self.aux.prev = self.current

        self.aux = self.current
        self.selected = False

    def begin(self):

        self.current = self.head

        if not self.selected:
            self.aux = self.head

    def end(self):

        while self.aux.next:
            self.aux = self.aux.next

        if not self.selected:
            self.current = self.aux


    def print(self):

        self.printer = self.head

        if self.current == None:
            print("|")
        else:
            element = ""

            while self.printer != None:
                element += self.printer.data
                if self.printer == self.current:
                    element+="|"
                self.printer = self.printer.next

            print(element)



if __name__ == "__main__":

    nQueries = int(input())
    doubleList = DoubleLinkedList()
    
    for _ in range(nQueries):

        action = input().split(" ")

        if action[0] == "PRINT":
            doubleList.print()
        elif action[0] == "INSERT":
            doubleList.insert(action[1])
        elif action[0] == "MOVE_LEFT":
            doubleList.move_left()
        elif action[0] == "MOVE_RIGHT":
            doubleList.move_right()
        elif action[0] == "DELETE":
            doubleList.delete()
        elif action[0] == "SELECT":
            doubleList.select()
        elif action[0] == "BEGIN":
            doubleList.begin()
        elif action[0] == "END":
            doubleList.end()
