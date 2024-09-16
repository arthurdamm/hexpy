#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from hexpy.codeFromGPT4o import drawParallelLines

ROOT_3 = np.sqrt(3)
ROOT_3_DIV_2 = np.sqrt(3) / 2
HexRadius = 2
AxisScalar = 5

def showPlt():
    plt.legend()
    plt.title('Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    # plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    # plt.tight_layout()
    # plt.grid()
    plt.xlim(-AxisScalar * HexRadius, AxisScalar * HexRadius)
    plt.ylim(-AxisScalar * HexRadius, AxisScalar * HexRadius)
    plt.gca().set_aspect('equal')
    plt.show()
    
def drawLine(m, b, color=None):
    """Draw a line given slope m and intercept b."""
    x = np.linspace(-10, 10, 100)
    y = m * x + b
    label=f'y = {m}x + {b}'
    plt.plot(x, y, color=color)

def drawVerticalLineAtX(x, color=None):
    y = np.linspace(-10, 10, 100)
    x = np.full_like(y, x)
    label = f'Vertical line at x={x[0]}'
    plt.plot(x, y, label="", color=color)

def drawAxes():
    drawVerticalLineAtX(0, 'black')
    drawLine(0,0, 'black')

def drawParallelVerticalLines():
    for i in range(-5, 6):
        drawVerticalLineAtX(i * ROOT_3_DIV_2 * HexRadius, 'green')

def drawParallelDownwardLines():
    m = -1 / ROOT_3
    b = 0
    distanceBetweenParrallelLines = HexRadius
    for i in range(-5, 5):
        drawLine(m, b + i * distanceBetweenParrallelLines, 'red')

def drawParallelUpwardsLines():
    m = 1 / ROOT_3
    b = 0
    distanceBetweenParrallelLines = HexRadius
    for i in range(-5, 5):
        drawLine(m, b + i * distanceBetweenParrallelLines, 'blue')

def getHexagonVertices():
    angles = np.linspace(0, 2 * np.pi, 7)[:-1]  # 6 vertices
    x = HexRadius * np.sin(angles)
    y = HexRadius * np.cos(angles)
    return x, y

def getHexagonVerticesHardcoded():
    x = [0, ROOT_3_DIV_2, ROOT_3_DIV_2, 0, -ROOT_3_DIV_2, -ROOT_3_DIV_2]
    y = [1, 0.5, -0.5, -1, -0.5, 0.5]
    xScaled = [i * HexRadius for i in x]
    yScaled = [i * HexRadius for i in y]
    return xScaled, yScaled

def drawHexagon():
    x, y = getHexagonVertices()
    plt.fill(x, y, 'yellow', alpha=0.5)
    x, y = getHexagonVerticesHardcoded()
    plt.fill(x, y, 'cyan', alpha=0.5)

drawParallelVerticalLines()
drawParallelDownwardLines()
drawParallelUpwardsLines()
drawAxes()
drawHexagon()
showPlt()
