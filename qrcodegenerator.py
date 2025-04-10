import image
import qrcode
qr = qrcode.QRCode(
    version= 15,#15 means the hight number of the qr code high the number bigger the code image and complicated picture
    border= 10, #a size of box where the qr code  will be desplayed
    box_size=5 #it's the white part of the image -- border in all size with white color

)
data = 'https://www.youtube.com/@marufahmmedpilow399'
#if you want to write the normal text in the quotes

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = 'black', back_color = 'white')
img.save('text.png')