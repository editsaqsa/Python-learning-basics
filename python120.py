# Walrus operator in python
numbers = [10, 25, 40, 5]
if (count := len(numbers)) >3:
    print(f"list has {count} items (more than 3)")


entries = [ ]
while (item := input("Add a topic\ item (or type 'stop'):").strip()) = "stop":
   if item:
       entries.append(item)
       print(f"Added: {item}")
       print("\nCollected items:", entries)
       