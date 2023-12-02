#!/usr/bin/python3
""" Create a function def pascal_triangle(n)"""
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]  # First element in every row is 1
        if triangle:  # If not the first row
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)  # Last element in every row is 1

        triangle.append(row)

    return triangle
