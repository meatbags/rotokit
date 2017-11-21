from src.config import Config

def easeInAndOut(value):
    if value < 0.5:
        return (value * 2) ** 2 * 0.5
    else:
        return value + ((value - 0.5) - ((value - 0.5) * 2) ** 2 * 0.5)

def applyEasing(easing, value):
    if easing == Config['Core']['Easing']['Linear']:
        if value < 0:
            value += 1
        return value

    elif easing == Config['Core']['Easing']['Out']:
        if value < 0:
            value += 1
        return value ** 2

    elif easing == Config['Core']['Easing']['In']:
        if value < 0:
            value += 1
        out = value ** 2
        return value + (value - out)

    elif easing == Config['Core']['Easing']['InAndOut']:
        if value < 0:
            value += 1
        return easeInAndOut(value)

    elif easing == Config['Core']['Easing']['Centre']:
        if value < 0:
            value += 1
        return value + (value - easeInAndOut(value))

    elif easing == Config['Core']['Easing']['Soften']:
        if value < 0:
            value += 1
        inAndOut = easeInAndOut(value)
        return (value + inAndOut) * 0.5

    return value
