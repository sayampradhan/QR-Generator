# import neccessary libraries
import qrcode as qr
from PIL import Image

# main qr content input from the user
data = input("Enter some data: ")

# for qr colour setting
y_colour = input("Do you want to add colour? (y/n)\n")

if y_colour.lower() == 'y':
    colour = input("Write the colour: ")

else:
    colour = 'black'

# features of qr
features = qr.QRCode(version=1, box_size=50, border=4)
features.add_data(f'{data}')
features.make(fit=True)

# qr image generation
generate_image = features.make_image(
    fill_color=f"{colour}", back_color="white")

# name of the file
name = input("Write the name of the qr image you want to save: ")

# generation of image
try:
    generate_image.save(f'{name}.png')
    print("successfully created....")

except:
    print("Ummmm.... Something gone wrong...!!")

# opening the qr file
qr_image = Image.open(f'{name}.png', 'r')
qr_image.show()
