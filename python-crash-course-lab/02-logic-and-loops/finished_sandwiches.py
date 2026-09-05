sandwich_orders = ['pastrami', 'bocadillo', 'bokit', 'pastrami', 'wurstbrot', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich.title()} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll finished sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())