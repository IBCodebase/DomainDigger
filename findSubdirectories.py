
import requests
from bs4 import BeautifulSoup
from directoryNode import DirectoryNode
def entryPoint(url):
    #this method begins the search for other subdirectories
    #serves as the entrypoint into the search
    response = requests.get(url)
    linkList = findUrlsContainingBaseUrl(response.text, findBaseUrl(url))
    for link in linkList:
        print(link)


def createDirectoryNode(url):
    directoryNode = createDirectoryNode(url)


def findUrlsContainingBaseUrl(html, baseUrl):
    soup = BeautifulSoup(html, 'html.parser')
    linkList = []
    #not to be confused with a linkedList!

    for link in soup.find_all('a', href=True):
        href = link.get('href')
        if href:
            #print(href)
            #print(baseUrl)
            if href[0:30].__contains__(baseUrl):
                if href[0] == '/' and href[1] == '/':
                    linkList.append("https://" + href)
                else:
                    linkList.append(href)
    return linkList
def findBaseUrl(url):
    return url.split(".com")[0].split("https://")[1] + ".com"

