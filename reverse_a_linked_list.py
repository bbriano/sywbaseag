from linked_list import LinkedList

l = LinkedList(range(4))

print("Original:", l)

#         0 -> 1 -> 2 -> 3 -> None
# None <- 0 <- 1 <- 2 <- 3
p, c, = None, l.head
while c:
    t = c.next
    c.next = p
    p = c
    c = t
l.head = p

print("Reversed:", l)
