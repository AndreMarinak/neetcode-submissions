class ListNode:

    def __init__(self,val=0,key=0):
        self.val=val
        self.key=key
        self.next=None
        self.prev=None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity #sets capacity for Cache
        self.d={} #sets cache dict where will store key,node pairs
        self.head=ListNode()
        self.tail=ListNode() #Dummy heads and tails
        self.head.next=self.tail
        self.tail.prev=self.head
    def remove(self,node): #remove, return key/node
        node.prev.next=node.next
        node.next.prev=node.prev
        return (node)
    def add(self,node): #add to front
        node.next=self.head.next  #node ---> 5, head <--> 5
        self.head.next=node #head ---> node ---> 5
        node.prev=self.head # head <---> node --> 5
        node.next.prev = node  # head <---> node <--> 5
    def add_to_front(self,node): #remove then add
        node.prev.next=node.next
        node.next.prev=node.prev
        self.add(node)



    def get(self, key: int) -> int:
        if key in self.d:
            self.add_to_front(self.d[key])
            return self.d[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d: #If exsists
            self.add_to_front(self.d[key]) #put node at front
            self.d[key].val=value #update value
            return
        if len(self.d) == self.capacity: #always check if full remove node, remove from dict
            temp=self.remove(self.tail.prev)
            del self.d[temp.key]
        #If new:
        new_node=ListNode(value,key)
        self.add(new_node)
        self.d[key]=new_node


