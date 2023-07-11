class Nodes:
    def __init__ (self, data):
        self.data = data
        self.next = None
        
        #self.a = None
        #self.b = None
        
class list1:
    def __init__(self, a):
        self.a = a
        
        
    
        
class list2:
    def __init__(self, b):
        self.b = b
       
        
def intersecting_node(a, b):
    ptr1 = a.a
    ptr2 = b.b

    while ptr1 != ptr2:
        if ptr1 == None:
            ptr1 = b.b
        else:
            ptr1 = ptr1.next

        if ptr2 == None:
            ptr2 = a.a
        else:
            ptr2 = ptr2.next

    return ptr1
    
    

# Create the Nodes for list1
node1 = Nodes(3)
node2 = Nodes(7)
node3 = Nodes(8)
node4 = Nodes(10)

# Create the Nodes for list2
node5 = Nodes(99)
node6 = Nodes(1)
node7 = Nodes(8)
node8 = Nodes(10)

# Create the list1 and list2 instances with Nodes as arguments
# create the list1 and list2 instances
l1 = list1(node1)
node1.next = node2
node2.next = node3
node3.next = node4

l2 = list2(node5)
node5.next = node6
node6.next = node7
node7.next = node8

# Test the intersecting_node function
intersection = intersecting_node(l1, l2)
if intersection is not None:
    print("The two lists intersect at node with data:", intersection.data)
else:
    print("The two lists do not intersect.")
