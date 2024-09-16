import numpy as np
import matplotlib.pyplot as plt

from hexpy.codeFromGPT4o import drawParallelLines

ROOT_3 = np.sqrt(3)
ROOT_3_DIV_2 = np.sqrt(3) / 2

def showPlt():
    plt.legend()
    plt.title('Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.tight_layout()
    plt.grid()
    plt.show()
    

def drawVerticalLineAtX(x):
    y = np.linspace(-10, 10, 100)
    x = np.full_like(y, x)
    plt.plot(x, y, label=f'Vertical line at x={x[0]}')


def drawParallelVerticalLines():
    for i in range(-5, 6):
        drawVerticalLineAtX(ROOT_3_DIV_2 + i * ROOT_3)

drawParallelVerticalLines()
showPlt()
