class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while(start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head: Node) -> Node:
        # Write your code here
        unique_node_list = {}
        new_node = Node
        if not head:
            return None

        prev_node = head
        current_node = head
        while current_node:
            if current_node.data in unique_node_list.keys():

                prev_node.next = current_node.next

            else:
                print("true", unique_node_list)
                unique_node_list[current_node.data] = True
                current_node = current_node.next

        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
