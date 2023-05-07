from math import *
import sys

OO = 1000000000
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Collosion:
    

    def line_polygon_intersect(self,line, vertices):
        """
        return True if Line intersect with rect
        """
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

    # Resource1 : https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
    # Resource2 : https://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/

    def intersect(self,A, B, C, D):
        # Return true if line segments AB and CD intersect
        return self.ccw(A, C, D) != self.ccw(B, C, D) and self.ccw(A, B, C) != self.ccw(A, B, D)

    def ccw(self,A, B, C):
        return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)
    

    # Resource1 : https://gamedev.stackexchange.com/questions/43873/how-does-the-sat-collision-detection-algorithm-work
    # Resource2 : https://gamedevelopment.tutsplus.com/tutorials/collision-detection-using-the-separating-axis-theorem--gamedev-169
    
    def two_polygon_intersect(self, VerticesA ,VerticesB):
        """
        Vertices : 2D List , Vertices[i][0] -> x, Vertices[i][1] -> y
        """
        # First we need to find all edges in shape A
        n = len(VerticesA)
        for i in range(n):
            p1 = VerticesA[i]
            p2 = VerticesA[(i+1) % n]
            axis = self.get_unit_normal_vector(p1,p2)
            # for Each Axis we need to project all points from shape A, and all points from shape B , then compare
            projA = self.projectVertices(VerticesA, axis)
            projB = self.projectVertices(VerticesB, axis)
            #There's a gap if (maxB < minA) or (maxA < minB) -->> return False No intersection
            if projB[1] < projA[0] or projA[1] < projB[0]:
                return False
        n = len(VerticesB)
        for i in range(n):
            p1 = VerticesB[i]
            p2 = VerticesB[(i+1) % n]
            axis = self.get_unit_normal_vector(p1,p2)
            # for Each Axis we need to project all points from shape A, and all points from shape B , then compare
            projA = self.projectVertices(VerticesA, axis)
            projB = self.projectVertices(VerticesB, axis)
            #There's a gap if (maxB < minA) or (maxA < minB) -->> return False No intersection
            if projB[1] < projA[0] or projA[1] < projB[0]:
                return False
        return True
            

    def projectVertices(self,vertices,axis):
        minA, maxA = OO, -OO
        # to project point on axis , just do dot product
        for v in vertices:
            proj = axis[0]*v[0] + axis[1]*v[1]
            if proj < minA:
                minA = proj
            if proj > maxA:
                maxA = proj
        return (minA,maxA)
    
    def get_unit_normal_vector(self,p1,p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        magnitude = sqrt(dx**2 + dy**2)
        if magnitude != 0: # To avoid division by zero
            dx = dx/magnitude
            dy = dy/magnitude
        return [-dy,dx]

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
        if i.collected == True:
            continue
        coinVertices = i.get_vertices()
        if col.two_polygon_intersect(carVertices,coinVertices):
            i.collected = True
            return True
    return False

def test_car_bomb(carModel,bombs):
    carVertices = carModel.get_vertices()
    for i in bombs:
        bombVertices = i.get_vertices()
        if col.two_polygon_intersect(carVertices,bombVertices) == True:
            return True
    return False

        
if __name__ == "__main__":
    c = Collosion()
    if c.two_polygon_intersect([[0,0],[10,0],[10,10],[0,10]], [[20,0],[30,0],[30,10],[20,10]]) == False:
        print("True")
    else:
        print("Expected True output False")
    if c.two_polygon_intersect([[0,0],[10,0],[10,10],[0,10]], [[5,0],[15,0],[15,10],[5,10]]) == True: 
        print("True")
    else:
        print("Expected True output False")
    if c.two_polygon_intersect([[20.0, 50.0], [20.0, 20.0], [80.0, 20.0], [80.0, 50.0]], [[100, 350], [100, 400], [150, 400], [150, 350]]) == False:
        print("True")
    else:
        print("Expected True output False")
    if c.two_polygon_intersect([[327.8437342690493, 68.23378448111289], [354.661908380755, 54.78813323938297], [381.5532108642146, 108.42448146279385], [354.7350367525089, 121.87013270452377]], [[100, 350], [100, 400], [150, 400], [150, 350]]) == False: 
        print("True")
    else:
        print("Expected True output False")
    