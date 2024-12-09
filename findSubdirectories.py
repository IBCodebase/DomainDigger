import requests
from bs4 import BeautifulSoup

def searchForDirectories(url):
    #this method begins the search for other subdirectories
    #serves as the entrypoint into the search
    response = requests.get(url)
    linkList = findUrlsContainingBaseUrl(response, findBaseUrl(url), url)
    return linkList

def extract_all_links(response, url):
    # Fetch the content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')

    links = set()  # Use a set to avoid duplicates


    for a_tag in soup.find_all('a', href=True):
        links.add(a_tag['href'])

    for form_tag in soup.find_all('form', action=True):
        links.add(form_tag['action'])

    for meta_tag in soup.find_all('meta', attrs={'http-equiv': 'refresh'}):
        content = meta_tag.get('content', '')
        if ';' in content:
            parts = content.split(';')
            for part in parts:
                if 'url=' in part:
                    links.add(part.split('=')[1].strip())

    base_tag = soup.find('base', href=True)
    if base_tag:
        links.add(base_tag['href'])

    for script_tag in soup.find_all('script'):
        script_content = script_tag.string or ''
        if 'location.href' in script_content:

            start = script_content.find("location.href")
            if start != -1:
                link_start = script_content.find('"', start)
                link_end = script_content.find('"', link_start + 1)
                if link_start != -1 and link_end != -1:
                    links.add(script_content[link_start + 1:link_end])

    # Convert relative URLs to absolute
    absolute_links = {requests.compat.urljoin(url, link) for link in links}

    return absolute_links



def findUrlsContainingBaseUrl(response, baseUrl, url):
    linkList = extract_all_links(response, url)
    baseList = []
    for link in linkList:
        if link.__contains__(baseUrl):
            baseList.append(link)
    return baseList

def findBaseUrl(url):
    if url.__contains__(".com"):
        return "https://" + (url.split(".com")[0].split("https://")[1] + ".com")
    if url.__contains__(".edu"):
        return "https://" + (url.split(".edu")[0].split("https://")[1] + ".edu")
    if url.__contains__(".gov"):
        print("WARNING - YOU ARE ABOUT TO CRAWL A GOVERNMENT SERVER - WARNING")
        if input("IF YOU WISH TO CONTINUE INPUT \'QTIP1580\'" == 'QTIP1580'):
            return "https://" + (url.split(".gov")[0].split("https://")[1] + ".gov")
        return "STOP"
    if url.__contains__(".org"):
        return "https://" + (url.split(".org")[0].split("https://")[1] + ".org")
    if url.__contains__(".net"):
        return "https://" + (url.split(".net")[0].split("https://")[1] + ".net")
    if url.__contains__(".biz"):
        return "https://" + (url.split(".biz")[0].split("https://")[1] + ".biz")
    if url.__contains__(".info"):
        return "https://" + (url.split(".info")[0].split("https://")[1] + ".info")
    return "obscure url high level domain --- add to code"

