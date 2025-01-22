class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Time complexity: O(n)
    # Space complexity: O(1)
    def append(self, data):
        print('Appending', data)
        node = data if isinstance(data, Node) else Node(data)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
    
    def search(self, data):
        print('Searching for', data)
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False
    
    def delete(self, data):
        print('Deleting', data)
        curr = self.head
        if curr.data == data:
            self.head = curr.next
        else:
            while curr.next:
                if curr.next.data == data:
                    curr.next = curr.next.next
                    return
                curr = curr.next

    def __repr__(self) -> str:
        print('Printing linked list')
        curr = self.head
        res = []
        while curr:
            res.append(curr.data)
            curr = curr.next
        if len(res) == 0:
            return 'Empty linked list'
        return ' -> '.join(map(str, res))


if __name__ == '__main__':
    ll = LinkedList()
    print(ll)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    print(ll)
    print(ll.search(3))
    print(ll.search(6))
    ll.delete(3)
    print(ll)
    print(ll.search(3))
    ll.delete(1)
    print(ll)
    print(ll.search(1))