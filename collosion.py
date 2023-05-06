from math import *
import sys

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Collosion:
    

    def line_polygon_intersect(self,line, rect_vertices):
        """
        return True if Line intersect with rect
        """
        vertices = rect_vertices
        WallP1 = point(line.x1, line.y1)
        WallP2 = point(line.x2, line.y2)
        CarP0, CarP3 = point(vertices[0][0], vertices[0][1]), point(
            vertices[3][0], vertices[3][1])
        CarP1, CarP2 = point(vertices[1][0], vertices[1][1]), point(
            vertices[2][0], vertices[2][1])
        if self.intersect(WallP1, WallP2, CarP0, CarP3):
            return True
        if self.intersect(WallP1, WallP2, CarP1, CarP2):
            return True
        if self.intersect(WallP1, WallP2, CarP0, CarP1):
            return True
        if self.intersect(WallP1, WallP2, CarP2, CarP3):
            return True
        return False


    def intersect(self,A, B, C, D):
        # Return true if line segments AB and CD intersect
        return self.ccw(A, C, D) != self.ccw(B, C, D) and self.ccw(A, B, C) != self.ccw(A, B, D)

    def ccw(self,A, B, C):
        return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)
    
    def two_polygon_intersect(self, VerticesA ,VerticesB):
        """
        we use Seperating Axis algrithm Here
        return True of Two polygon intersect 
        """
        # First we need to get all edges from two shapse
        n = len(VerticesA)
        for i in range(n):
            p1 = point(VerticesA[i][0], VerticesA[i][1])
            p2 = point(VerticesA[(i+1)%n][0], VerticesA[(i+1)%n][1])
            # To get normal Axis : https://stackoverflow.com/questions/1243614/how-do-i-calculate-the-normal-vector-of-a-line-segment
            axis = point(-(p2.y - p1.y), (p2.x - p1.x))
            # We need to get the unit vector of axis
            val = sqrt(axis.x**2+axis.y**2)
            if val != 0:
                axis.x = axis.x / val
                axis.y = axis.y / val
            mnA,mxA = sys.maxsize,-sys.maxsize
            self.projectVertices(VerticesA,axis,mnA,mxA)
            mnB,mxB = sys.maxsize,-sys.maxsize
            self.projectVertices(VerticesB,axis,mnB,mxB)
            # Test Separating axis
            if mnA <= mnB <= mxA and mnA <= mxB <= mxA:
                continue
            else:
                # There's a separating axis
                return False
        # Repeat the same process for edges in B 
        n = len(VerticesB)
        for i in range(n):
            p1 = point(VerticesB[i][0], VerticesB[i][1])
            p2 = point(VerticesB[(i+1)%n][0], VerticesB[(i+1)%n][1])
            axis = point(-(p2.y - p1.y), (p2.x - p1.x))
            # We need to get the unit vector of axis
            val = sqrt(axis.x**2+axis.y**2)
            if val != 0:
                axis.x = axis.x / val
                axis.y = axis.y / val
            mnA,mxA = sys.maxsize,-sys.maxsize
            self.projectVertices(VerticesA,axis,mnA,mxA)
            mnB,mxB = sys.maxsize,-sys.maxsize
            self.projectVertices(VerticesB,axis,mnB,mxB)
            # Test Separating axis
            if mnA <= mnB <= mxA and mnA <= mxB <= mxA:
                continue
            else:
                # There's a separating axis
                return False
        # No separating axis , so they are intersected
        return True

    def projectVertices(self,vertices,axis,mn,mx):
        for i in vertices:
            # To get the projection of a vertix on axis : just fo dot product
            proj = i[0]*axis.x + i[1] * axis.y
            if proj > mx:
                mx = proj
            if proj < mn:
                mn = proj

col = Collosion()

def test_car_walls(carModel, walls):
    vertices = carModel.get_vertices()
    for i in walls:
        if col.line_polygon_intersect(i,vertices):
            return True
    return False

def test_car_coin(carModel, coins):
    carVertices = carModel.get_vertices()
    for i in coins:
        coinVertices = i.get_vertices()
        if col.two_polygon_intersect(carVertices,coinVertices):
            i.collected = True

def test_car_bomb(carModel,bombs):
    carVertices = carModel.get_vertices()
    for i in bombs:
        bombVertices = i.get_vertices()
        if col.two_polygon_intersect(carVertices,bombVertices):
            i.collected = True
            carModel.health = 0