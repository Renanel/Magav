import requests
import json
import shutil

response_API = requests.get('https://api.imgflip.com/get_memes')
dict = response_API.json()
print(dict)

only_memes = dict['data']['memes']
print (only_memes)

for meme in only_memes:

        image_url = meme['url']
        filename = image_url.split("/")[-1]
        filename.replace('?',' ')
        r = requests.get(image_url, stream = True)
        r.raw.decodce_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

            
