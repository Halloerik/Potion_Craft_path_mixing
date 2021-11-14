from typing import List

import numpy as np


class CubicBezierCurve:
    def __init__(self, control_points, line_segments=1000):
        self.control_points = control_points

        self.line_segments = line_segments
        self.coordinates = self.bernstein_cubic_line()
        self.look_up_table = []
        self.generate_look_up_table()
        self.length = self.look_up_table[-1]

    def bernstein_cubic_point(self, t):
        p0 = self.control_points[0] * (- t ** 3 + 3 * t ** 2 - 3 * t + 1)
        p1 = self.control_points[1] * (3 * t ** 3 - 6 * t ** 2 + 3 * t)
        p2 = self.control_points[2] * (-3 * t ** 3 + 3 * t ** 2)
        p3 = self.control_points[3] * (t ** 3)
        return p0 + p1 + p2 + p3

    def speed(self, t):
        p0 = self.control_points[0] * (- 3 * t ** 2 + 6 * t - 3)
        p1 = self.control_points[1] * (9 * t ** 2 - 12 * t + 3)
        p2 = self.control_points[2] * (-9 * t ** 2 + 6 * t)
        p3 = self.control_points[3] * (3 * t ** 2)
        return p0 + p1 + p2 + p3

    def acceleration(self, t):
        p0 = self.control_points[0] * (- 6 * t + 6)
        p1 = self.control_points[1] * (18 * t - 12)
        p2 = self.control_points[2] * (-18 * t + 6)
        p3 = self.control_points[3] * (6 * t)
        return p0 + p1 + p2 + p3

    def bernstein_cubic_line(self):
        points = np.zeros((self.line_segments + 1, 2))
        for t in range(self.line_segments + 1):
            points[t] = self.bernstein_cubic_point(t / self.line_segments)

        return points

    def generate_look_up_table(self):
        self.look_up_table = np.zeros((self.line_segments + 1))
        previous_point = self.bernstein_cubic_point(0)
        for t in range(1, self.line_segments + 1):
            current_point = self.bernstein_cubic_point(t / self.line_segments)
            distance = np.linalg.norm(current_point - previous_point) + self.look_up_table[t - 1]
            previous_point = current_point

            self.look_up_table[t] = distance

    def get_distance(self, t):
        for i in range(1, self.line_segments + 1):
            t1 = (i - 1) / self.line_segments
            t2 = i / self.line_segments
            if t1 <= t <= t2:
                d1 = self.look_up_table[i - 1]
                d2 = self.look_up_table[i]
                # t = (t - t1) / (t2 - t1)
                # return d1 * t + d2 * (1 - t)
                return lerp(t1, t2, t, d1, d2)

    def get_t(self, d):
        for i in range(1, self.line_segments + 1):
            d1 = self.look_up_table[i - 1]
            d2 = self.look_up_table[i]
            if d1 <= d <= d2:
                t1 = (i - 1) / self.line_segments
                t2 = i / self.line_segments
                # d = (d - d1) / (d2 - d1)
                # return t1 * d + t2 * (1 - d)
                return lerp(d1, d2, d, t1, t2)


class BezierCurve:
    def __init__(self, curves, line_segments=1000):
        self.curves = [CubicBezierCurve(curve, line_segments) for curve in curves]

        self.line_segments = line_segments
        # self.coordinates = self.curves[0].coordinates
        self.length = 0
        for curve in self.curves:
            # self.coordinates = np.vstack((self.coordinates, curve.coordinates))
            self.length += curve.length

        self.coordinates = np.zeros((line_segments + 1, 2))
        for i in range(line_segments + 1):
            self.coordinates[i] = self.get_coordinate(i / line_segments)

        self.length_at_coordinate = self.make_length_by_coordinate_table()
        self.length = self.length_at_coordinate[-1]

    def get_t(self, d):
        for curve in self.curves:
            if d - curve.length <= 0:
                t = curve.get_t(d)
                return curve, t
            else:
                d -= curve.length
        return self.curves[-1], 1

    def get_coordinate(self, p):
        d = p * self.length
        curve, t = self.get_t(d)
        return curve.bernstein_cubic_point(t)

    def make_length_by_coordinate_table(self):
        lengths = np.zeros((self.coordinates.shape[0]))
        for i in range(1, self.coordinates.shape[0]):
            lengths[i] = lengths[i - 1] + np.linalg.norm(self.coordinates[i] - self.coordinates[i - 1])
        # print(lengths.shape)
        return lengths

    def get_grind_path(self, grind_percentage):

        grind_length = grind_percentage * self.length
        left_index, left_length = find_closest(self.length_at_coordinate, grind_length)
        right_index, right_length = (left_index + 1, self.length_at_coordinate[left_index + 1])

        middle_coordinate = lerp(left_length, right_length, grind_length,
                                 self.coordinates[left_index], self.coordinates[right_index])

        grinded_part = np.vstack((self.coordinates[:left_index], middle_coordinate))
        unground_part = np.vstack((middle_coordinate, self.coordinates[left_index:]))
        return grinded_part, unground_part


def add_curves(curves: List['BezierCurve'], grind_levels: list = None, segments=100):
    """

    :param curves:
    :param grind_levels:
    :param segments:
    :return:
    """
    if grind_levels is None:
        grind_levels = [1.0, 1.0, 0]
    elif len(grind_levels) == 2:
        grind_levels.append(0)
    elif len(grind_levels) == 3:
        #grind_levels[2] = min(2 - (grind_levels[0]+grind_levels[1]),grind_levels[2])
        grind_levels[0] += grind_levels[2]/2
        grind_levels[1] += grind_levels[2]/2
        if grind_levels[0]>1 and grind_levels[1]>1:
            grind_levels[0] = 1
            grind_levels[1] = 1
        elif grind_levels[0]>1:
            overgrinded = grind_levels[0] - 1
            grind_levels[0] = 1
            grind_levels[1] = min(grind_levels[1]+overgrinded, 1)
        elif grind_levels[1]>1:
            overgrinded = grind_levels[1] - 1
            grind_levels[0] = min(grind_levels[0]+overgrinded, 1)
            grind_levels[1] = 1


    first_grinded, first_unground = curves[0].get_grind_path(grind_levels[0])
    second_grinded, second_unground = curves[1].get_grind_path(grind_levels[1])

    grinded_coordinates = np.zeros((segments + 1, 2))
    unground_coordinates = np.zeros((segments + 1, 2))
    zero = np.zeros((1, 2))
    for i in range(1, segments + 1):
        # print(i,"/",segments)
        # sum_ = sum([curve.get_coordinate(i / segments) for curve in curves])
        # grinded_coordinates[i] = sum_
        """
        grinded_coordinates[i] = sum([curve.get_coordinate(grind_levels[j] * i / segments)
                                      for j, curve in enumerate(curves)])
        unground_coordinates[i] = sum([curve.get_coordinate(grind_levels[j] + (1 - grind_levels[j]) * i / segments)
                                       for j, curve in enumerate(curves)])
        """
        first_index = int(first_grinded.shape[0] * (i - 1) / segments)
        second_index = int(second_grinded.shape[0] * (i - 1) / segments)

        grinded_coordinates[i] = (first_grinded[first_index] if first_grinded.shape[0] > 0 else zero) + \
                                 (second_grinded[second_index] if second_grinded.shape[0] > 0 else zero)

        first_index = int((first_unground.shape[0]) * (i - 1) / segments)
        second_index = int((second_unground.shape[0]) * (i - 1) / segments)
        unground_coordinates[i] = first_unground[first_index] + second_unground[second_index]

    unground_coordinates[0] = grinded_coordinates[-1]
    return grinded_coordinates, unground_coordinates


def find_closest(values: list, query: float):
    """Finds the closest value to the value parameter

    :param values: List of numbers. This function assumes the list is sorted!
    :param query: The number that is searched
    :return: index and closest value to the query
    """

    left_index = 0
    right_index = len(values) - 1

    if query < values[0]:
        # print("query < values[0]")
        return 0, values[0]
    elif query > values[right_index]:
        # print("query > values[right_index]")
        return right_index, values[right_index]

    while right_index - left_index > 1:

        middle_index = (left_index + right_index) // 2
        # print(left_index,middle_index,right_index,query,values[middle_index])
        if values[middle_index] == query:
            return middle_index, values[left_index]
        elif values[middle_index] >= query:
            right_index = middle_index
        else:
            left_index = middle_index
    # print(left_index,right_index)

    return left_index, values[left_index]


def lerp(a, b, p, x=1, y=0):
    """Calculates the t value that result in p when interpolating a and b and interpolates x and y by the same t value

    :param a: first value
    :param b: second value
    :param p: interpolated value between a and b
    :param x: first value that will be interpolated
    :param y: second value that will be interpolated
    :return: x and y interpolated by t. In the case that x=1 and y=0 t is returned
    """
    t = (p - a) / (b - a)
    return x * t + y * (1 - t)
