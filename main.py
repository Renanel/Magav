# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import requests
import timeit
import time
def lengthh(func,value):
    start_time= time.time()
    func(value)
    return ("--- %s seconds ---" % (time.time() - start_time))


def timing(func):
    t = timeit.timeit(lambda: func)
    return t


def renanel(name):
    print("hi")


if __name__ == '__main__':
    renanel('PyCharm')

response = requests.get("https://api.imgflip.com/get_memes")

file_dictionary = response.json()
print(file_dictionary)

new_dict = file_dictionary['data']['memes']
print(new_dict)


field_names = ['id', 'url', "width", 'height','common_color_rgb_1',
'common_color_rgb_2', 'common_color_rgb_3', 'common_color_rgb_4']

new_dict2 = []


def tzeva(image_url):
    from colorthief import ColorThief
    import urllib3
    address="pic1.jpg"
    http = urllib3.PoolManager()
    r = http.request('GET', image_url)
    x = r.data
    open(address ,'wb').write(x)
    color_thief = ColorThief(address)
    palette = color_thief.get_palette(color_count=4)
    return (palette)



for meme in new_dict:
    meme2 = {}
    for key in meme:
        if key in field_names:
            meme2[key] = meme[key]
        if key == 'url':
            url_pic = meme2.get(key)
            try:
                temp  =   tzeva(url_pic)
            except:
                print("This image isn't working: {0}/n".format(url_pic))
                continue
            meme2['common_color_rgb_1'] = temp[0]
            meme2['common_color_rgb_2'] = temp[1]
            meme2['common_color_rgb_3'] = temp[2]
            meme2['common_color_rgb_4'] = temp[3]
    new_dict2.append(meme2)


with open('renanel.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(new_dict2)

csvfile.close()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/

