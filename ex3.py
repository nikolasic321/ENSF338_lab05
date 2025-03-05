import random
import timeit
import matplotlib.pyplot as plt

#Question 1 - Stack using python lists
class ArrayStack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.stack: #if array isn't empty, pop, else don't
            return self.stack.pop()
        return None

#Question 2 - stack using a singly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        return None

#Question 3 - ggenerate random lists of 10000 tasks (push probability=0.7, pop probablity=0.3)
def generate_tasks(n=10000):
    tasks = []
    for _ in range(n):
        if random.random() < 0.7:
            tasks.append(('push', random.randint(1, 100)))
        else:
            tasks.append(('pop', None))
    return tasks

#Question 4 - measure performance of both
def measure_performance(stack_class, task_lists):
    def execute_tasks(tasks):
        stack = stack_class()
        for task, value in tasks:
            if task == 'push':
                stack.push(value)
            else:
                stack.pop()
    
    return timeit.timeit(lambda: [execute_tasks(tasks) for tasks in task_lists], number=1)

task_lists = [generate_tasks() for _ in range(100)]

array_times = [measure_performance(ArrayStack, [tasks]) for tasks in task_lists]
linked_list_times = [measure_performance(LinkedListStack, [tasks]) for tasks in task_lists]

print("Array Stack Implementation Times: ", array_times)
print("Linked List Stack Implementation Times: ", linked_list_times)

#Questoin 5- plot results
plt.hist(array_times, bins=20, alpha=0.5, label='Array Stack')
plt.hist(linked_list_times, bins=20, alpha=0.5, label='Linked List Stack')
plt.xlabel('Execution Time (s)')
plt.ylabel('Frequency')
plt.legend()
plt.title('Performance Distribution of Stack Implementations')
plt.show()

#Array Stack has smaller distribution and smaller execution times.
#makes sense, pytohn lists already optimized for pop and append at the end

#Singly-linked-list has larger distribution and higher execution times
#makese sense, dynamic memory allocation for linked list nodes introduces overhead
