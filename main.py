#main.py
#
#Author:        Farjad Tariq
#Version:       2023/08/20
#
#Purpose:       The purpose of this question is calculating the approximate
#               area of an ellipse using Simpson's rule with three different
#               techniques.
#                   1. lists
#                   2. arrays
#                   3. arrays with vector arithmetic
#               Furthermore, a simple analysis is performed to detrmine the
#               the trade-offs between different data structures (lists vs. arrays)
#               and the advantages of using vector arithmetic for numerical computations.


from time import ctime
from math import sqrt, pi
import numpy as np
import timeit


def displayTerminationMessage():
    print(f"""
Programmed by Farjad Tariq
Date: {ctime()}
End of processing.\n""")

def getPositiveNumber(prompt, EOF):
    while True:
        value = input(prompt).strip()
        if value != '':
            try:
                value = eval(value, {}, {})
                if isinstance(value, (int, float)):
                    if value < 0:
                        print(f"{value} is less than 0!")
                    elif value == 0:
                        return EOF
                    else:
                        return value
                else:
                    print(f"{value} is not a number")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print('Missing input!')


# Part 1: Lists
# -------------------------------------------------------------------------------------
def list_computeXCoordinates(a, intervals):
    #a = length of the semi-major axis
    #intervals = the number of intervals 
    #i = index variable used for going through the loop
    
    return [i * (a / intervals) for i in range(intervals + 1)]


def list_ellipse(a, b, xValues):
    #xValues = the list of xCoordinates
    #a = length of the semi-major axis
    #b = length of the semi-minor axis
    #x = index variable for values of xCoordinates
    
    return [b * sqrt(1 - (x / a) ** 2) for x in xValues]


def list_computeArea(a, b, intervals):
    #xValues = list of xCoordinates
    #yCoords = list of y coordinates
    #a = length of the semi-major axis
    #b = length of the semi-minor axis
    #intervals = the number of intervals 
    #i = index variable
    #h = a / intervals
    #firstSum = first summation of the simpsons rule
    #secondSum = second summation of the simpsons rule
    #approxArea = approximate area of ellipse using simpsons rule
    
    xValues = list_computeXCoordinates(a, intervals)
    yCoords = list_ellipse(a, b, xValues)
    h = a / intervals
    firstSum = sum(yCoords[1:-1:2])
    secondSum = sum(yCoords[2:-2:2])
    approxArea = h / 3. * (yCoords[0] + 4 * firstSum + 2 * secondSum + yCoords[-1]) * 4
    return approxArea, pi * a * b


# Part 2: Arrays
# -------------------------------------------------------------------------------------
def array_computeXCoordinates(a, intervals):
    #a = length of the semi-major axis
    #intervals = the number of intervals 
    #i = index variable used for going through the loop
    
    return np.array([i * (a / intervals) for i in range(intervals + 1)])


def array_ellipse(a, b, xValues):
    #xValues = the list of xCoordinates
    #a = length of the semi-major axis
    #b = length of the semi-minor axis
    #x = index variable for values of xCoordinates
    
    return np.array([b * sqrt(1 - (x / a) ** 2) for x in xValues])


def array_computeArea(a, b, intervals):
    #xValues = list of xCoordinates
    #yCoords = list of y coordinates
    #a = length of the semi-major axis
    #b = length of the semi-minor axis
    #intervals = the number of intervals 
    #i = index variable
    #h = a / intervals
    #firstSum = first summation of the simpsons rule
    #secondSum = second summation of the simpsons rule
    #approxArea = approximate area of ellipse using simpsons rule
    
    xValues = array_computeXCoordinates(a, intervals)
    yCoords = array_ellipse(a, b, xValues)
    h = a / intervals
    firstSum = np.sum(yCoords[1:-1:2])
    secondSum = np.sum(yCoords[2:-2:2])
    approxArea = h / 3. * (yCoords[0] + 4 * firstSum + 2 * secondSum + yCoords[-1]) * 4
    return approxArea, pi * a * b


# Part 3: Vector Arithmetic
# -------------------------------------------------------------------------------------
def vector_computeXCoordinates(a, intervals):
    #a = length of the semi-major axis
    #intervals = the number of intervals
    
    return np.linspace(0, a, intervals + 1)


def vector_ellipse(a, b, xValues):
    #xValues = the list of xCoordinates
    #a = length of the semi-major axis
    #b = length of the semi-minor axis
    
    return b * np.sqrt(1 - (xValues / a) ** 2)


def vector_computeArea(a, b, intervals):
    #xValues = list of xCoordinates
    #yCoords = list of y coordinates
    #a = length of the semi-major axis
    #b = length of the semi-minor axis
    #intervals = the number of intervals 
    #i = index variable
    #h = a / intervals
    #firstSum = first summation of the simpsons rule
    #secondSum = second summation of the simpsons rule
    #approxArea = approximate area of ellipse using simpsons rule
    
    xValues = vector_computeXCoordinates(a, intervals)
    yCoords = vector_ellipse(a, b, xValues)
    h = a / intervals
    firstSum = np.sum(yCoords[1:-1:2])
    secondSum = np.sum(yCoords[2:-2:2])
    approxArea = h / 3. * (yCoords[0] + 4 * firstSum + 2 * secondSum + yCoords[-1]) * 4
    return approxArea, pi * a * b


# Main loop
# -------------------------------------------------------------------------------------
#a = length of the semi-major axis
#b = length of the semi-minor axis
#intervals = the number of intervals
#t = timer for the run of program
#EOF = end of file

# Dictionary to map methods to their functions
methods_dict = {
    'list': list_computeArea,
    'array': array_computeArea,
    'vector': vector_computeArea
}

print('\n' + '-' * 80)
EOF = -1
compute_time_list = []
compute_time_array = []
compute_time_vector = []

while True:
    a = getPositiveNumber('Enter the length of the semi-major axis (0 to quit): ', EOF)
    if a == EOF:
        break
    b = getPositiveNumber('Enter the length of the semi-minor axis (0 to quit): ', EOF)
    if b == EOF:
        break
    intervals = int(getPositiveNumber('Enter the number of intervals (0 to quit): ', EOF))
    if intervals == EOF:
        break

    for method, func in methods_dict.items():
        t = timeit.Timer(lambda: func(a, b, intervals))
        computeTime = t.timeit(number=10) / 10  # Average over 10 runs
        approxArea, actualArea = func(a, b, intervals)
        
        print(f'''
Using {method} method:
The approximate area of the ellipse is {approxArea:.14e}
The actual area is {actualArea:.14e}
The error in the approximate area is {abs(actualArea - approxArea):.6e}
Compute time using {method} is {computeTime:.6f} seconds.
-------------------------------------------------------------------------------------
      ''')
        globals()[f'compute_time_{method}'].append(computeTime)



# Part 4: Analysis
# -------------------------------------------------------------------------------------
print("\nAnalysis:\n Each method is run a total of 10 times and the averages of all of them are presented together for cross-referencing.\n")
print(f"1. Average compute time using lists: {np.mean(compute_time_list):.6f} seconds.")
print(f"2. Average compute time using arrays: {np.mean(compute_time_array):.6f} seconds.")
print(f"3. Average compute time using arrays and vector arithmetic: {np.mean(compute_time_vector):.6f} seconds.")

displayTerminationMessage()