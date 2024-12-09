import queue
import time
from pynput import keyboard
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

        running = True
        def on_press(key):
            nonlocal running  # Capture the local variable
            try:
                if key.char == 'x':  # Stop loop when 'x' is pressed
                    print("Key 'x' pressed. Stopping loop...")
                    running = False
                    return False
            except AttributeError:
                pass

        with keyboard.Listener(on_press=on_press) as listener:
            while unexploredNodeQueue.qsize() > 0 and running:
                time.sleep(0.1)
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

    def recordNode(self, node):

        with open("nodeNetworkRecord.txt", "a") as file:
            file.write(node.getSelfUrl + ":" + node.getConnections)

