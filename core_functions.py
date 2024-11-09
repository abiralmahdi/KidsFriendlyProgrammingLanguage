import random

def draw_item(items):
    """Simulate drawing a random item from a list."""
    return random.choice(items)

def roll_dice(sides=6):
    """Simulate rolling a dice with a given number of sides (default 6)."""
    return random.randint(1, sides)

# Example Usage
print("Drawing an item:", draw_item(['apple', 'banana', 'cherry']))
print("Rolling a dice:", roll_dice())
