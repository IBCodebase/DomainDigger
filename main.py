import directoryNode
from nodeNetwork import NodeNetwork
from directoryNode import DirectoryNode
import findSubdirectories
import networkx as nx
import matplotlib.pyplot as plt
import random
import scipy

#the nesting of the classes goes as follows
#NodeNetwork > DirectoryNode > findSubdirectories(not a class)

#NodeNetwork is the overarching collection of Directory nodes, organized in a dictionary with their corresponding
#urls as keys. DirectoryNodes are the individual nodes that are representative of a single directory. Each
#DirectoryNode is capable of scrapping and getting all nodes of the same base URL using generateConnections(),
#and is initialized with an internal selfUrl variable. This functionality is enabled by findSubdirectories.py.

def interface():
    entrypoint = input("Please enter the entrypoint url you want to use:")
    nn = NodeNetwork()

    print("-----------------------------------------------------------------------")
    print("Now beginning the crawl, please be patient as this will take some time!")
    print("Each new node will be printed as it is processed")
    print("If you would like to stop the process mid-crawl, press x")
    print("Stopping the crawl mid-way will still allow for a partial map generation")
    print("-----------------------------------------------------------------------")

    nodeDict = nn.generateNetwork(entrypoint)
    print("\n")
    randomColor(nodeDict)

def randomColor(nodeDict):

    for node in nodeDict:
        nodeDict[node] = nodeDict[node].getConnections()

    G = nx.DiGraph()
    for node, neighbors in nodeDict.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    node_colors = {node: f"#{random.randint(0, 0xFFFFFF):06x}" for node in G.nodes}

    edge_colors = [node_colors[u] for u, v in G.edges()]

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, k = 2)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=50,
        node_color=list(node_colors.values()),
        font_size=10,
        font_weight='bold',
        edge_color=edge_colors,
        width=1,
        arrows=True
    )


    plt.title("Graph with Nodes and Edges Colored by Source Node")
    plt.show()

def colorBasedOnFrequency(nodeDict):
    node_colors = assignColors(nodeDict)

    for node in nodeDict:
        nodeDict[node] = nodeDict[node].getConnections()

    G = nx.DiGraph()

    for node, neighbors in nodeDict.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    edge_colors = []

    for u, v in G.edges():
        if u not in node_colors:
            edge_colors.append('#0000FF')
        else:
            edge_colors.append(node_colors[u])

    for node in G.nodes():
        if node not in node_colors:
            node_colors[node] = "#0000FF"

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=20,
        node_color=list(node_colors.values()),
        font_size=10,
        font_weight='bold',
        edge_color=edge_colors,
        width=.5,
        arrows=True
    )
    plt.title("Directed Graph with Edge Colors Based on Target Nodes")
    plt.show()

def countConnections(nodeDict):
    counterDict = nodeDict.copy()
    for node in nodeDict:
        for link in nodeDict[node].getConnections():
            #print(dict[node].getConnections())
            if counterDict.__contains__(link):

                if isinstance(counterDict[link], int):
                    counterDict[link] = counterDict[link] + 1
                else:
                    counterDict[link] = 1
    for obj in counterDict:
        if not isinstance(counterDict[obj], int):
            counterDict[obj] = 0
    return counterDict

def colorThresholdFullRange(nodeDict, threshold):
    for key in nodeDict:
        value = max(0, min(nodeDict[key], threshold))

        ratio = value / threshold

        red = int(255 * ratio)
        green = int(255 * (1 - ratio))
        blue = int(255 * (ratio / 2))

        alpha = int(255 * 0.5)

        nodeDict[key] = f"#{red:02X}{green:02X}{blue:02X}{alpha:02X}"
    return nodeDict

def highestValueDict(nodeDict):
    highestValue = -1;
    for url in nodeDict:
        print(nodeDict[url])
        if nodeDict[url] > highestValue:
            highestValue = nodeDict[url]
    return highestValue

def assignColors(nodeDict):
    countedConnections = countConnections(nodeDict)
    print(countedConnections)
    nodeDict = colorThresholdFullRange(countedConnections, highestValueDict(countedConnections))
    return nodeDict

def main():
    interface()


if __name__ == "__main__":
    main()
