def sgn(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1

def circleToSquare(u,v):
    newU = u**2
    newV = v**2
    
    if (u == 0 or v == 0):
        return ((u,v))

    new2 = (newU + newV)**0.5/(u + v)**0.5
    
    if (newU >= newV):
        return ((sgn(u) * new2, sgn(u) * v / u * new2))
    else:
        return ((sgn(v) * u / v * new2, sgn(v) * new2))

    return (x,y)

print circleToSquare(1,1.0)
print circleToSquare(0,0)
print circleToSquare(-1,0)
print circleToSquare(0,-1)
print circleToSquare(1,0)
print circleToSquare(0,1)
print circleToSquare(0.0001,1)
print circleToSquare(20,20)
print circleToSquare(0.5,0.5)
print circleToSquare(0.95,0.95)
