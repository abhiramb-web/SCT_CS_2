from PIL import Image
import os

# ------------------------
# Encrypt Image
# ------------------------

image = Image.open("images/sample.jpg")

width, height = image.size

encrypted = image.copy()

for x in range(width):
    for y in range(height):

        r, g, b = image.getpixel((x, y))

        r = (r + 50) % 256
        g = (g + 50) % 256
        b = (b + 50) % 256

        encrypted.putpixel((x, y), (r, g, b))

os.makedirs("encrypted", exist_ok=True)
encrypted.save("encrypted/encrypted_image.png")

print("Image encrypted successfully!")

# ------------------------
# Decrypt Image
# ------------------------

encrypted_image = Image.open("encrypted/encrypted_image.png")

decrypted = encrypted_image.copy()

for x in range(width):
    for y in range(height):

        r, g, b = encrypted_image.getpixel((x, y))

        r = (r - 50) % 256
        g = (g - 50) % 256
        b = (b - 50) % 256

        decrypted.putpixel((x, y), (r, g, b))

os.makedirs("decrypted", exist_ok=True)
decrypted.save("decrypted/decrypted_image.png")

print("Image decrypted successfully!")