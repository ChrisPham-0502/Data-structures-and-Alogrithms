import array_queue as q
Q = q.ArrayQueue()
Q.enqueue(10)
Q.enqueue(10)
Q.enqueue(5)
Q.enqueue(5)
Q.enqueue(0)
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
