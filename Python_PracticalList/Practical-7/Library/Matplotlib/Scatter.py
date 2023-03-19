import matplotlib.pyplot as pyplot

x1 = [1, 2, 3, 4, 5, 6, 7]
y1 = [1, 2, 3, 4, 5, 6, 7]
x2 = [1.6,2.2,3.4,5.8]
y2 = [1.8,2.1,3.3,5.6]

pyplot.scatter(x1, y1, label="City", color="c")
pyplot.scatter(x2, y2, label="Growth", color="g")
pyplot.title("Smart Band Data Report")
pyplot.xlabel("x")
pyplot.ylabel("y")
pyplot.legend()

# Print the chart
pyplot.show()
