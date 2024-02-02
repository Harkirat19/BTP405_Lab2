import matplotlib.pyplot as plt
import numpy as np

def graphSnowfall(file_path):
    with open('q2.txt', 'r') as file:
        snowfall_data = [int(line.strip()) for line in file]
    bins = [0, 11, 21, 31, 41, 51]
    counts, bins_edges = np.histogram(snowfall_data, bins=bins)

    # chart design
    plt.bar(bins_edges[:-1], counts, width=10, align='edge', color='red', edgecolor='black')
    
    # labels for chart
    plt.xlabel('Snowfall Range (in cms)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation Distribution')

    # Display the plot
    plt.show()

graphSnowfall('q2.txt')
