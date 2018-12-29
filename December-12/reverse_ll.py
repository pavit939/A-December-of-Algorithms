class node:
  def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def rev(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def print(self):
        temp = self.head
        while (temp):
            print(temp.data,"-->",end=" ")
            temp = temp.next
def main():
  ll = linkedlist()
  num=int(input("Enter number of Nodes:"))
  for i in range(0,num):
      node=int(input("Enter Node:"))
      ll.push(node)
  print("\nThe given Linked List:\n")
  ll.print()
  ll.rev()
  print("\nReversed Linked List:\n")
  ll.print()
main()
