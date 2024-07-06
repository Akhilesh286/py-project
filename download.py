# <div class="favorites_book">
# <ul>
# <li class="dowloads"><a href="https://s3taku.com/download?id=OTAwODA=&amp;typesub=Gogoanime-DUB&amp;title=One+Piece+%28Dub%29+Episode+365" target="_blank"><i class="icongec-dowload"></i><span>Download</span></a></li>
# <li class="favorites"><i class="icongec-fa-heart"></i><span>Add to Favorites</span></li>
# </ul>
# </div>


# <a href="https://gredirect.info/download.php?url=aHR0cHM6LyURASDGHUSRFSJGYfdsffsderFStewthsfSFtrfteAdrefsdsdfwerFrefdsfrersfdsrfer36343534sdf9xZXc2eG8zN2JmLmFuZjU5OC5jb20vdXNlcjEzNDIvNWFiZWQ2NjkxYzk0NTlhNGRiMDI5MWNkNzlmZjc5MjYvRVAuMzY2LnYxLjcyMHAubXA0P3Rva2VuPXZ3WnhrWHZjZEZBVVZZM0xJaERxR0EmZXhwaXJlcz0xNzIwMjYyMzg3JmlkPTkwMDgx">Download
                        # (720P - mp4)</a>


import requests
from bs4 import BeautifulSoup


# url = 'https://ww8.gogoanimes.fi/one-piece-dub-episode-366'
def find_href (url):

    # URL of the webpage you want to scrape
    url = url
  
    # Send a GET request to fetch the HTML content
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # print(soup)

    # Find the element by its id
    element_with_id = soup.find_all("a")

    # Check if the element is found

    count = 0

    for i in element_with_id:
        target = i.get("target")
        if target == "_blank":
            if count == 9:
                href = i.get("href")
            count += 1

    return href

def main (count,start):
    count = count+1
    start = start
    href = []
    for i in range (1,count):
        url = f'https://ww8.gogoanimes.fi/one-piece-dub-episode-{start+i}'
        href.append(find_href(url))
    return href
