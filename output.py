from core_functions import *
from visualizations import *

calculate_mean([5, 3, 9, 3, 7, 8, 5, 3])
x = calculate_mean([5, 3, 9, 3, 7, 8, 5, 3])
calculate_median([2, 3, 4, 5])
y = calculate_median([2, 3, 4, 5])
plot_histogram([1, 2, 3, 4, 5])
plot_bar_chart(["A", "B", "C"], [10, 15, 7])
labels = ["Group A", "Group B"]
plot_box_plot([[7, 8, 5, 3], [6, 9, 3, 4]], labels)
title = "Sample Scatter Plot"
xlabel = "Time"
ylabel = "Value"
plot_scatter_plot([1, 2, 3, 4], [10, 20, 25, 30], title, xlabel, ylabel)
choose(8, 5)
a = choose(8, 5)
permute(7, 4)
b = permute(7, 4)
f = math.factorial(8)
abir = (4 + 33)