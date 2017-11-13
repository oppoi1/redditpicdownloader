#! python3
# img download script

import requests, os, bs4, time

url = 'http://imgur.com/r/aww'          # starting url

try:
    os.chdir('C://vaio//downloads//')
except:
    os.makedirs('C://vaio//downloads//')
    
os.makedirs('aww', exist_ok=True)       # store comics in folder


while not url.endswith('#'):
    # TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # TODO: Find the URL of the comic image.
    try:
        for picElem in soup.select('.image-list-link img'):
            picURL = 'http:' + picElem.get('src')
            picURL = picURL[:-5]
            picURL = picURL + '.jpg'
            # Download the image.
            print('Downloading image %s...' % (picURL))
            res = requests.get(picURL)
            res.raise_for_status()

            # TODO: Save the image to the folder.
            imageFile = open(os.path.join('test', os.path.basename(picURL)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
    except:
            imageFile = open(os.path.join('test', os.path.basename(picURL)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

print('Done.')


