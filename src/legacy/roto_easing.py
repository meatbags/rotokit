
def easing(t, type):
    if type == False or type == "ease-linear":
        return t;
    
    if type == "ease-in-and-out":
        return 2 * t * t if t < .5 else -1 + (4 - 2 * t) * t;
    
    if type == "ease-in":
        return t * t;
    
    if type == "ease-out":
        return t * (2 - t);
    
    if type == "ease-centre":
        if t < 0.5:
            f = 0.5 - t;
            return 0.5 - (2 * f * f);
        else:
            f = 0.5 + 1 - t;
            return 0.5 + 1 - (-1 + (4 - 2 * f) * f);
    
    if type == "ease-blend":
        f = 0;
        if t < 0.5:
            f = 0.5 - t;
            f = 0.5 - (2 * f * f);
        else:
            f = 0.5 + 1 - t;
            f = 0.5 + 1 - (-1 + (4 - 2 * f) * f);
        return (t * 0.4) + (f * 0.6);
        
    if type == "ease-blend-2":
        f = 0;
        if t < 0.5:
            f = 0.5 - t;
            f = 0.5 - (2 * f * f);
        else:
            f = 0.5 + 1 - t;
            f = 0.5 + 1 - (-1 + (4 - 2 * f) * f);
        return (t * 0.75) + (f * 0.25);