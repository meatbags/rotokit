#
#   geometric analysis and interpolation
#

import svg.path
import math
from xml.dom import minidom

import roto_profile
import roto_maths
from roto_settings import *
from roto_geometry import *

# composite geometry

class Path:

    # a collection of bezier curves
    
    def __init__(self, path, tag, index):

        # extract tag data

        self.index = index
        self.fill = tag.getAttribute("fill");
        self.stroke = tag.getAttribute("stroke");
        self.strokeWidth = 0;

        if self.stroke:
            self.strokeWidth = 1;

        try:
            if tag.getAttribute("stroke-width"):
                self.strokeWidth = tag.getAttribute("stroke-width")
        except: # NameError
            pass

        # create bezier curve objects from file data

        self.path = path;
        self.data = [];

        for p in self.path:
            if isinstance(p, svg.path.Line):
                self.data.append(Bezier(p, bezFlag=False)); # convert straight line -> curve
            if isinstance(p, svg.path.CubicBezier):
                self.data.append(Bezier(p));

        # generate path profile

        self.profile = roto_profile.Profile(self)

        # normalise position attribute [0, 1] for beziers

        pathLength = self.profile.length
        length = 0;

        for p in self.data:
            p.position = length / pathLength
            p.positionEnd = (length + p.length) / pathLength
            length += p.length;
        
        # sorting
        
        self.sorted = False
        self.reversed = False
    
    def setIndex(self, index):
        self.index = index
        self.profile.index = index
    
    def profileSiblings(self, paths):
        self.profile.profileSiblings(paths)
    
    def findTarget(self, paths):

        # search for most similar path

        match = self.profile.findMatch(paths)

        if match != None:
            self.target = paths[match]

            if roto_profile.opposingQuadrants(self.profile, self.target.profile):
                self.reversePath()
            
            if not self.sorted:
                paths[match].sorted = True

    def interpolatePaths(self):
        self.pathFrom = [];
        self.pathProxy = [];
        self.pathTo = [];
        
        # proxy transform data
        
        self.proxy = roto_profile.Proxy(self, self.target)
        
        # create a new set of points
        
        if self.profile.points != self.target.profile.points:
            pos = [0] + self.getPositions() + self.target.getPositions() + [1];
            pos.sort();
            targetPos = pos;
        else:
            pos = [0] + self.getPositions() + [1];
            targetPos = [0] + self.target.getPositions() + [1];
        
        # create a transformed path from proxy
        
        for i in range(0, len(pos)-1):
            bezFrom = Bezier(self.bezierFromPath(pos[i], pos[i+1]));
            bezProxy = self.proxy.transformBezier(bezFrom)          
            bezTo = Bezier(self.target.bezierFromPath(targetPos[i], targetPos[i+1]));

            self.pathFrom.append(bezFrom);
            self.pathProxy.append(bezProxy);
            self.pathTo.append(bezTo);
    
    def getPositions(self):

        # get point positions

        return [self.data[i].position for i in range(1, len(self.data))];
    
    def reversePath(self):

        # reverse bezier curves

        self.data = self.data[::-1];

        for p in self.data:
            p.reverseCurve()
        
        # cache sibling data
        
        siblings = self.profile.siblings
        self.profile = roto_profile.Profile(self)
        self.profile.siblings = siblings
        
        # store value
        
        self.reversed = True
        
    def bezierFromPath(self, p1, p2):

        # create new bezier at point on path

        target = self.data[0]

        for b in self.data:
            if b.position <= p1 and b.positionEnd >= p2:
                target = b
                break

        if p1 == target.position and p2 == target.positionEnd:
            return target.bez

        # p1---x---|-------p2

        if p1 == target.position:
            b1, b2 = roto_maths.sliceBezier(target.bez, p2)
            return b1

        # p1-------|---x---p2

        if p2 == target.positionEnd:
            b1, b2 = roto_maths.sliceBezier(target.bez, p1)
            return b2

        # p1---|---x---|---p2

        b1, b2 = roto_maths.sliceBezier(target.bez, p1)
        b3, b4 = roto_maths.sliceBezier(b2, p2)

        return b3
 
    def getAttrString(self):

        # SVG attribute string

        if self.strokeWidth:
            return 'stroke="{0}" stroke-linecap="round" fill="{1}" stroke-width="{2}" stroke-miterlimit="10"'.format(
                LINE_COLOUR if LINE_COLOUR else self.stroke, self.fill, self.strokeWidth
            );
        else:
            return 'fill="{0}" stroke-miterlimit="10"'.format(self.fill)
 
    def translate(self, x, y):

        # utility for centralising animation frames

        self.profile.translate(x, y)

        for bez in self.data:
            bez.translate(x, y)
    
    def getPathAtTime(self, t):

        # convert path data into svg.path.Path object for easier saving

        newPath = svg.path.Path();
        prev = False;
        x, y, rotate, axis = self.proxy.getTransformAtTime(t)
        smoothing = math.sin(t * math.pi) * CURVE_SMOOTHING
        
        for i in range(0, len(self.pathProxy)):
            a = self.pathProxy[i].bez
            b = self.pathTo[i].bez
            start = a.start + (b.start - a.start) * t
            control1 = a.control1 + (b.control1 - a.control1) * t
            control2 = a.control2 + (b.control2 - a.control2) * t
            end = a.end + (b.end - a.end) * t
            proxyBezier = Bezier(svg.path.CubicBezier(start, control1, control2, end))
            bez = proxyBezier.getTransformed(x, y, rotate, axis)
            newPath.append(bez.bez)
            
            if prev:
                # snap points together
                
                newPath[-1].start = newPath[-2].end = (newPath[-1].start + newPath[-2].end) * 0.5
            
                # smoothing
            
                roto_maths.smoothBezierCurves(newPath[-2], newPath[-1], smoothing)
            
            prev = bez.bez;

        d = newPath.d()

        return d

class Group:

    # a collection of paths, frame data container

    def __init__(self, id, g):
        self.id = id;
        self.iteration = 0;
        self.paths = [];
        
        # parse SVG data
        # paths
        
        paths = g.getElementsByTagName("path");
        index = 0
        
        for p in paths:
            path = svg.path.parse_path(p.getAttribute("d"));
            if len(path) != 0:
                self.paths.append(Path(path, p, index))
                index += 1
        
        # lines
        
        lines = g.getElementsByTagName("line");
        
        for i in range(len(lines)):
            l = lines[i]
            x1 = float(l.getAttribute("x1"))
            y1 = float(l.getAttribute("y1"))
            x2 = float(l.getAttribute("x2"))
            y2 = float(l.getAttribute("y2"))
            path = svg.path.Path(svg.path.Line(complex(x1, y1), complex(x2, y2)))
            self.paths.append(Path(path, l, index))
            index += 1
        
        # polylines
        
        polylines = g.getElementsByTagName("polyline");
        
        for i in range(len(polylines)):
            pl = polylines[i];
            pts = pl.getAttribute("points").split(" ");
            
            for j in range(len(pts) - 1, -1, -1):
                if pts[j] == "":
                    pts.pop(j);
                else:
                    pt = pts[j].split(",");
                    pt[0] = float(pt[0])
                    pt[1] = float(pt[1])
                    pts[j] = pt
            
            for j in range(1, len(pts)):
                path = svg.path.Path(svg.path.Line(complex(pts[j][0], pts[j][1]), complex(pts[j-1][0], pts[j-1][1])));
                self.paths.append(Path(path, pl, index))
                index += 1
        
        # colour mode
        
        if COLOUR_MODE == "exclude":
            self.paths = [p for p in self.paths if p.stroke not in COLOUR_MAP]
            
            for i in range(len(self.paths)):
                self.paths[i].setIndex(i)
                
        elif COLOUR_MODE == "include":
            self.paths = [p for p in self.paths if p.stroke in COLOUR_MAP]
            
            for i in range(len(self.paths)):
                self.paths[i].setIndex(i)
        
        # attributes
        
        self.x = sum(p.profile.x for p in self.paths) / len(self.paths)
        self.y = sum(p.profile.y for p in self.paths) / len(self.paths)
        
        # profile siblings
        
        for p in self.paths:
            p.profileSiblings(self.paths)
        
        # containers
        
        self.tweenPaths = []
    
    def nextFrame(self, g):
    
        # find target paths
    
        for p in self.paths:
            p.findTarget(g.paths);

            if p.target != None:
                p.interpolatePaths();
            
    def tweenFrame(self, time):
    
        # find the in-between frame at time [0,1]
    
        self.tweenPaths = [];
        
        for p in self.paths:
            if (not IGNORE_SORTED) or (not p.sorted):
                if p.target != None:
                    attr = p.getAttrString();
                    d = p.getPathAtTime(time);
                    self.tweenPaths.append('<path ' + attr + ' d="' + d + '"/>');
     
    def hasPaths(self):
        return (len(self.tweenPaths) != 0);
        
    def getPaths(self):
        paths = []
        
        for i in range(len(self.tweenPaths)):
            paths.append({"path": self.tweenPaths[i], "index": i});

        return paths;
    
    def iterate(self):
        self.iteration += 1;
        
    def resetSortedFlags(self):
        for p in self.paths:
            p.sorted = False
            p.target = None
            p.reversed = False
            
    def centrePaths(self, centreX, centreY):
    
        # move all paths to centre on X
    
        deltaX = centreX - self.x;
        deltaY = centreY - self.y;
        
        for p in self.paths:
            p.translate(deltaX, deltaY);

# convert path data to string

def groupsToGroupString(groups):

    # groups to SVG group format

    id = groups[0].id;
    iteration = groups[0].iteration;
    paths = [];
    
    for g in groups:
        if g.hasPaths():
            gp = g.getPaths();
            for p in gp:
                paths.append(p);
    
    paths = sorted(paths, key=lambda path: path["index"]);
    str = str = '\t<g id="{0}_{1}">\n'.format(id, iteration) + "".join(['\t\t' + p["path"] + '\n' for p in paths]) + '\t</g>\n';
    
    for g in groups:
        g.iterate();
    
    return str;
    