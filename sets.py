##Ratical on sets: #Sets operation on Dataset in Python:
# Sample Dataset - List of Dictionaries
students_dataset = [
    {"name": "John", "age": 20, "grade": "A"},
    {"name": "Alice", "age": 22, "grade": "B"},
    {"name": "Bob", "age": 21, "grade": "C"},
    {"name": "Charlie", "age": 20, "grade": "A"},
    {"name": "David", "age": 23, "grade": "B"},
]

# a) Create Set
dataset_set = set(student["name"] for student in students_dataset)
print("Created Set:", dataset_set)

# b) Access Dataset items
print("\nAccessing Dataset items:")
for student in students_dataset:
    print(student)

# c) Add items in Dataset using add()
dataset_set.add("Eve")
print("\nAfter adding 'Eve' using add():", dataset_set)

# d) Add sets using update()
additional_set = {"Frank", "Grace"}
dataset_set.update(additional_set)
print("After updating with another set:", dataset_set)

# e) Remove items: remove() and discard()
dataset_set.remove("John")
print("\nAfter removing 'John' using remove():", dataset_set)

dataset_set.discard("Alice")  # Removes 'Alice' if present, does nothing otherwise
print("After discarding 'Alice' using discard():", dataset_set)

# f) Intersection
set1 = {"John", "Alice", "Bob"}
set2 = {"Bob", "Charlie", "David"}
intersection_result = set1.intersection(set2)
print("\nIntersection of sets:", intersection_result)

# g) Pop
popped_item = dataset_set.pop()
print(f"\nPopped item from the set: {popped_item}, Set after pop: {dataset_set}")

# h) Clear
dataset_set.clear()
print("\nSet after clear():", dataset_set)

# i) Union
set3 = {"John", "Alice", "Bob"}
set4 = {"Bob", "Charlie", "David"}
union_result = set3.union(set4)
print("\nUnion of sets:", union_result)

# j) Symmetric Difference Update
set5 = {"John", "Alice", "Bob"}
set6 = {"Bob", "Charlie", "David", "Eve"}
set5.symmetric_difference_update(set6)
print("\nSymmetric Difference Update:", set5)
