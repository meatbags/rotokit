#
#	geometric data
#

import svg.path
import roto_maths
import math

class Point:
    def __init__(self, complexNo):
        self.x = complexNo.real
        self.y = complexNo.imag
        self.c = complexNo

    def translate(self, x, y):
        self.x += x
        self.y += y
        self.c = complex(self.x, self.y)

    def rotate(self, axis, angle):
        mag = roto_maths.magnitudeBetween(axis, self)
        angle += roto_maths.angleBetween(axis, self)
        self.x = axis.x + math.cos(angle) * mag
        self.y = axis.y + math.sin(angle) * mag
        self.c = complex(self.x, self.y)

    def getTransformed(self, axis, rotation, translateX, translateY):
        newPoint = Point(complex(self.x, self.y))
        newPoint.rotate(axis, rotation)
        newPoint.translate(translateX, translateY)

        return newPoint

class Bezier:
    
    # bezier curve
    
	def __init__(self, bez, bezFlag=True):

		# data from file

		self.bez = bez if bezFlag else svg.path.CubicBezier(bez.start, bez.start, bez.end, bez.end);

		# coordinates

		self.p1 = Point(self.bez.start);
		self.cp1 = Point(self.bez.control1);
		self.cp2 = Point(self.bez.control2);
		self.p2 = Point(self.bez.end);

		# general attributes for comparison

		self.x = (self.p1.x + self.p2.x) / 2
		self.y = (self.p1.y + self.p2.y) / 2
		self.angle = roto_maths.angleBetween(self.p1, self.p2)
		self.angleReverse = roto_maths.angleBetween(self.p2, self.p1)
		self.length = bez.length(error=1e-2);
		self.position = 0.0;
		self.positionEnd = 0.0;
        
	def reverseCurve(self):

		# reverse order of points in curve

		self.p1 = Point(self.bez.end);
		self.cp1 = Point(self.bez.control2);
		self.cp2 = Point(self.bez.control1);
		self.p2 = Point(self.bez.start);

		# reform bezier

		self.bez = svg.path.CubicBezier(complex(self.p1.x, self.p1.y), complex(self.cp1.x, self.cp1.y), complex(self.cp2.x, self.cp2.y), complex(self.p2.x, self.p2.y));

		# reflect angle

		tempAngle = self.angleReverse
		self.angleReverse = self.angle
		self.angle = tempAngle

		# reverse position data

		tempPosition = 1 - self.position
		self.position = 1 - self.positionEnd
		self.positionEnd = tempPosition
        
	def translate(self, x, y):
		self.x += x
		self.y += y
		self.p1.x += x
		self.p1.y += y
		self.cp1.x += x
		self.cp1.y += y
		self.cp2.x += x
		self.cp2.y += y
		self.p2.x += x
		self.p2.y += y
		self.bez.start += complex(x, y)
		self.bez.control1 += complex(x, y)
		self.bez.control2 += complex(x, y)
		self.bez.end += complex(x, y)

	def getTransformed(self, tx, ty, angle, axis):

		# create a new Bezier object with transformed coordinates

		p1 = self.p1.getTransformed(axis, angle, tx, ty)
		cp1 = self.cp1.getTransformed(axis, angle, tx, ty)
		cp2 = self.cp2.getTransformed(axis, angle, tx, ty)
		p2 = self.p2.getTransformed(axis, angle, tx, ty)
		newBez = svg.path.CubicBezier(p1.c, cp1.c, cp2.c, p2.c);

		return Bezier(newBez);