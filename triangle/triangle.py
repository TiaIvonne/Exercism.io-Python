
def equilateral(sides):
    # triangles with 0 value doesn't exist
    # you can use set() for delete duplicate values. For example: from [1,1,1] => [1]
    if len(set(sides)) != 1 or 0 in sides:
        return False
    else:
        return True
   
def isosceles(sides):
    # equilateral triangle also is isosceles triangle too
    sides.sort()
    # a triangle exists when the sum of two sides is greather than third side
    # if triangle doesn't exist return false
    if sum(sides[:2]) < sum(sides[2:]):
        return False
    if len(set(sides)) == 3:
       return False
    else:
        return True

def scalene(sides):
    sides.sort()
    if sum(sides[:2]) < sum(sides[2:]):
        return False
    if len(set(sides)) == 3:
        return True
    else:
        return False