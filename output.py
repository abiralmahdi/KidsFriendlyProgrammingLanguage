from core_functions import *
from visualizations import *

title = "Values"
for i in range(1, 5 + 1):
    x = (i * 2)
    if (x > 5):
        plot_bar_chart([x, i], [x, i], title = "Values")