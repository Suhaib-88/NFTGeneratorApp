from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import os
import random

def resize_emojis(dirName):
    list_of_emojis=os.listdir(dirName)
    new_list_emojis=[]
    for i,j in enumerate(list_of_emojis):
        try:
            im = Image.open(f"{dirName}/{j}")

            resized_im = im.resize((320, 250))
            resized_im.save(f"{dirName}_resized/emoji_{i}.png")
            new_list_emojis.append(f"emoji_{i}.png")
        except:
            pass
    return new_list_emojis


def resize_background(dirName):
    list_of_bg=os.listdir(dirName)
    new_list_bg=[]
    for i,j in enumerate(list_of_bg):
        try:
            im = Image.open(f"{dirName}/{j}")
            resized_im = im.resize((320, 250))
            resized_im.save(f"{dirName}_resized/background_{i}.png")
            new_list_bg.append(f"background_{i}.png")
        except:
            pass
    return new_list_bg

emoji_list=resize_emojis(dirName='emoji')
bg_list=resize_background(dirName='background')

def overlay_pictures(emoji_list=emoji_list,bg_list=bg_list):    

    random_img=random.choice(emoji_list)
    random_bg=random.choice(bg_list)

    background = Image.open(f"background_resized/{random_bg}")
    overlay = Image.open(f"emoji_resized/{random_img}")  

    # Image1 = Image.open(img1)
    
    # make a copy the image so that
    # the original image does not get affected
    
    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")

    Image1copy = overlay.copy()
    Image2 = Image.open("accessories/hat.jpg")
    Image2=Image2.convert("RGBA")
    Image2copy = Image2.copy()
    
    Image3 = Image.open("accessories/shirt.jpg")
    Image3=Image3.convert("RGBA")
    Image3copy = Image3.copy()
    
    # paste image giving dimensions
    Image1copy.paste(Image2copy, (110, 10))
    Image1copy.paste(Image3copy, (38,202))


    new_img = Image.blend(background, Image1copy, 0.20)
    new_img.save("new.png","PNG")
    return new_img



def photo2pixelart(image, i_size):
    """
    image: path to image file
    i_size: size of the small image eg:(8,8)
    """
    #read file
    img=Image.open(image)
    
    # Add Text to an image
    I1 = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('K22 Xanthus.ttf', 50)                                                                        
    I1.text((10, 10), "N F T", font=myfont,fill =(120, 213,1))        

    #convert to small image
    small_img=img.resize(i_size,Image.BILINEAR)

    #resize to output size
    res=small_img.resize(img.size, Image.NEAREST)

    #Save output image
    filename=f'static/NFT_pixelated_{i_size[0]}x{i_size[1]}.png'
    res.save(filename)
