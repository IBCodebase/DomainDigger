import queue
import time

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
            return self.nodeDict[url].getConnections()
        return None

    def createDirectoryNode(self, url):
        newNode = DirectoryNode(url)
        newNode.generateConnections()

        return newNode

    def generateNetwork(self, entryNode):
        unexploredNodeQueue = queue.Queue()
        addList = self.addNode(entryNode)
        for url in addList:
            unexploredNodeQueue.put(url)

        while unexploredNodeQueue.qsize() > 0:
            time.sleep(.25)
            try:
                newAdd = unexploredNodeQueue.get()
                print(newAdd)
                addList = self.addNode(newAdd)
                for url in addList:
                    if not self.nodeDict.__contains__(url):
                        unexploredNodeQueue.put(url)


            except Exception as e:
                print(f"whoopsy: {e}")
        return self.nodeDict