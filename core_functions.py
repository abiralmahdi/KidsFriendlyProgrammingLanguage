import random
import math
from statistics import mean, median, mode, stdev, NormalDist

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

def factorial(n):
    """Calculate the factorial of n."""
    return math.factorial(n)

def choose(n, r):
    """Calculate n choose r (combinations)."""
    return factorial(n) // (factorial(r) * factorial(n - r))

def permute(n, r):
    """Calculate n permute r (permuatations)."""
    return factorial(n) // factorial(n-r)
