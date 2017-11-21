
def interpolatePaths(frame, time):
    for layer in frame.layers:
        for path in layer.paths:
            path.setTween(time)
