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

def createNodes(readNode):
    timeOffsetNode = nuke.createNode("TimeOffset")
    timeOffsetNode["time_offset"].setValue(-1)
    timeOffsetNode.setInput(0, readNode)
    differenceNode = nuke.createNode("Difference")
    differenceNode.setInput(0, readNode)
    differenceNode.setInput(1, timeOffsetNode)
    curveToolNode = nuke.createNode("CurveTool")
    curveToolNode["channels"].setValue("alpha")
    curveToolNode["ROI"].setValue([0,0,readNode.width(),readNode.height()])
    curveToolNode.setInput(0, differenceNode)
    return curveToolNode

def checkDifferenceValues(curveToolNode, lastFrame):
    duplicatedFramesArray = []
    for i in range(1,lastFrame):
        value = curveToolNode["intensitydata"].getValueAt(i)[-1]
        if value == 0.0:
            duplicatedFramesArray.append(i)
    return duplicatedFramesArray

def writeWarningFile(duplicatedFramesArray):
    savePath = "D:/quality_check/failed_qc_shots" #VFX Co-ordinator has this folder setup as a watch folder for notifications of shots that fail QC
    nameOfFile = filePath.split("\\")[-1]
    shotName = nameOfFile.split(".")[0]
    completePath = os.path.join(savePath, shotName+".txt")
    fileContents = "Duplicate Frames detected on frames: " + str(duplicatedFramesArray)
    file = open(completePath, "w+")
    file.write(fileContents)
    file.close()
    pass


#Setup

if __name__ == "__main__":
    readNode = nuke.createNode("Read")
    readNode.knob("file").fromUserText(filePath)
    readNode["colorspace"].setValue("AlexaV3LogC")
    lastFrame = getLastFrame(filePath)
    readNode["last"].setValue(lastFrame)
    readNode["origlast"].setValue(lastFrame)
    curveToolNode = createNodes(readNode)
    nuke.execute(curveToolNode, 1, lastFrame)
    duplicatedFramesArray = checkDifferenceValues(curveToolNode, lastFrame)
    if duplicatedFramesArray:
        writeWarningFile(duplicatedFramesArray)
