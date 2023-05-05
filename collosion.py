class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def test_wall_car(walls, carModel):
    vertices = carModel.get_vertices()

    for wall in walls:
        WallP1 = point(wall.x1, wall.y1)
        WallP2 = point(wall.x2, wall.y2)
        CarP0, CarP3 = point(vertices[0][0], vertices[0][1]), point(
            vertices[3][0], vertices[3][1])
        CarP1, CarP2 = point(vertices[1][0], vertices[1][1]), point(
            vertices[2][0], vertices[2][1])
        if intersect(WallP1, WallP2, CarP0, CarP3):
            return True
        if intersect(WallP1, WallP2, CarP1, CarP2):
            return True
        if intersect(WallP1, WallP2, CarP0, CarP1):
            return True
        if intersect(WallP1, WallP2, CarP2, CarP3):
            return True
    return False


def ccw(A, B, C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

# Return true if line segments AB and CD intersect


def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
