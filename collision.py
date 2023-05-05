def detect_collision(carModel, lst_of_lines):

    rotated_vertices = carModel.get_vertices()
    int_vertices = [[int(val) for val in row] for row in rotated_vertices]

    bottom_left = int_vertices [0]
    bottom_right = int_vertices [1]
    top_right = int_vertices [2]
    top_left = int_vertices [3]
    print("")
    print (bottom_left)
    print (bottom_right)
    print (top_right)
    print (top_left)

    for line in lst_of_lines:
        if line_line_intersection(top_left, top_right, (line.x1, line.y1), (line.x2, line.y2)):
            return True
        elif line_line_intersection(bottom_right, top_right, (line.x1, line.y1), (line.x2, line.y2)):
            return True
        elif line_line_intersection(bottom_left, bottom_right, (line.x1, line.y1), (line.x2, line.y2)):
            return True
        elif line_line_intersection(bottom_left, top_left, (line.x1, line.y1), (line.x2, line.y2)):
            return True
    # No intersection detected
    return False


def line_line_intersection(A, B, C, D):
    # Line AB represented as a1x + b1y = c1
    a1 = B[1] - A[1]
    b1 = A[0] - B[0]
    c1 = a1*(A[0]) + b1*(A[1])
 
    # Line CD represented as a2x + b2y = c2
    a2 = D[1] - C[1]
    b2 = C[0] - D[0]
    c2 = a2*(C[0]) + b2*(C[1])
 
    determinant = a1*b2 - a2*b1
 
    if (determinant == 0):
        # The lines are parallel. This is simplified
        # by returning a pair of FLT_MAX
        if A[0] != C[0] and A[1] != C[1]:
            return False
        x = A[0]
        y = A[1]
    else:
        x = (b2*c1 - b1*c2)/determinant
        y = (a1*c2 - a2*c1)/determinant
    # Check if intersection point is within bounds of both line segments
    if ((A[0] <= x <= B[0] or B[0] <= x <= A[0]) and 
        (A[1] <= y <= B[1] or B[1] <= y <= A[1]) and 
        (C[0] <= x <= D[0] or D[0] <= x <= C[0]) and 
        (C[1] <= y <= D[1] or D[1] <= y <= C[1])):
        return True
    else:
        return False
