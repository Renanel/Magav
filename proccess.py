# אני מעבד כאן את כל התמונות, מקבל מעכך ממים ומחזיר מערך של הצבעים
# לכל הפוציה תשלח כל מם מהמערך לונקציית עזר שמוציאה םלטה אחת
from multiprocessing import Pool
import requests
import shutil
import os.path
import csv

def load (url):
    response_API = requests.get(url)
    dict = response_API.json()
    only_memes = dict['data']['memes']
    path = 'C:\\Networks\MAGAV\Pictures'
    for meme in only_memes:
        image_url = meme['url']
        filename = meme['name']
        filename.replace('?', '')
        r = requests.get(image_url, stream=True)
        r.raw.decodce_content = True
        temp = filename.replace('?', ' ')
        meme['name'] = temp
        with open(os.path.join(path, temp), 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return only_memes

def insertcolorv2(meme):
    from colorthief import ColorThief
    address=('C:\\Networks\\MAGAV\\Pictures'+ '\\' + meme['name'])
    color_thief = ColorThief(address)
    try:
        palette = color_thief.get_palette(color_count=4)
        return palette
    except:
        print("This image isn't working: {0}/n".format(meme['name']))
        palette = [-1, -1, -1, -1]
        return palette

only_memes = load('https://api.imgflip.com/get_memes')
for meme in only_memes:
    meme['common_color_rgb_1'] = 1
    meme['common_color_rgb_2'] = 1
    meme['common_color_rgb_3'] = 1
    meme['common_color_rgb_4'] = 1


if __name__ == '__main__':
    p = Pool(2)
    result = p.map(insertcolorv2, only_memes)
    p.close()
    p.join()
    index = 0
    for palette in result:
        only_memes[index]['common_color_rgb_1'] = palette[0]
        only_memes[index]['common_color_rgb_2'] = palette[1]
        only_memes[index]['common_color_rgb_3'] = palette[2]
        only_memes[index]['common_color_rgb_4'] = palette[3]
        index = index + 1

field_names = ['id', 'name', 'url', "width", 'height', 'box_count', 'common_color_rgb_1','common_color_rgb_2', 'common_color_rgb_3', 'common_color_rgb_4']
with open('new3.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(only_memes)

csvfile.close()

