# def imageFromWeb(url):
#     from io import BytesIO

#     import requests

#     response = requests.get(url)  
#     print(response)
#     # https://c.ndtvimg.com/2020-05/5mk12sl_football-generic-afp_625x300_06_May_20.jpg
#     # https://i.imgur.com/IyC9C8m.jpeg
#     return BytesIO(response.content) 


# def imageFromWeb2(url):
#     import urllib.request
#     from PIL import Image
    
#     urllib.request.urlretrieve(url,'filename.jpg')
#     img = Image.open('filename.jpg')
#     return img



# from PIL import Image
# # img = Image.open('G:\ProjectWorkHere\Projects_MK\#2-Docs2PDF\logo.png')
# img = Image.open('G:\ProjectWorkHere\Projects_MK\#2-Docs2PDF\logo.png')
# img2 = imageFromWeb2('https://i.imgur.com/eQ2UNSI.jpeg')

# img = img.resize((300, 300), Image.ANTIALIAS)
# img2 = img2.resize((1440, 900), Image.ANTIALIAS)
# img_w, img_h = img.size
# img2_w, img2_h = img2.size

# # background = Image.open('G:\ProjectWorkHere\Projects_MK\#2-Docs2PDF\index2.jpg', 'r')
# # background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
# # bg_w, bg_h = background.size
# offset = ((img2_w - img_w) // 2, (img2_h - img_h) // 2)
# img2.paste(img, offset,img)
# # img2.save('out.png')
# img2.show()

from PIL import Image

def add_play_button(back,button):
    background = Image.open(back)
    button = Image.open(button)

    button = button.resize((300, 300), Image.ANTIALIAS)
    background = background.resize((1440, 900), Image.ANTIALIAS)
    background_w, background_h = background.size
    button_w, button_h = button.size

    offset = (( background_w - button_w ) // 2, (background_h - button_h  ) // 2)
    background.paste(button, offset,button)
    background.save('edited.jpg')


add_play_button('images/index2.jpg','images/logo.png')

# This works
# from PIL import Image
# img = Image.open('G:\ProjectWorkHere\Projects_MK\#2-Docs2PDF\logo.png')
# img2 = Image.open('G:\ProjectWorkHere\Projects_MK\#2-Docs2PDF\index2.jpg')
# img = img.resize((300, 300), Image.ANTIALIAS)
# img2 = img2.resize((1440, 900), Image.ANTIALIAS)
# img_w, img_h = img.size
# img2_w, img2_h = img2.size

# # background = Image.open('G:\ProjectWorkHere\Projects_MK\#2-Docs2PDF\index2.jpg', 'r')
# # background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
# # bg_w, bg_h = background.size
# offset = ((img2_w - img_w) // 2, (img2_h - img_h) // 2)
# img2.paste(img, offset,img)
# # img2.save('out.png')
# img2.show()





# from PIL import Image
# img = Image.open('G:\ProjectWorkHere\Projects_MK\#2-Docs2PDF\index.jpg', 'r')
# img = Image.open('G:\ProjectWorkHere\Projects_MK\#2-Docs2PDF\index.jpg', 'r')
# img_w, img_h = img.size
# # background = Image.open('G:\ProjectWorkHere\Projects_MK\#2-Docs2PDF\index2.jpg', 'r')
# background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
# bg_w, bg_h = background.size
# offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
# background.paste(img, offset)
# background.save('out.png')