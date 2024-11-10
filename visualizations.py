import matplotlib.pyplot as plt

def plot_histogram(data, title="Histogram"):
    plt.hist(data, bins=10, edgecolor='black')
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

def plot_bar_chart(categories, counts, title="Bar Chart"):
    plt.bar(categories, counts, color='skyblue')
    plt.title(title)
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.show()

def plot_pie_chart(categories, counts, title="Pie Chart"):
    plt.pie(counts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.show()

# # Example Usage
# plot_pie_chart(['A', 'B', 'C'], [10, 15, 7], title="Sample Pie Chart")


# # Example Usage
# data = [5, 3, 9, 3, 7, 8, 5, 3]
# plot_histogram(data, title="Sample Histogram")
# plot_bar_chart(['A', 'B', 'C'], [10, 15, 7], title="Sample Bar Chart")
