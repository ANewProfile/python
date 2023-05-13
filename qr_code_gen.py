import qrcode
import qrcode.image.svg

link = input('Would link would you like to the QR code to go to? ')
file_name = input('What file do you want to save the image as? ')

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make(link, image_factory=factory)
svg_img.save(f'{file_name}.svg')