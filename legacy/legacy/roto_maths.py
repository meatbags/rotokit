#
#   maths
#

import math, svg.path

def magnitude(*args):
    
    mag = math.sqrt(sum(math.pow(arg, 2) for arg in args))
    
    return mag

def magnitudeBetween(p1, p2):
    
    mag = math.sqrt(math.pow(p2.x - p1.x, 2) + math.pow(p2.y - p1.y, 2))
    
    return mag

def angleBetween(p1, p2):
    
    angle = math.atan2(p2.y - p1.y, p2.x - p1.x)
    
    return angle

def angleDifference(a1, a2):
    
    angle = math.atan2(math.sin(a2 - a1), math.cos(a2 - a1))

    return angle
    
# complex numbers

def magnitudeBetweenComplex(p1, p2):
    
    mag = math.sqrt(math.pow(p2.real - p1.real, 2) + math.pow(p2.imag - p1.imag, 2))
    
    return mag

def angleBetweenComplex(p1, p2):
    
    angle = math.atan2(p2.imag - p1.imag, p2.real - p1.real)
    
    return angle

# coordinates

def polarToCartesian(x, y, angle, mag):
    newX = x + math.cos(angle) * mag
    newY = y + math.sin(angle) * mag
    
    return newX, newY

# bezier functions

def sliceBezier(bez, t):

    # De Casteljau's algorithm
    # create two bezier curves by slicing at point t [0,1] along the curve
    
    A = bez.start;
    B = bez.control1;
    C = bez.control2;
    D = bez.end;
    E = A + (B - A) * t;
    F = B + (C - B) * t;
    G = C + (D - C) * t;
    H = E + (F - E) * t;
    J = F + (G - F) * t;
    K = H + (J - H) * t;
    
    return svg.path.CubicBezier(A,E,H,K), svg.path.CubicBezier(K,J,G,D);

def smoothBezierCurves(a, b, t):
    # bezier A
    
    a_p = a.end
    a_cp = a.control2
    a_angle = angleBetweenComplex(a_p, a_cp)
    a_mag = magnitudeBetweenComplex(a_p, a_cp)
    
    # bezier B
    
    b_p = b.start
    b_cp = b.control1
    b_angle = angleBetweenComplex(b_p, b_cp)
    b_mag = magnitudeBetweenComplex(b_p, b_cp)
    
    # get new control positions
    
    difference = angleDifference(a_angle, b_angle)
    
    if difference > 0:
        tune = (math.pi * 0.5) - (difference / 2)
    else:
        tune = (-math.pi * 0.5) - (difference / 2)
    
    tune *= t
    a_angle -= tune
    b_angle += tune
    
    a_x, a_y = polarToCartesian(a_p.real, a_p.imag, a_angle, a_mag)
    b_x, b_y = polarToCartesian(b_p.real, b_p.imag, b_angle, b_mag)
    
    # transfer
    
    a.control2 = complex(a_x, a_y)
    b.control1 = complex(b_x, b_y)
    