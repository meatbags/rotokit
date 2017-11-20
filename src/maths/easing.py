from src.config import Config

def applyEasing(easing, value):
    if easing == Config['Core']['Easing']['Linear']:
        return value

    elif easing == Config['Core']['Easing']['Out']:
        if value < 0:
            value += 1
        return value * value

    elif easing == Config['Core']['Easing']['In']:
        if value < 0:
            value += 1
        out = value * value
        return value + (value - out)

    elif easing == Config['Core']['Easing']['InAndOut']:
        if value < 0:
            value += 1
        return value

    elif easing == Config['Core']['Easing']['Centre']:
        return value

    elif easing == Config['Core']['Easing']['Soften']:
        return value

    return value
