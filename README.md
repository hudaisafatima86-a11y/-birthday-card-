import qrcode

def generate_qr():
    url = "https://hudaisafatima86-a11y.github.io/birthday-card/birthday_card.html"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save("birthday_qr.png")
    print("QR code saved as 'birthday_qr.png'. Scan it to access the card!")

if __name__ == "__main__":
    generate_qr()