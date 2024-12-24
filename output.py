from core_functions import *
from visualizations import *

for i in range(1, 5 + 1):
    x = (i * 2)
    if (x > 5):
        print("x is greater than 5")
    break
title = "Sample Scatter Plot"
xlabel = "Time"
ylabel = "Value"
plot_scatter_plot([1, 2, 3, 4], [10, 20, 25, 30], title = "Sample Scatter Plot", xlabel = "Time", ylabel = "Value")