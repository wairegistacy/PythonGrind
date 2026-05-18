# Traversing a Linked List to find the least value, delete a node, and insert a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # traverse a linked list
    def traverseAndPrint(head):
        currentNode = head

        while currentNode:
            print(currentNode.data, end = "->")
            currentNode = currentNode.next
        
        print("null")

    # Find the least value of the linked list
    def findLowestValue(head):
        minValue = head.data
        currentNode = head.next

        while currentNode:
            if currentNode.data < minValue:
                minValue = currentNode.data
            currentNode = currentNode.next
        
        return minValue
    
    # Delete a node in linked list
    def deleteSpecifiedNode(head, nodeToDelete):
        if head == nodeToDelete:
            return head.next
        
        currentNode = head

        while currentNode.next and currentNode.next != nodeToDelete:
            currentNode = currentNode.next

        if currentNode.next is None:
            return head
        
        currentNode.next = currentNode.next.next

        return head
    
    # Insert a new node to a specified position
    def insertNodeAtPosition(head, newNode, position):
        if position == 1:
            newNode.next = head
            return newNode
        
        currentNode = head

        for _ in range(position - 2):
            if currentNode.next is None:
                break
            currentNode = currentNode.next

        newNode.next = currentNode.next
        currentNode.next = newNode
        return head
    
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original Linked List: ")
Node.traverseAndPrint(node1)

print("\nLeast value of linked list: ", Node.findLowestValue(node1))

deleteNode = Node.deleteSpecifiedNode(node1, node4)
print("\nLinked List after deleting node:")
Node.traverseAndPrint(deleteNode)

newNode = Node(97)
insertNode = Node.insertNodeAtPosition(node1, newNode, 2)

print("\nAfter insertion:")
Node.traverseAndPrint(insertNode)
