# import neccessary libraries
import qrcode as qr

# main qr content input from the user
data = input("Enter some data: ")

# for qr colour setting
y_colour = input("Do you want to add colour? (y/n)\n")

if y_colour.lower() == 'y':
    colour = input("Write the colour: ")

try:
    # features of QR
    features = qr.QRCode(version=1, box_size=20, border=4)
    features.add_data(f'{data}')
    features.make(fit=True)

except ValueError:
    print("Invalid input....")

except:
    print("Ummmm... Some Error Occurred...")

# qr image generation
    generate_image = features.make_image(
        fill_color=f"{colour}", back_color="white")

# name of the file
name = input("Write the name of the qr image you want to save: ")

try:
    generate_image.save(f'{name}.png')
    print("successfully created....")

except:
    print("Ummmm.... Some error occurred while generating QR...!!")
