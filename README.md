# Ellipse-Area-Approximation-Using-Simpsons-Rule

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [How to Run](#how-to-run)
5. [Results](#results)
6. [Analysis](#analysis)
7. [Significance](#significance)
8. [Author](#author)
9. [License](#license)

## Introduction
This Python project approximates the area of an ellipse using Simpson's Rule. It explores the performance of three different methods for implementing the rule:
1. Python Lists
2. NumPy Arrays
3. NumPy Arrays with Vector Arithmetic

The main goal is to understand the trade-offs between different data structures and the advantages of using vector arithmetic for numerical computations.

## Features
- Calculates the approximate area of an ellipse with user-defined semi-major and semi-minor axes and intervals
- Measures the compute time for each method
- Provides an error analysis comparing the approximate and actual areas

## Technologies Used
- Python
- NumPy
- timeit (for performance measurement)

## How to Run
1. Clone the repository
2. Run `main.py`
3. Follow the on-screen prompts to input the ellipse parameters and intervals

## Results
- The following parameters were used to generate these results:
  - Semi-major axis: 10.5
  - Semi-minor axis: 5.25
  - Intervals: 10,000,000
- All three methods yielded errors in the \(10^{-10}\) range, demonstrating high accuracy.
- Compute times for each method are as follows:
  - **List method**: 4.82 seconds
  - **Array method**: 6.21 seconds
  - **Vector method**: 0.18 seconds

## Analysis
1. **Error Analysis**: All methods show extremely low errors, which implies that for the case of computing areas of ellipses, all three methods are almost equally accurate.

2. **Time Complexity**: 
    - **List Method**: Not optimized for numerical calculations, leading to a higher computation time.
    - **Array Method**: Slightly slower than the list method, possibly due to array operation overheads.
    - **Vector Method**: Significantly faster, leveraging underlying optimized C/Fortran libraries.

3. **Trade-off Analysis**: Since all methods provide almost the same level of accuracy, the vector method is the most time-efficient.

## Significance
1. **Optimization**: The vector method is the most efficient approach for minimizing computational time while maintaining high accuracy.
2. **Generalizability**: The finding could extend to other computational problems that involve numerical approximations.
3. **Resource Allocation**: The vector method allows for more computational bandwidth for other tasks.
4. **Educational**: This exercise demonstrates the differences in performance between basic Python data structures and specialized numerical libraries.

## Author
**Farjad Tariq**

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
