from class_tools import Tools


a = Tools()

print("Let's to generate the QR Code !!\n\n")
value = input("text or link: ")

if value == "":
    value = None

print(f"\n{value}\n")

a.save_qrcode(value)
a.show_qrcode(value)