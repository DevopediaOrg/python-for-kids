import itertools
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


allmarks = {
    'Kiran' : {
        'Maths' : 78,
        'Science' : 82,
        'Social': 87,
        'English': 52,
        'Hindi': 58,
        'Kannada': 62
    },
    'Kavita' : {
        'Maths' : 75,
        'Science' : 80,
        'Social': 87,
        'English': 68,
        'Hindi': 69,
        'Kannada': 78
    },
    'Ahmed' : {
        'Maths' : 70,
        'Science' : 88,
        'Social': 67,
        'English': 59,
        'Hindi': 78,
        'Kannada': 90
    }
}

mpl.style.use('seaborn')
plt.figure(figsize=(12, 9))
barwidth = 1 / (1 + len(allmarks))

# Draw the graph
for i, (student, marks) in enumerate(allmarks.items()):
    subjects = marks.keys()
    plt.bar(np.arange(len(subjects))+i*barwidth, tuple(marks.values()), width=barwidth, align='center', label=student)

# Add useful text to the graph
plt.ylabel('%')
plt.title('Marks by Subject')
plt.xticks(np.arange(len(subjects))+barwidth*(len(allmarks)/2), subjects)
plt.legend()

# Display the graph to user
plt.show()

