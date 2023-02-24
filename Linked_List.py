from Node import *

class DoubleLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print('Список не пустой')

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print('Узел вставлен')
            return
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.pref = n

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print('Список пустой')
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.next
            if n is None:
                print('Объект не в списке')
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.next = n.next
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print('Список пустой')
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.next
            if n is None:
                print('Объект не в списке')
            else:
                new_node = Node(data)
                new_node.next = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref = new_node

    def traverse_list(self):
        if self.start_node is None:
            print('В списке нет элементов')
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, ' ')
                n = n.next

    def delete_at_start(self):
        if self.start_node is None:
            print('В списке нет элементов для удаления')
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None

    def delete_at_end(self):
        if self.start_node is None:
            print("В списке нет элементов для удаления")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.pref.next = None

    def delete_item_by_value(self, x):
        if self.start_node is None:
            print('В списке нет элементов для удаления')
            return
        if self.start_node.next is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print('Объект не найден')
                return
        if self.start_node.item == x:
            self.start_node = self.start_node.next
            self.start_node.pref = None
            return
        n = self.start_node
        while n.next is not None:
            if n.item == x:
                break
            n = n.next
        if n.next is not None:
            n.pref.next = n.next
            n.next.pref = n.pref
        else:
            if n.item == x:
                n.pref.next = None
            else:
                print('Элемент не найден')
        if self.start_node is None:
            print('В списке нет элементов для удаления')
            return
        if self.start_node.next is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print('Объект не найден')
            return
        if self.start_node.item == x:
            self.start_node = self.start_node.next
            self.start_node.pref = None
            return
        n = self.start_node
        while n.next is not None:
            if n.item == x:
                break
            n = n.next
        if n.next is not None:
            n.pref.next = n.next
            n.next.pref = n.pref
        else:
            if n.item == x:
                n.pref.next = None
            else:
                print('Объект не найден')

    def reverse_linked_list(self):
        if self.start_node is None:
            print('В списке нет элементов для удаления')
            return
        p = self.start_node
        q = p.next
        p.next = None
        p.pref = q
        while q is not None:
            q.pref = q.next
            q.next = p
            p = q
            q = q.pref
        self.start_node = p