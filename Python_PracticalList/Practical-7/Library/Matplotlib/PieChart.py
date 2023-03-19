import matplotlib.pyplot as pyplot

slice = [12, 25, 50, 36, 19]
activities = [
    "DAA",
    "Operating System",
    "Computer Network",
    "System Design",
    "Machine Learning",
]
cols = ["pink", "yellow", "r", "green", "orange"]
pyplot.pie(
    slice,
    labels=activities,
    colors=cols,
    startangle=90,
    shadow=True,
    explode=(0, 0.1, 0, 0.1, 0),
    autopct="%1.1f%%",
)
pyplot.title("Training Subjects")

# Print the chart
pyplot.show()
