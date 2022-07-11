import csv
import requests
import shutil
import os.path
from multiprocessing import Process
from multi import insertcolor

response_API = requests.get('https://api.imgflip.com/get_memes')
dict = response_API.json()


only_memes = dict['data']['memes']


path = 'C:\\Networks\MAGAV\Pictures'
for meme in only_memes:

        image_url = meme['url']
        #filename = image_url.split("/")[-1]
        # למה זה עושה בעיה כשיש סימן שאלה בשם?
        filename = meme['name']
        #כי אי אפשר לכתוב קובץ שיש בו ,?,, לכן אצטרך למצוא דרך למחוק את סימן השאלה
        filename.replace('?','')
        r = requests.get(image_url, stream = True)
        r.raw.decodce_content = True
        temp = filename.replace('?', ' ')
        meme['name'] = temp
        with open(os.path.join(path, temp), 'wb') as f:
                shutil.copyfileobj(r.raw, f)
#עד כאן שמרתי את כל התמונות לפי השם שלהן
def insertcolor(meme):
    from colorthief import ColorThief
    address=('C:\\Networks\\MAGAV\\Pictures'+ '\\' + meme['name'])
    color_thief = ColorThief(address)
    palette = color_thief.get_palette(color_count=4)
    meme['common_color_rgb_1'] = palette[0]
    meme['common_color_rgb_2'] = palette[1]
    meme['common_color_rgb_3'] = palette[2]
    meme['common_color_rgb_4'] = palette[3]
#פונקציית העזר
if __name__ == '__main__':  # confirms that the code is under main function
    only_memes1 = dict['data']['memes']
    procs = []
    proc = Process(target=insertcolor)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    for meme in only_memes1:
        proc = Process(target=insertcolor, args=(meme))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()
#זה היה אמור לעבור על כל הממים עם הפונקציה שמכניסה את הנתונים של הצבעים לתוך המם באופן מקבילי, משום מה זה לא עובד

#for meme in only_memes:
 #       insertcolor(meme)

field_names = ['id', 'url', "width", 'height','common_color_rgb_1',
'common_color_rgb_2', 'common_color_rgb_3', 'common_color_rgb_4']
new_dict2 = []
for meme in only_memes:
        meme2 = {}
        for key in meme:
                if key in field_names:
                        meme2[key] = meme[key]
        new_dict2.append(meme2)

with open('new.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(new_dict2)

csvfile.close()
