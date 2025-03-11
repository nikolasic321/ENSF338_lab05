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

#Question 2 - queue using a doubly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def dequeue(self):
        if not self.tail:
            return None
        value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
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
dll_times = [measure_performance(DoublyLinkedListQueue, [tasks]) for tasks in task_lists]

print("Array Stack Implementation Times: ", array_times)
print("Linked List Stack Implementation Times: ", dll_times)

#Questoin 5- plot results
plt.figure(figsize=(10, 6))
plt.hist(array_times, bins=30, alpha=0.5, label='Array Queue', edgecolor='black')
plt.hist(dll_times, bins=30, alpha=0.5, label='Doubly Linked List Queue', edgecolor='black')
plt.xlabel('Execution Time (s)')
plt.ylabel('Frequency')
plt.yscale('log')  #used a log scale to better see differences
plt.legend()
plt.title('Performance Distribution of Queue Implementations')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


#Array Queue has wider distribution of execution times, generally taking longer
#makes sense, inserting from head is an O(n) operation since all elements must be shifted, even though removing from tail is O(1)
#it doesn't makes up for it.

#Doubly Linked List Queue has a smaller distribution of execution times, generally taking less time since inserting at head is O(1)
#and removing from tail is O(1) as well (enqueues are O(1) and dequeues are O(1)) since we have pointers to both head and tail.
#there is also no need to shift elements around like in the array queue so its faster.
