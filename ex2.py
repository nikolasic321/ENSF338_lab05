import timeit
import random

class PriorityQueue1:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        self.queue = self.mergesort(self.queue) 

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def mergesort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.mergesort(arr[:mid])
        right = self.mergesort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]: 
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def __str__(self):
        return str(self.queue)


class PriorityQueue2:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Inserts an item into the queue at the correct position."""
        if not self.queue or item >= self.queue[-1]:  
            self.queue.append(item)
        else:
            i = len(self.queue) - 1
            while i >= 0 and self.queue[i] > item:
                i -= 1
            self.queue.insert(i + 1, item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)


def generate_tasks(priorityQueueClass):
    queue = priorityQueueClass()

    for _ in range(1000):
        if random.random() < 0.7:  # 70% probability for 'push'
            queue.enqueue(random.randint(0,1000))
        else:  # 30% probability for 'pop'
            queue.dequeue()
    return queue


merge_queue_times = timeit.timeit(lambda: generate_tasks(PriorityQueue1), number = 100)
insertion_queue_times = timeit.timeit(lambda: generate_tasks(PriorityQueue2), number = 100)

print(merge_queue_times)
print(insertion_queue_times)


'''
5. 
The second implementation using insertion sort is faster. When using merge_sort to enqueue the list,
it first has to append the element to the array, which has the worst case time complexity of O(n).
Then it calls merge_sort after every insertion, which has the time complexity of O(nlogn). In total,
each insertion will have the time complexity of O(n) + O(nlogn)

In the second implementation, inserting the element into the correct position so that the array is
sorted has the total time complexity of O(n), since it does not have to sort again after insertion.
'''
    


