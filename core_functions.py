import random
from statistics import mean, median, mode, stdev

def calculate_mean(values):
    return mean(values)

def calculate_median(values):
    return median(values)

def calculate_mode(values):
    return mode(values)

def calculate_stdev(values):
    return stdev(values)

def draw_item(items):
    """Simulate drawing a random item from a list."""
    return random.choice(items)

def roll_dice(sides=6):
    """Simulate rolling a dice with a given number of sides (default 6)."""
    return random.randint(1, sides)
