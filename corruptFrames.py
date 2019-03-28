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
    curveToolNode = nuke.createNode("CurveTool")
    curveToolNode["channels"].setValue("red")
    curveToolNode["ROI"].setValue([0,0,readNode.width(),readNode.height()])
    curveToolNode.setInput(0, readNode)
    return curveToolNode

def checkPixelValue(curveToolNode, lastFrame):
    duplicatedFramesArray = []
    for i in range(1,lastFrame):
        value = curveToolNode["intensitydata"].isKeyAt(i)
        if value == False:
            duplicatedFramesArray.append(i)
    return duplicatedFramesArray

def writeWarningFile(duplicatedFramesArray):
    savePath = "D:\\quality_check\\failed_qc_shots" #VFX Co-ordinator has this folder setup as a watch folder for notifications of shots that fail QC
    nameOfFile = filePath.split("\\")[-1]
    shotName = nameOfFile.split(".")[0]
    completePath = os.path.join(savePath, shotName+".txt")
    fileContents = "Corrupt Frames detected on frames: " + str(duplicatedFramesArray)
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
    curveToolNode = createNodes(readNode)
    nuke.execute(curveToolNode, 1, lastFrame)
    duplicatedFramesArray = checkPixelValue(curveToolNode, lastFrame)
    if duplicatedFramesArray:
        writeWarningFile(duplicatedFramesArray)
