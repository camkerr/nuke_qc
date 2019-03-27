import os.path
import sys
filePath = sys.argv[1]
#Importing Nuke as a Python Module on Windows
sys.path.insert(0, "C:/Program Files/Nuke11.3v1/lib/site-packages/")
import nuke

#Functions

def getLastFrame(filePath):
    dirPath = filePath.rsplit("\\", 1)[0]
    array = nuke.getFileNameList(dirPath+"\\")
    print array
    for i in array:
        if ".tmp" in i:
            array.remove(i)
        elif ".mov" in i:
            array.remove(i)
        else:
            pass
    lastFrame = array[0].split("-")[-1]

    return int(lastFrame)

def samplePixelValues(readNode, lastFrame):
    corruptedFramesArray = []
    for i in range(1,lastFrame):
        nuke.frame(i)
        value = nuke.sample(readNode, 'red', 1, 1)
        if value == 0.0:
            corruptedFramesArray.append(i)
    return corruptedFramesArray

def writeWarningFile(corruptedFramesArray):
    savePath = "D:/quality_check/failed_qc_shots" #VFX Co-ordinator has this folder setup as a watch folder for notifications of shots that fail QC
    nameOfFile = filePath.split("\\")[-1]
    shotName = nameOfFile.split(".")[0]
    completePath = os.path.join(savePath, shotName+".txt")
    fileContents = "Corruption or Errors detected on frames: " + str(corruptedFramesArray)
    file = open(completePath, "a+")
    file.write(fileContents)
    file.close()
    pass


#Setup

if __name__ == "__main__":
    readNode = nuke.createNode("Read")
    readNode.knob("file").fromUserText(filePath)
    lastFrame = getLastFrame(filePath)
    readNode["last"].setValue(lastFrame)
    readNode["origlast"].setValue(lastFrame)
    if corruptedFramesArray:
        writeWarningFile(corruptedFramesArray)
