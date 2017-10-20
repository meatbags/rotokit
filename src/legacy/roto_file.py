#
#   file handling
#

from xml.dom import minidom;
from roto_analyse import *;
from roto_settings import *;
from os.path import dirname, abspath
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from math import floor
import subprocess
import os

def getFileSuffix(number, type):
    s = "_";
    
    if number > 99:
        s += str(number);
    elif number > 9:
        s += "0" + str(number);
    else:
        s += "00" + str(number);
    
    return s + type;
    
def openSVG(filename, centre):

    # open SVG1.1 file and convert to objects

    svg = minidom.parse(open(filename, "r"));
    tags = svg.getElementsByTagName("svg")[0].childNodes;
    pathGroups = [];
    
    for i in range(0, len(tags)):
        id = "group_{0}".format(i);
        g = tags[i];
        if g.nodeName == "g" and len(g.getElementsByTagName("image")) == 0 and (len(g.getElementsByTagName("path")) > 0 or len(g.getElementsByTagName("line")) > 0):
            pathGroups.append(Group(id, g))
    
    header = svg.getElementsByTagName("svg")[0];
    info = {
        "x": header.getAttribute("x").replace("px", ""),
        "y": header.getAttribute("y").replace("px", ""),
        "width": header.getAttribute("width").replace("px", "") if not SETTINGS_WIDTH else SETTINGS_WIDTH,
        "height": header.getAttribute("height").replace("px", "") if not SETTINGS_HEIGHT else SETTINGS_HEIGHT
    }
    svg.unlink();
    
    if centre:
        for g in pathGroups:
            x = int(int(info["width"]) / 2);
            y = int(int(info["height"]) / 2);
            g.centrePaths(x, y);
    
    return pathGroups, info;

def saveSVG(file, path, info, groups, count):

    filename = path + file

    # save .svg file with SVG 1.1 prefixes

    print("Saving SVGs", count + (0 if (count==0) else 1), "-", count + len(groups));
    
    for i in range(0, len(groups)):
        svg = "".join([
            '<?xml version="1.0" encoding="utf-8"?>\n',
            '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n',
            '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="{0}px" y="{1}px" width="{2}px" height="{3}px" viewBox="{0} {1} {2} {3}">\n'.format(info["x"], info["y"], info["width"], info["height"]),
            "\n" + groups[i],
            '</svg>'
        ]);
        
        write_to = filename + getFileSuffix(i + count, ".svg");
        f = open(write_to, "w");
        f.write(svg);
        f.close();

def convertToImage(svgFileName, imgFileName, svgPath, imgPath, num, imageType):
    
    svgPath += svgFileName
    imgPath += imgFileName
    
    # convert .svg to .png files
    
    print ("Converting", num, "files");
    
    # inkscape -z --file="{0}" --export-png="{1}"
    
    for i in range(num):
        if (i % 5 == 0):
            print(floor(100 * i / num), "%");
        
        if imageType == '-png':
            input = svgPath + getFileSuffix(i, ".svg");
            output = imgPath + getFileSuffix(i, ".png");
            FNULL = open(os.devnull, 'w')
            subprocess.call('inkscape -z --file="{0}" --export-png="{1}"'.format(input, output), stdout=FNULL);
        else:
            url = svgPath + getFileSuffix(i, ".svg");
            write_to = imgPath + getFileSuffix(i, ".tiff");
            renderPM.drawToFile(svg2rlg(url), write_to, fmt="TIFF");
        
        #retcode = subprocess.call(['echo', 'foo'], stdout=FNULL, stderr=subprocess.STDOUT)
    
    print("100 %")
