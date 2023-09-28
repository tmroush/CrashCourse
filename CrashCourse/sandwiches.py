def make_sandwich(bread_type, *sandwich_items):
    """Build a sandwich on the type of bread"""
    print(f"\nBuilding a sandwich on {bread_type} bread:")
    for item in sandwich_items:
        print(f"Adding {item} to your sandwich.")


make_sandwich('wheat', 'peanut butter', 'jelly')
make_sandwich('rye', 'ham', 'swiss cheese', 'bacon', 'tomato', 'lettuce')
make_sandwich('white', 'turkey', 'cheddar cheese', 'guacamole', 'lettuce')
