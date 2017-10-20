import roto_analyse
import roto_easing

def tweenFrames(a, b, steps, easingType, firstFrame):
    g = []
    steps -= 1
    
    a.resetSortedFlags()
    b.resetSortedFlags()
    a.nextFrame(b)
    b.nextFrame(a)
    
    for i in range(0 if firstFrame else 1, steps + 1):
        t = i / (steps * 1.0)
        str = ""
        ease = roto_easing.easing(t, easingType)
        
        # tween objects
        
        a.tweenFrame(ease)
        b.tweenFrame(1 - ease)
        
        # convert to output string
        
        str = roto_analyse.groupsToGroupString([a, b])
        g.append(str)
    
    return g