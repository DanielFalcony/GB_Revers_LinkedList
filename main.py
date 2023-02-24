from Node import *
from Linked_List import *

print('Инициализация списка')
new_linked_list = DoubleLinkedList()
print('Заполенение списка')
new_linked_list.insert_in_emptylist(50)
new_linked_list.insert_at_start(8)
new_linked_list.insert_at_start(6)
new_linked_list.insert_at_start(13)
new_linked_list.insert_at_start(19)
new_linked_list.traverse_list()
print('Разворот списка')
new_linked_list.reverse_linked_list()
new_linked_list.traverse_list()
