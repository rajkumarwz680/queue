class node:
    def init(self,data):
        self.data=data
        self.next=None
class queue:
    def init(self):
        self.rear=None
        self.front=None
    def enqueue(self,data):
        newnode=node(data)
        if self.rear==None and self.front==None:
            self.rear=newnode
            self.front=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
    def dequeue(self):
        if self.rear==None and self.front==None:
            print("Queue is empty")
        else:
            temp=self.front
            print(f"element: {self.front.data}")
            self.front=self.front.next
            del temp
            if self.front is None:
                self.rear=None
obj=queue()
while True:
    print("1.enqueue 2.dequeue 3.exit")
    choice=int(input("enter the choice"))
    if choice==1:
        data=int(input("enter the data"))
        obj.enqueue(data)
    elif choice==2:
        obj.dequeue()
    elif choice==3:
        break
    else:
        print("Invalid choice")






def filter(stack):
    primary_colors = ['Red', 'Green', 'Blue']
    queue = []  # Queue for removed boxes
    new_stack = []  # New stack for primary color boxes

    for box in stack:
        if box in primary_colors:
            new_stack.append(box)
        else:
            queue.append(box)

    return new_stack, queue

# Test the function with the given input
stack = ['Purple', 'White', 'Green', 'Orange', 'Red', 'Yellow', 'Magenta', 'Red']

new_stack, queue = filter(stack)

print("Boxes in the stack after modification:")
for box in new_stack:
    print(box)

print("\nBoxes in the queue:")
for box in queue:
    print(box)
