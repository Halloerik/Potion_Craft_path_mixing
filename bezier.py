import numpy as np


class CubicBezierCurve:
    def __init__(self, control_points, line_segments=1000):
        self.control_points = control_points

        self.line_segments = line_segments
        self.coordinates = self.bernstein_cubic_line()
        self.look_up_table = []
        self.generate_look_up_table()
        self.length = self.look_up_table[-1][1]

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
        points = []
        for t in range(self.line_segments + 1):
            points.append(self.bernstein_cubic_point(t / self.line_segments))

        return np.array(points)

    def generate_look_up_table(self):
        self.look_up_table = [[0, 0]]
        previous_point = self.bernstein_cubic_point(0)
        for t in range(1, self.line_segments + 1):
            current_point = self.bernstein_cubic_point(t / self.line_segments)
            distance = np.linalg.norm(current_point - previous_point)
            self.look_up_table.append([t / self.line_segments, distance])

    def get_distance(self, t):
        for i in range(1, self.line_segments + 1):
            t1, d1 = self.look_up_table[i - 1]
            t2, d2 = self.look_up_table[i]
            if t1 <= t <= t2:
                t = (t - t1) / (t2 - t1)
                return d1 * t + d2 * (1 - t)

    def get_t(self, d):
        for i in range(1, self.line_segments + 1):
            t1, d1 = self.look_up_table[i - 1]
            t2, d2 = self.look_up_table[i]
            if d1 <= d <= d2:
                d = (d - d1) / (d2 - d1)
                return t1 * d + t2 * (1 - d)


class BezierCurve:
    def __init__(self, curves, line_segments=1000):
        self.curves = [CubicBezierCurve(curve, line_segments) for curve in curves]

        self.line_segments = line_segments
        self.coordinates = self.curves[0].coordinates
        self.length = self.curves[0].length
        for curve in self.curves[1:]:
            self.coordinates = np.vstack((self.coordinates, curve.coordinates))
            self.length += curve.length

    def get_t(self, d):
        for curve in self.curves:
            if d - curve.length <= 0:
                t = curve.get_t(d)
                return curve, t
            else:
                d -= curve.length
        return self.curves[-1], 1

    def get_d_percentage(self, p):
        return p * self.length

    def get_coordinate(self, t):
        d = self.get_d_percentage(t)
        curve, t = self.get_t(d)
        return curve.bernstein_cubic_point(t)


def add_curves(curves: BezierCurve, segments=100):
    coordinates = np.zeros((segments + 1, 2))
    for i in range(1, segments + 1):
        sum_ = sum([curve.get_coordinate(i / segments) for curve in curves])
        coordinates[i] = sum_
    return coordinates
