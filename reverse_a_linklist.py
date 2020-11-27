import unittest


class LinkedListNode:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __getitem__(self, index):
        self.__check_index_inbound(index)
        return self.__node_at_index(index).value

    def __setitem__(self, index, value):
        self.__check_index_inbound(index)
        self.__node_at_index(index).value = value

    def __len__(self):
        return self.length

    def __str__(self):
        return str(list(self))

    def append(self, value):
        new = LinkedListNode(value)
        if self.head is None:
            self.head = new
        last_node = self.__node_at_index(self.length-1)
        last_node.next = new
        self.length += 1

    def pop(self):
        if self.head is None:
            raise IndexError("index out of bounds")
        elif self.head.next is None:
            value = self.head.value
            self.head = None
        else:
            second_last = self.__node_at_index(self.length-2)
            value = second_last.next and second_last.next.value
            second_last.next = None
        self.length -= 1
        return value

    def reverse(self):
        p, c, = None, self.head
        while c:
            t = c.next
            c.next = p
            p = c
            c = t
        self.head = p

    def __check_index_inbound(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("index out of bounds")

    def __node_at_index(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current


class TestLinkedList(unittest.TestCase):
    def test_init(self):
        l = LinkedList()
        self.assertEqual(len(l), 0)

    def test_get(self):
        l = LinkedList()

    def test_set(self):
        l = LinkedList()

    def test_len(self):
        l = LinkedList()
        self.assertEqual(len(l), 0)
        l.append(1)
        self.assertEqual(len(l), 1)
        l.append(1)
        self.assertEqual(len(l), 2)
        l.pop()
        self.assertEqual(len(l), 1)
        l.pop()
        self.assertEqual(len(l), 0)

    def test_str(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        self.assertEqual(str(l), "[1, 2, 3, 4]")

    def test_iter(self):
        l = LinkedList()
        l.append(0)
        l.append(1)
        l.append(2)
        l.append(3)
        for i, n in enumerate(l):
            self.assertEqual(n, i)
        self.assertEqual(list(l), [0, 1, 2, 3])

    def test_append(self):
        l = LinkedList()
        l.append(1)
        self.assertEqual(len(l), 1)
        self.assertEqual(l[0], 1)

    def test_pop(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        self.assertEqual(l.pop(), 2)
        l.append(3)
        self.assertEqual(l.pop(), 3)
        self.assertEqual(l.pop(), 1)
        with self.assertRaises(IndexError):
            l.pop()

    def test_reverse(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.reverse()
        self.assertEqual(list(l), [4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
