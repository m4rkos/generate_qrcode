import qrcode
import io
import uuid


class Tools:

    base_url = "https://moow.com.br"


    def save_qrcode(self, value=base_url):
        img = qrcode.make(value)
        type(img)  # qrcode.image.pil.PilImage
        name = uuid.uuid4()
        img.save(f"./qr_codes/{name}.png")


    def generate_qrcode_custom(self, value=base_url):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(value)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")


    def show_qrcode(self, value=base_url):
        qr = qrcode.QRCode()
        qr.add_data(value)
        f = io.StringIO()
        qr.print_ascii(out=f)
        f.seek(0)
        print(f.read())