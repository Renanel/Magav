import requests
import json
import shutil

response_API = requests.get('https://api.imgflip.com/get_memes')
dict = response_API.json()
print(dict)

only_memes = dict['data']['memes']
print (only_memes)
path = 'C:\\Networks\MAGAV\Pictures'

for meme in only_memes:

        image_url = meme['url']
        
        r = requests.get(image_url, stream = True)
        r.raw.decodce_content = True
        temp = filename.replace('?', ' ')
        meme['name'] = temp
        with open(os.path.join(path, temp), 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            
