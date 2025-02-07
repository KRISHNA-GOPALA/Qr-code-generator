import qrcode
features = qrcode.QRCode(version=1,box_size=40,border=3)
a = input("Enter the URL or Message : ")
features.add_data(a)
features.make(fit=True)
generate_image = features.make_image(fill_color='black',back_color='white')
generate_image.save('image1.png')
print("The QR code is successfully generated")