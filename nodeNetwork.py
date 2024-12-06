import directoryNode
from directoryNode import DirectoryNode

class NodeNetwork:
    def __init__(self):
        #the node dictionary will be populated {url:directoryNode} for each corresponding node
        self.nodeDict = {}
        self.numberOfNodes = 0

    def getNodeDict(self):
        return self.nodeDict

    def getNumberOfNodes(self):
        return self.numberOfNodes

    def getSpecificNode(self, url):
        return self.nodeDict[url]

    def addNode(self, url):
        if not self.nodeDict.__contains__(url):
            self.nodeDict[url] = self.createDirectoryNode(url)
        

    def createDirectoryNode(self, url):
        newNode = DirectoryNode(url)
        newNode.generateConnections()

        return newNode

    def generateNetwork(self, entryNode):

