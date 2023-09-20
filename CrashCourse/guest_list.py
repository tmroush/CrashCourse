# These are exercises 3-4, 3-5, 3-6, and 3-7 from Python Crash Course

guest_list = ["Hester", "John", "Rex", "Carol"]
invite = ", you are invited to dinner"
print(guest_list[0] + invite)
print(guest_list[1] + invite)
print(guest_list[2] + invite)
print(guest_list[3] + invite)

print("\n" + guest_list[0] + " can't make it")

del guest_list[0]
guest_list.insert(0, "Mike")
guest_list.insert(2, "Laurel")
guest_list.append("Rodney")

print(guest_list)
print(guest_list[0] + invite)
print(guest_list[1] + invite)
print(guest_list[2] + invite)
print(guest_list[3] + invite)
print(guest_list[4] + invite)
print(guest_list[5] + invite)

print("\nSorry. We only have room for 2!")

print(guest_list.pop() + ", we don't have room for you.")
print(guest_list.pop() + ", we don't have room for you.")
print(guest_list.pop() + ", we don't have room for you.")
print(guest_list.pop() + ", we don't have room for you.")

invite_2 = ", you are still invited"
print(guest_list[0] + invite_2)
print(guest_list[1] + invite_2)

del guest_list[1]
del guest_list[0]

print(guest_list)
