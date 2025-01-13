import qrcode
from PIL import Image

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("tel:+90##########")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

logo = Image.open("./bettle.png").resize((80, 80))
position = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
img.paste(logo, position)


img.save("qr_code.png")
img.save("qr_code_logolu.png")