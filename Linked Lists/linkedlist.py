class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def add(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def removeFromHead(self):
    if self.head is None:
      print("Linked list is empty.")
      return

    removed_value = self.head.value
    self.head = self.head.next

    return removed_value

  def isEmpty(self):
    return self.head is None

  def print_list(self):
    current_node = self.head
    if not current_node:
        print("Linked list is empty.")
        return

    elements = []
    while current_node:
        elements.append(str(current_node.value))
        current_node = current_node.next
    print(" -> ".join(elements))

  def length(self):
    current_node = self.head
    count = 0
    while current_node:
      count += 1
      current_node = current_node.next
    return count

  def addAtTail(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      return
    current_node = self.head
    while current_node.next:
      current_node = current_node.next
    current_node.next = new_node
  

  def find(self, value):
    current_value = self.head
    while current_value:
      if current_value.value == value:
        return True
      current_value = current_value.next
    return False
  
  def findMid(self):
    ahead = self.head
    while ahead and ahead.next:
      ahead = ahead.next.next
      self.head = self.head.next
    return self.head

  
  def reverse(self):
      new_list = None

      while self.head:
          next_node = self.head.next      
          self.head.next = new_list
          new_list = self.head
          self.head = next_node


      return new_list


linkedList = LinkedList()

linkedList.addAtTail(10)
linkedList.addAtTail(20)
linkedList.addAtTail(30)
linkedList.print_list()
print("Tamanho:", linkedList.length())

linkedList.add(5)
linkedList.print_list()

linkedList.removeFromHead()
linkedList.print_list()
print(linkedList.find(3))

print(linkedList.reverse().value)

print(linkedList.findMid())