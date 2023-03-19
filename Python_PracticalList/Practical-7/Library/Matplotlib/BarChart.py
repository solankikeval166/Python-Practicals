import matplotlib.pyplot as plt

plt.bar([0.25,2.25,3.25,5.25,7.25],[40,45,75,25,60],
label="city",color='orange',width=0.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[50,30,20,50,60],
label="growth", color='r',width=.5)
plt.legend()
plt.xlabel('Year')
plt.ylabel('Growth')
plt.title('Details')

# Print the chart
plt.show()



