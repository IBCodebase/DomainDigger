import directoryNode
from nodeNetwork import NodeNetwork
from directoryNode import DirectoryNode
import findSubdirectories

#the nesting of the classes goes as follows
#NodeNetwork > DirectoryNode > findSubdirectories(not a class)

#NodeNetwork is the overall collection of Directory nodes, organized in a dictionary with their corresponding
#urls as keys. DirectoryNodes are the individual nodes that are representative of a single directory. Each
#DirectoryNode is capable of scrapping and getting all nodes of the same base URL using generateConnections(),
#and is initialized with an internal selfUrl variable. This functionality is enabled by findSubdirectories.py.

def main():
    nn = NodeNetwork()
    #print(nn.addNode("https://unity.com/"))
    dict = nn.generateNetwork("www.goodAndEthical.com")
    #print("-------------------------------------------------------------------------")
    for node in dict:
        print(node.getConnections)
    #print(findSubdirectories.searchForDirectories("https://unity.com/"))

if __name__ == "__main__":
    main()
