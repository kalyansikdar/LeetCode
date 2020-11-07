class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(None)
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        count = 0

        while index:
            curr = curr.next
            index -= 1

        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will
        not be inserted.
        """
        if index < 0 or index > self.size:
            return -1

        curr = self.head
        new_node = ListNode(val)

        if index == 0:
            new_node.next = curr
            self.head = new_node
        else:
            while index - 1:
                curr = curr.next
                index -= 1
            temp = curr.next
            curr.next = new_node
            new_node.next = temp

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        if index == 0:
            self.head = self.head.next
        else:
            while index-1:
                curr = curr.next
                index -= 1
            curr.next = curr.next.next

        self.size -= 1

    def __repr__(self):
        curr = self.head
        result = ""
        while curr:
            result += str(curr.val) + " "
            curr = curr.next

        return result


# Your MyLinkedList object will be instantiated and called as such:
ll = MyLinkedList()
# Test Case # 1
# ll.addAtHead(1)
# print(ll)
# ll.addAtTail(3)
# print(ll)
# ll.addAtIndex(1,2)
# print(ll)
# print(ll.get(1))
# ll.deleteAtIndex(1)
# print(ll)
# print(ll.get(1))
####    Test Case # 2  ####
# ll.addAtHead(1)
# print(ll)
# ll.addAtTail(3)
# print(ll)
# ll.addAtIndex(1,2)
# print(ll)
# print(ll.get(1))
# ll.deleteAtIndex(0)
# print(ll)
# print(ll.get(0))
# Test Case # 3
# ll.addAtHead(1)
# print(ll)
# ll.deleteAtIndex(0)
# print(ll)
### Test case 4 ###
ll.addAtHead(7)
print(ll)
ll.addAtHead(2)
print(ll)
ll.addAtHead(1)
print(ll)
ll.addAtIndex(3, 0)
print(ll)
ll.deleteAtIndex(2)
print(ll)
ll.addAtHead(6)
print(ll)
ll.addAtTail(4)
print(ll)
ll.get(4)
ll.addAtHead(4)
print(ll)
ll.addAtIndex(5, 0)
print(ll)
ll.addAtHead(6)
print(ll)