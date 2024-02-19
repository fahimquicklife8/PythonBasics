import heapq

minHeap = []
heapq.heappush(minHeap,3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)
#min in always at index 0
print(minHeap[0])



maxHeap = []

heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -6)
heapq.heappush(maxHeap, -4)
heapq.heappush(maxHeap, -3)

print(-1*heapq.heappop(maxHeap))

while len(maxHeap):
    print(-1*heapq.heappop(maxHeap))





