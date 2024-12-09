import graphMaker

#the nesting of the classes goes as follows
#NodeNetwork > DirectoryNode > findSubdirectories(not a class)

#NodeNetwork is the overarching collection of Directory nodes, organized in a dictionary with their corresponding
#urls as keys. DirectoryNodes are the individual nodes that are representative of a single directory. Each
#DirectoryNode is capable of scrapping and getting all nodes of the same base URL using generateConnections(),
#and is initialized with an internal selfUrl variable. This functionality is enabled by findSubdirectories.py.


def main():
    graphMaker.interface()


if __name__ == "__main__":
    main()
