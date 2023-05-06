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


# Normal equation : y = n*x + d , n = -1/m , m is slope, we can ignore d , as we only need to project points
# We need to project points of Shape A on normal axis and get min and max point
# and project also points of Shape B on normal axis and get min and max point
# Then Test if they are overlapping or not
# They overlap if (Amin <= Bmin <= Amax) or (Amin <= Bmax <= Amax)

# First Step : We need to Find normals of each line
# for Each point in shape A project it in curr Normal
# for Each point in shape B project it in curr Normal

def sat(carModel, box):
    carPoints = carModel.get_vertices()
    boxPoints = box.get_vertices()
    normals = get_normals(carPoints)
    normals = normals + get_normals(boxPoints)
    for n in normals:
        # For Each Line 1- Project د
        return


def get_normals(points):
    # Take Each two consecative points and from
    res = []
    n = len(points)
    for i in range(n):
        x1, y1 = points[i][0], points[i][1]
        x2, y2 = points[(i+1) % n][0], points[(i+1) % n][1]
        n = -1*(x1-x2)/(y1-y2)
        res.append(n)
    return n
