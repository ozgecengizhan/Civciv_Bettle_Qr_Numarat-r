import qrcode

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("tel:+90##########")
qr.make(fit=True)