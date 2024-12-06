import directoryNode
from nodeNetwork import NodeNetwork
from directoryNode import DirectoryNode

#the nesting of the classes goes as follows
#NodeNetwork > DirectoryNode > findSubdirectories(not a class)

#NodeNetwork is the overall collection of Directory nodes, organized in a dictionary with their corresponding
#urls as keys. DirectoryNodes are the individual nodes that are representative of a single directory. Each
#DirectoryNode is capable of scrapping and getting all nodes of the same base URL using generateConnections(),
#and is initialized with an internal selfUrl variable. This functionality is enabled by findSubdirectories.py.

def main():
    nn = NodeNetwork()
    nn.addNode("https://blog.hubspot.com/marketing")
    nodeDict = nn.getNodeDict()
    for node in nodeDict:
        print(nodeDict[node].getConnections())


if __name__ == "__main__":
    main()
