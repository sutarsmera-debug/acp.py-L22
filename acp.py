box_alex = {"apple", "banana", "popcorn", "juice"}
box_sam = {"popcorn", "cookie", "juice", "grapes"}

print(f"Alex's Snack Box: {box_alex}")
print(f"Sam's Snack Box: {box_sam}\n")

box_alex.add("pretzels")
print(f"Updated Alex's Box (added pretzels): {box_alex}\n")

shared_snacks = box_alex.intersection(box_sam)
print(f"Shared snacks between Alex and Sam: {shared_snacks}\n")

all_snacks = box_alex.union(box_sam)
print(f"All available unique snacks: {all_snacks}\n")

only_alex_snacks = box_alex.difference(box_sam)
print(f"Snacks only Alex has: {only_alex_snacks}")
