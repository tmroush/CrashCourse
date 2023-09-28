sandwiches_ordered = ['rueben', 'pastrami', 'peanutbutter', 'pastrami', 'ham and cheese', 'grilled cheese', 'pastrami']
completed_sandwiches = []

print(sandwiches_ordered)
print("\nI am sorry, we are out of pastrami.")

while 'pastrami' in sandwiches_ordered:
    sandwiches_ordered.remove('pastrami')

while sandwiches_ordered:
    sandwich = sandwiches_ordered.pop()
    print(f"I am making your {sandwich} sandwich.")
    completed_sandwiches.append(sandwich)

print("The sandwiches I made are: ")
for s in completed_sandwiches:
    print(s)
