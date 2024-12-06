import findSubdirectories

class DirectoryNode:
    def __init__(self, selfUrl):
        #selfUrl is the url of this node's website
        #connections is a list of subdirectories (other node) that this website is connected to
        self.selfUrl = selfUrl
        self.connections = []

    def getConnections(self):
        return self.connections

    def getSelfUrl(self):
        return self.selfUrl

    def generateConnections(self):
        self.connections = findSubdirectories.searchForDirectories(self.selfUrl)


