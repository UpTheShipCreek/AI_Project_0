import heapq

class PriorityQueue:

    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, task, priority):
        item = [priority, task]
        heapq.heappush(self.heap, item)
        self.count+=1
    
    def pop(self):
        self.count-=1
        return heapq.heappop(self.heap)
        

    def isEmpty(self):
        if(self.count == 0):
            return True
        else: return False

    def update(self, task, priority):
        for item in self.heap: 
            if task in item[1]:
                if item[0] > priority:
                    item[0] = priority

            
def  PQSort(int_list):
    pq = PriorityQueue()
    sorted_int_list = []
    for integer in int_list:
        pq.push(integer, integer) #Since Priority Queue works with two items, we fill it with the same integer for both the task and its priority
    while not pq.isEmpty():
        item = pq.pop()  #Likewise we only take one of the two in the list we return
        sorted_int_list.append(item[0])
    return sorted_int_list
  

    
# Main Method
if __name__ == '__main__':
    integer_list = [12,4,623,324,6,542,14,12,4] 
    print(PQSort(integer_list))