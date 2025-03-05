import random
import timeit
import matplotlib.pyplot as plt

#Question 1 - Queue using python lists
class ArrayQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.insert(0, value)  # Insert at head
    
    def dequeue(self):
        if self.queue:
            return self.queue.pop()  # Remove from tail
        return None

#Question 2 - queue using a singly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def dequeue(self):
        if not self.head:
            return None
        if self.head == self.tail:
            value = self.head.value
            self.head = self.tail = None
            return value
        
        current = self.head
        while current.next != self.tail:
            current = current.next
        
        value = self.tail.value
        self.tail = current
        self.tail.next = None
        return value


#Question 3 - ggenerate random lists of 10000 tasks (push probability=0.7, pop probablity=0.3)
def generate_tasks(n=10000):
    tasks = []
    for _ in range(n):
        if random.random() < 0.7:
            tasks.append(('enqueue', random.randint(1, 100)))
        else:
            tasks.append(('dequeue', None))
    return tasks

#Question 4 - measure performance of both
def measure_performance(queue_class, task_lists):
    def execute_tasks(tasks):
        queue = queue_class()
        for task, value in tasks:
            if task == 'enqueue':
                queue.enqueue(value)
            else:
                queue.dequeue()
    
    return timeit.timeit(lambda: [execute_tasks(tasks) for tasks in task_lists], number=1)


task_lists = [generate_tasks() for _ in range(100)]

array_times = [measure_performance(ArrayQueue, [tasks]) for tasks in task_lists]
linked_list_times = [measure_performance(LinkedListQueue, [tasks]) for tasks in task_lists]

print("Array Stack Implementation Times: ", array_times)
print("Linked List Stack Implementation Times: ", linked_list_times)

#Questoin 5- plot results
plt.figure(figsize=(10, 6))
plt.hist(array_times, bins=30, alpha=0.5, label='Array Queue', edgecolor='black')
plt.hist(linked_list_times, bins=30, alpha=0.5, label='Linked List Queue', edgecolor='black')
plt.xlabel('Execution Time (s)')
plt.ylabel('Frequency')
plt.yscale('log')  #using logarithmic scale to better distinguish
plt.legend()
plt.title('Performance Distribution of Queue Implementations')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


#Array Queue has very small distribution and small execution times.
#makes sense, inserting from head and popping from tail is generally efficient for small lists

#Singly-linked-list has larger distribution and higher execution times
#makese sense, linked lists require traversal to remove the tail element, leading to O(n) complexity for each dequeue() operation.