#
#   curve data profiles
#

import math
import roto_maths
import roto_geometry
from roto_settings import *

def compareProfiles(a, b):
    
    # compare profiles
    
    return roto_maths.magnitude(
        (b.x - a.x) * SCALE_X,
        (b.y - a.y) * SCALE_Y,
        (b.length - a.length) * SCALE_LENGTH,
        (b.points - a.points) * SCALE_NUMBER_POINTS,
        (b.width - a.width) * SCALE_WIDTH,
        (b.height - a.height) * SCALE_HEIGHT,
        (b.internalAngle - a.internalAngle) * SCALE_INTERNAL_ANGLE,
        sum([(b.siblings[i][0] - a.siblings[i][0]) for i in range(len(a.siblings))]) * SCALE_SIBLING_MAGNITUDE,
        sum([(b.siblings[i][1] - a.siblings[i][1]) for i in range(len(a.siblings))]) * SCALE_SIBLING_ANGLE,
        (1 if b.index != a.index else 0) * SCALE_INDEX
    )

def opposingQuadrants(a, b):
    angle = abs(roto_maths.angleDifference(a.simpleAngle, b.simpleAngle))
    
    if (angle > math.pi / 2):
        return True
    else:
        return False
    
    q1 = a.quadrant
    q2 = b.quadrant
    x1 = a.qx
    x2 = b.qx
    y1 = a.qy
    y2 = b.qy
    o1 = a.orientation
    o2 = b.orientation
    
    if (o1 == o2 == 'vertical') and (a.qy != b.qy):
        return True
    
    if (o1 == o2 == 'horizontal') and (a.qx != b.qx):
        return True
    
    if (o1 != o2) and ((q1 == 1 and q2 == 3) or (q1 == 3 and q2 == 1) or (q1 == 2 and q2 == 4) or (q1 == 4 and q2 == 2)):
        return True
    
    return False
    
class Profile:

    # generate a profile for classifying curves

    def __init__(self, path):
        data = path.data

        # svg attributes

        self.stroke = path.stroke
        self.fill = path.fill
        self.strokeWidth = path.strokeWidth
        
        # bezier attributes

        self.index = path.index
        self.points = len(data)
        self.x = sum(p.x for p in data) / len(data)
        self.y = sum(p.y for p in data) / len(data)
        self.length = sum(p.length for p in data)
        self.width = max(p.x for p in data) - min(p.x for p in data)
        self.height = max(p.y for p in data) - min(p.y for p in data)
        self.orientation = "horizontal" if self.width > self.height else "vertical"
        self.calculateAngles(data)
        self.getQuadrant(data)
        
    def translate(self, x, y):
        self.x += x
        self.y += y
    
    def calculateAngles(self, data):
        self.totalAngles = sum((p.angle - data[0].angle) for p in data)
        self.simpleAngle = roto_maths.angleBetween(data[0].p1, data[-1].p2)
        self.internalAngle = 0
        
        if len(data) > 1:
            for i in range(len(data) - 1):
                self.internalAngle += data[i + 1].angle - data[i].angleReverse

    def getQuadrant(self, data):
        if self.simpleAngle >= 0 and self.simpleAngle < math.pi / 2:
            self.qx = 1
            self.qy = 1
            self.quadrant = 1
        elif self.simpleAngle >= math.pi / 2 and self.simpleAngle <= math.pi:
            self.qx = -1
            self.qy = 1
            self.quadrant = 2
        elif self.simpleAngle > -math.pi / 2:
            self.qx = 1
            self.qy = -1
            self.quadrant = 4
        else:
            self.qx = -1
            self.qy = -1
            self.quadrant = 3

    def hasSameDrawAttributes(self, profile):
        return (self.stroke == profile.stroke and self.fill == profile.fill and self.strokeWidth == self.strokeWidth)
            
    def profileSiblings(self, paths):
        self.siblings = []
        
        if len(paths):
            for p in paths:
                if p.index != self.index: # self.hasSameDrawAttributes(p.profile):
                    self.siblings.append([roto_maths.magnitudeBetween(self, p.profile), p.profile.internalAngle])

            self.siblings = sorted(self.siblings, key=lambda x: x[0])
            self.siblings = self.siblings[:SIBLING_COUNT]
        
        if len(self.siblings) < SIBLING_COUNT:
            self.siblings += [[0, 0]] * (SIBLING_COUNT - len(self.siblings))
    
    def findMatch(self, paths):
        matches = []
        
        for p in paths:         
            if p.stroke == self.stroke and p.fill == self.fill and p.strokeWidth == self.strokeWidth:
                matches.append([p.index, compareProfiles(self, p.profile)])
        
        mag = -1
        match = None
        
        for m in matches:
            if m[1] < mag or mag == -1:
                match = m[0]
                mag = m[1]
        
        return match
    
class Proxy:
    
    # transform proxy
    
    def __init__(self, path, target):
        self.x = target.profile.x - path.profile.x
        self.y = target.profile.y - path.profile.y
        self.rotate = roto_maths.angleDifference(path.profile.simpleAngle, target.profile.simpleAngle)
        self.axis = roto_geometry.Point(complex(path.profile.x, path.profile.y))

    def transformBezier(self, bezier):
        newBezier = bezier.getTransformed(self.x, self.y, self.rotate, self.axis)
        
        return newBezier

    def getTransformAtTime(self, t):
        x = -1 * self.x * (1 - t)
        y = -1 * self.y * (1 - t)
        rotate = -1 * self.rotate * (1 - t)
        axis = roto_geometry.Point(complex(self.axis.x + self.x, self.axis.y + self.y))
        
        return x, y, rotate, axis