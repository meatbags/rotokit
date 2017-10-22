import roto_tween
import roto_file
import roto_window
import roto_settings
import sys, os, os.path

parentDir = os.path.abspath(__file__ + '\..\..')

try:
    inputFile = parentDir + '\\input\\' + sys.argv[1]
    outputDir = parentDir + '\\output\\' + sys.argv[2]
    outputPath = outputDir + '\svg\\'
    imagePath = outputDir + '\img\\'
    frames = int(sys.argv[3]) + 1
    fps = int(sys.argv[4])
    imageType = '-png' if '-png' in sys.argv else '-tiff'
    
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)
except:
    print('Error: Incorrect input')
    sys.exit()

groups, info = roto_file.openSVG(inputFile, roto_settings.SETTINGS_CENTRE);
count = 0;
settings = [item for item in dir(roto_settings) if not item.startswith("__") and "SETTINGS" not in item];

# print out settings

print("\n_Output Mode_")
print("Steps:{0} Fps:{1} Size:{2}x{3} Easing:{4} CentreMode:{5}".format(frames - 1, fps, info["width"], info["height"], roto_settings.SETTINGS_EASING, roto_settings.SETTINGS_CENTRE != False));
print("\n_Analysis Settings_")

for s in settings:
    evals = eval("roto_settings." + s);
    if evals != 0 and evals != False:
        print(s, '...', evals)

print("\nAnalysing...");

for i in range(0, len(groups) - 1):
    a = groups[i]
    b = groups[i + 1]
    g = roto_tween.tweenFrames(a, b, frames, roto_settings.SETTINGS_EASING, firstFrame=(i==0))
    roto_file.saveSVG('svg', outputPath, info, g, count)
    count += frames - (0 if (i==0) else 1)
    
print(outputPath, imagePath);

roto_file.convertToImage('svg', 'img', outputPath, imagePath, count, imageType);
roto_window.display('img', imagePath, count, fps, imageType)

