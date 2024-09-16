import numpy as np
import matplotlib.pyplot as plt

def drawParallelLines():
    # Parameters for the hexagon grid
    hex_height = np.sqrt(3)  # Height of a regular hexagon side
    spacing = 2  # Distance between lines

    # Function to draw a line between two points
    def draw_line(x1, y1, x2, y2):
        x_values = np.linspace(x1, x2, 100)
        y_values = y1 + (y2 - y1) / (x2 - x1) * (x_values - x1)
        plt.plot(x_values, y_values)

    # Number of parallel lines
    num_lines = 5

    # Draw a series of parallel lines
    for i in range(num_lines):
        x1, y1 = 0, i * hex_height
        x2, y2 = 10, i * hex_height
        draw_line(x1, y1, x2, y2)

    # Configure plot display
    plt.gca().set_aspect('equal')
    plt.xlim(0, 10)
    plt.ylim(0, num_lines * hex_height)
    plt.title('Parallel Lines for Hexagon Geometry')
    plt.show()

def drawTestLine():
    plt.plot([0, 1], [0, 1], label='Line 1')
    plt.show()


def drawALine():
    x = np.linspace(-10, 10, 100)
    y = 2 * x + 1  # Example line equation: y = 2x + 1
    plt.plot(x, y, label='y = 2x + 1')
    plt.legend()
    plt.title('Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.show()
    