import matplotlib.pyplot as plt
import matplotlib as mpl

marks = {
    'Maths' : 78,
    'Science' : 82,
    'Social': 87,
    'English': 52,
    'Hindi': 58,
    'Kannada': 62
}

# Draw the graph
plt.bar(tuple(marks.keys()), tuple(marks.values()), align='center', color='#ff3d3d77')

# Add useful text to the graph
plt.ylabel('%')
plt.title('Marks by Subject')

# Save the graph in a file
plt.savefig('marks.png')

