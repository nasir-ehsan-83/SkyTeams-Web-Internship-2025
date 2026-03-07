import unittest

from data_structure_algorithm.data_structure.week6.question1 import SinglyLinkedList
from data_structure_algorithm.data_structure.week6.question2 import SinglyLinkedListWithInsert
from data_structure_algorithm.data_structure.week6.question3 import SinglyLinkedList
from data_structure_algorithm.data_structure.week6.question4 import SinglyLinkedList
from data_structure_algorithm.data_structure.week6.question5 import SinglyLinkedList
from data_structure_algorithm.data_structure.week6.question6 import Queue
from data_structure_algorithm.data_structure.week6.question7 import Stack
from data_structure_algorithm.data_structure.week6.question8 import Stack
from data_structure_algorithm.data_structure.week6.question9 import isValid
from data_structure_algorithm.data_structure.week6.question10 import MinStack
from data_structure_algorithm.data_structure.week6.question11 import QueueTwoStacks
from data_structure_algorithm.data_structure.week6.question12 import evalRPN
from data_structure_algorithm.data_structure.week6.question13 import backspaceCompare
from data_structure_algorithm.data_structure.week6.question14 import removeAdjacent

class TestWeek1(unittest.TestCase):
    def test_linked_list_creation(self):
        ll = SinglyLinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        self.assertEqual(ll.to_list(), [10,20,30])

    def test_insert_beginning(self):
        sll = SinglyLinkedListWithInsert()
        sll.append(10)
        sll.append(20)
        sll.append(30)
        sll.insert_at_beginning(5)
        self.assertEqual(sll.to_list(), [5, 10, 20, 30])
  
    def test_append(self):
        sll = SinglyLinkedList()
        sll.append(10)
        sll.append(20)
        sll.append(30)
        self.assertEqual(sll.to_list(), [10, 20, 30])
        
        # Test appending to an existing list
        sll.append(40)
        self.assertEqual(sll.to_list(), [10, 20, 30, 40])

    def test_delete_first(self):
        ll = SinglyLinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        ll.delete_first()
        self.assertEqual(ll.to_list(), [20,30])

    def test_search(self):
        ll = SinglyLinkedList()
        ll.append(10)
        ll.append(20)
        self.assertTrue(ll.search(20))
        self.assertFalse(ll.search(30))

    def test_queue_operations(self):
        q = Queue()
        self.assertTrue(q.isEmpty())
        q.enqueue(10)
        q.enqueue(20)
        q.enqueue(30)
        self.assertEqual(q.to_list(), [10,20,30])
        self.assertEqual(q.dequeue(), 10)
        self.assertEqual(q.to_list(), [20,30])
        self.assertEqual(q.front(), 20)
        self.assertEqual(q.rear(), 30)

    def test_stack_operations(self):
        s = Stack()
        self.assertTrue(s.isEmpty())
        s.push(10)
        s.push(20)
        s.push(30)
        self.assertEqual(s.to_list(), [10,20,30])
        self.assertEqual(s.pop(), 30)
        self.assertEqual(s.top(), 20)
        self.assertFalse(s.isEmpty())
        self.assertEqual(s.size(), 2)

    def test_reverse_stack(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.reverse()
        self.assertEqual(s.to_list(), [3,2,1])

    def test_valid(self):
        self.assertTrue(isValid("()[]{}"))
        self.assertFalse(isValid("(]"))
        self.assertFalse(isValid("([)]"))
        self.assertTrue(isValid("{[]}"))

    def test_min_stack(self):
        s = MinStack()
        s.push(5)
        s.push(3)
        s.push(7)
        self.assertEqual(s.getMin(), 3)
        s.pop()
        self.assertEqual(s.getMin(), 3)
        s.pop()
        self.assertEqual(s.getMin(), 5)

    def test_queue_two_stacks(self):
        q = QueueTwoStacks()
        self.assertTrue(q.empty())
        q.push(10)
        q.push(20)
        self.assertFalse(q.empty())
        self.assertEqual(q.peek(), 10)
        self.assertEqual(q.pop(), 10)
        self.assertEqual(q.peek(), 20)

    def test_rpn(self):
        self.assertEqual(evalRPN(["2","1","+","3","*"]), 9)
        self.assertEqual(evalRPN(["4","13","5","/","+"]), 6)
        self.assertEqual(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)

    def test_backspace(self):
        self.assertTrue(backspaceCompare("ab#c", "ad#c"))
        self.assertTrue(backspaceCompare("a##c", "#a#c"))
        self.assertFalse(backspaceCompare("a#c", "b"))

    def test_remove_adjacent(self):
        self.assertEqual(removeAdjacent("abbaca"), "ca")
        self.assertEqual(removeAdjacent("aabbcc"), "")
        self.assertEqual(removeAdjacent("abc"), "abc")


if __name__ == "__main__":
	unittest.main()