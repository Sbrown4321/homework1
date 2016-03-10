#Steven Brown
#assignment_1
import unittest

class linked_list:
    #iterator
    front = rear = None
    current = None

    class node:
        #Function for reference next in list
        def __init__(self, item, next):
                self.item = item #contains the data
                self.next = next #reference to next node
        #Funtion to convert to string
        def __str__(self):
            return str(self.item)

    def empty(self):
        #return len(self.item) == 0
        return not self.front
    #Appened function to add item to front of list
    def push_front(self, item):
        x = self.node(item, self.front)
        self.front = x
        if not self.rear:
            self.rear = x
    #Appeand function to add item to end of list
    def push_back(self, item):
        if self.empty():
            self.front = self.rear = self.node(item, None)
        else:
            x = self.node(item, None)
            self.rear.next = x
            self.rear = x
    #Function to remove item from front of list
    def pop_front(self):
        if self.empty():
            raise RuntimeError("The list is empty")
        x = self.front.item
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return x
    #Function to remove item from rear of list
    def pop_back(self):
        if self.empty():
            raise RuntimeError("The list is empty")
        y = self.rear.item
        if not self.front.next:
            self.front = self.rear = None
        else:
            x = self.front
            while x.next is not self.rear:
                x = x.next
            x.next = None
            self.rear = x
        return y

class factorial:
    def fact(self, a):
        if a < 0: raise ValueError("Less than zero")
        if a == 0 or a == 1: return 1

        stack = linked_list()
        while a > 1:
            stack.push_front(a)
            a -= 1

        result = 1
        while not stack.empty():
            result *= stack.pop_front()

        return result

class test_linked_list (unittest.TestCase):
    def test_none(self):
        self.assertTrue(linked_list().empty())
    def test_pop_front_empty(self):
        self.assertRaises(RuntimeError, lambda: linked_list().pop_front())
    def test_pop_back_empty(self):
        self.assertRaises(RuntimeError, lambda: linked_list().pop_back())
    def test_push_back_pop_front(self):
        ll = linked_list()
        ll.push_back(1)
        ll.push_back(2)
        ll.push_back(3)
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_front(), 1)
        self.assertEquals(ll.pop_front(), 2)
        self.assertEquals(ll.pop_front(), 3)
        self.assertTrue(ll.empty())
    def test_push_front_pop_front(self):
        ll = linked_list()
        ll.push_front(1)
        ll.push_front(2)
        ll.push_front(3)
        self.assertEquals(ll.pop_front(), 3)
        self.assertEquals(ll.pop_front(), 2)
        self.assertEquals(ll.pop_front(), 1)
        self.assertTrue(ll.empty())
    def test_push_front_pop_back(self):
        ll = linked_list()
        ll.push_front(1)
        ll.push_front(2)
        ll.push_front(3)
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_back(), 1)
        self.assertEquals(ll.pop_back(), 2)
        self.assertEquals(ll.pop_back(), 3)
        self.assertTrue(ll.empty())
    def test_push_back_pop_back(self):
        ll = linked_list()
        ll.push_back(1)
        ll.push_back("foo")
        ll.push_back([3,2,1])
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_back(),[3,2,1])
        self.assertEquals(ll.pop_back(), "foo")
        self.assertEquals(ll.pop_back(), 1)
        self.assertTrue(ll.empty())

print (factorial().fact(1))
print (factorial().fact(2))
print (factorial().fact(100))