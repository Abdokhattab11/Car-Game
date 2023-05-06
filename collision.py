def detect_collision(carModel, lst_of_lines):
    v = carModel.get_vertices()
    vertices = [[int(x) for x in rows] for rows in v]

    bottom_left = vertices[0]
    bottom_right = vertices[1]
    top_right = vertices[2]
    top_left = vertices[3]

    for line in lst_of_lines:
        dx, dy = 0, 0
        if line.vertical:
            dx = 2
        else :
            dy = 2
        if two_lines_intersection(top_left, top_right, [line.x1+dx, line.y1+dy], [line.x2+dx, line.y2+dy]) or \
                two_lines_intersection(top_left, top_right, [line.x1-dx, line.y1-dy], [line.x2-dx, line.y2-dy]):
            return True
        elif two_lines_intersection(bottom_right, top_right, [line.x1+dx, line.y1+dy], [line.x2+dx, line.y2+dy]) or \
                two_lines_intersection(bottom_right, top_right, [line.x1-dx, line.y1-dy], [line.x2-dx, line.y2-dy]):
            return True
        elif two_lines_intersection(bottom_left, bottom_right, [line.x1+dx, line.y1+dy], [line.x2+dx, line.y2+dy]) or \
                two_lines_intersection(bottom_left, bottom_right, [line.x1-dx, line.y1-dy], [line.x2-dx, line.y2-dy]):
            return True
        elif two_lines_intersection(bottom_left, top_left, [line.x1+dx, line.y1+dy], [line.x2+dx, line.y2+dy]) or \
                two_lines_intersection(bottom_left, top_left, [line.x1-dx, line.y1-dy], [line.x2-dx, line.y2-dy]):
            return True
    return False

def line_equation(point_1, point_2):
    x1, y1, x2, y2 = point_1[0], point_1[1], point_2[0], point_2[1]
    slope_numerator = y2 - y1
    slope_denominator = x2 - x1

    a = -1 * slope_numerator
    b = slope_denominator
    c = slope_denominator * y1 - slope_numerator * x1

    # in form a*x + b*y = c
    return [a, b, c]

def two_lines_intersection(A, B, C, D):
    # equation of first line
    [a1, b1, c1] = line_equation(A, B)
    # equation of second line
    [a2, b2, c2] = line_equation(C, D)

    determinant = a1 * b2 - a2 * b1

    if (determinant == 0):
        # lines are parallel
        if A[0] != C[0] and A[1] != C[1]:
            # lines are not the same
            return False
        # intersection point
        x = A[0]
        y = A[1]
    else:
        # intersection point
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant

    # Check if intersection point is within both line
    if ((A[0] <= x <= B[0] or B[0] <= x <= A[0]) and
        (A[1] <= y <= B[1] or B[1] <= y <= A[1]) and
        (C[0] <= x <= D[0] or D[0] <= x <= C[0]) and
        (C[1] <= y <= D[1] or D[1] <= y <= C[1])):
        return True
    else:
        return False
