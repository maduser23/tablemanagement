import bisect
import json
from datetime import datetime, timedelta
from selfsortingarray import SelfSortingArray

ssa = SelfSortingArray()
lst=ssa
for i in lst:
    print(i)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value["time"] < node.value["time"]:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance_factor = self._get_balance_factor(node)

        if balance_factor > 1:
            if value["time"] < node.left.value["time"]:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance_factor < -1:
            if value["time"] > node.right.value["time"]:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _traverse_inorder(self, node, result):
        if node:
            self._traverse_inorder(node.left, result)
            result.append(node.value)
            self._traverse_inorder(node.right, result)

    def traverse_inorder(self):
        result = []
        self._traverse_inorder(self.root, result)
        return result

def check_availability(avl_tree, booking_time, duration):
    current_time = datetime.strptime(booking_time, "%H:%M")
    end_time = current_time + timedelta(hours=duration)

    bookings = avl_tree.traverse_inorder()

    for booking in bookings:
        start = datetime.strptime(booking["time"], "%H:%M")
        end = start + timedelta(hours=booking["duration"])

        if start <= current_time <= end or start <= end_time <= end:
            return False

    return True

def find_immediate_next_element(lst, value):
    index = bisect.bisect_right(lst, value)
    
    if index < len(lst) and lst[index] == value:
        return lst[index]
    elif index < len(lst):
        return lst[index-1]
    return None

def book_table(value, booking_time, duration):
    file_name = f"{value}.json"

    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            avl_tree = AVLTree()
            for item in data:
                avl_tree.insert(item)
    except FileNotFoundError:
        avl_tree = AVLTree()

    index = bisect.bisect_right(lst, value)
    if index >= len(lst):
        return "Not possible"

    next_element = lst[index]
    if not check_availability(avl_tree, booking_time, duration):
        result = book_table(next_element, booking_time, duration)
        return next_element

    new_booking = {"time": booking_time, "duration": duration}
    avl_tree.insert(new_booking)

    with open(file_name, "w") as file:
        json.dump(avl_tree.traverse_inorder(), file, indent=2)

    return '1'



