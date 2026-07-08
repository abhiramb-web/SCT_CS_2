import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import random
import os

# =====================================
# Global Variables
# =====================================

KEY = 122

image_path = ""

encrypted_image = None
decrypted_image = None

# =====================================
# Generate Random Keystream
# =====================================

def generate_key_stream(length):

    rng = random.Random(KEY)

    return [
        (
            rng.randint(0,255),
            rng.randint(0,255),
            rng.randint(0,255)
        )
        for _ in range(length)
    ]


# =====================================
# Encrypt / Decrypt Pixels
# =====================================

def process_pixels(pixels):

    key_stream = generate_key_stream(len(pixels))

    result = []

    for (r,g,b),(kr,kg,kb) in zip(pixels,key_stream):

        result.append(

            (
                r ^ kr,
                g ^ kg,
                b ^ kb
            )

        )

    return result


# =====================================
# Browse Image
# =====================================

def browse_image():

    global image_path

    image_path = filedialog.askopenfilename(

        title="Select Image",

        filetypes=[

            ("Image Files","*.png *.jpg *.jpeg *.bmp")

        ]

    )

    if image_path:

        file_label.config(

            text=os.path.basename(image_path)

        )

        status_label.config(

            text="Image Selected",

            fg="lightgreen"

        )
    # =====================================
# Encrypt Image
# =====================================

def encrypt_image():

    global encrypted_image

    if image_path == "":
        messagebox.showerror(
            "Error",
            "Please select an image first!"
        )
        return

    try:

        image = Image.open(image_path).convert("RGB")

        width, height = image.size

        pixels = list(image.getdata())

        encrypted_pixels = process_pixels(pixels)

        encrypted_image = Image.new("RGB", (width, height))
        encrypted_image.putdata(encrypted_pixels)

        status_label.config(
            text="Encryption Successful",
            fg="lightgreen"
        )

        messagebox.showinfo(
            "Success",
            "Image encrypted successfully!\n\nClick 'Download Encrypted' to save it."
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e))


# =====================================
# Decrypt Image
# =====================================

def decrypt_image():

    global decrypted_image

    if image_path == "":
        messagebox.showerror(
            "Error",
            "Please select an encrypted image first!"
        )
        return

    try:

        image = Image.open(image_path).convert("RGB")

        width, height = image.size

        pixels = list(image.getdata())

        decrypted_pixels = process_pixels(pixels)

        decrypted_image = Image.new("RGB", (width, height))
        decrypted_image.putdata(decrypted_pixels)

        status_label.config(
            text="Decryption Successful",
            fg="cyan"
        )

        messagebox.showinfo(
            "Success",
            "Image decrypted successfully!\n\nClick 'Download Decrypted' to save it."
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e))


# =====================================
# Download Encrypted
# =====================================

def download_encrypted():

    if encrypted_image is None:
        messagebox.showerror(
            "Error",
            "Encrypt an image first!"
        )
        return

    save_path = filedialog.asksaveasfilename(
        title="Save Encrypted Image",
        defaultextension=".png",
        initialfile="encrypted_image.png",
        filetypes=[
            ("PNG Image","*.png")
        ]
    )

    if save_path:

        encrypted_image.save(save_path)

        status_label.config(
            text="Encrypted Image Saved",
            fg="lightgreen"
        )


# =====================================
# Download Decrypted
# =====================================

def download_decrypted():

    if decrypted_image is None:
        messagebox.showerror(
            "Error",
            "Decrypt an image first!"
        )
        return

    save_path = filedialog.asksaveasfilename(
        title="Save Decrypted Image",
        defaultextension=".png",
        initialfile="decrypted_image.png",
        filetypes=[
            ("PNG Image","*.png")
        ]
    )

    if save_path:

        decrypted_image.save(save_path)

        status_label.config(
            text="Decrypted Image Saved",
            fg="cyan"
        )
# =====================================
# Clear
# =====================================

def clear():

    global image_path
    global encrypted_image
    global decrypted_image

    image_path = ""
    encrypted_image = None
    decrypted_image = None

    file_label.config(
        text="No image selected"
    )

    status_label.config(
        text="Ready",
        fg="white"
    )


# =====================================
# About
# =====================================

def about():

    messagebox.showinfo(
        "About",
        "Image Encryption Tool\n\n"
        "SkillCraft Technology Internship\n"
        "Task 2\n\n"
        "Algorithm:\n"
        "XOR Stream Cipher\n\n"
        "Developed by:\n"
        "B Abhiram"
    )


# =====================================
# GUI
# =====================================

window = tk.Tk()

window.title("Image Encryption Tool")

window.geometry("760x520")

window.configure(bg="#1E1E1E")

window.resizable(False, False)

# ---------------- Title ----------------

title = tk.Label(
    window,
    text="🔐 Image Encryption Tool",
    font=("Segoe UI",24,"bold"),
    bg="#1E1E1E",
    fg="white"
)

title.pack(pady=20)

# ---------------- Browse ----------------

browse_btn = tk.Button(
    window,
    text="Browse Image",
    width=22,
    bg="#0D6EFD",
    fg="white",
    font=("Segoe UI",11,"bold"),
    command=browse_image
)

browse_btn.pack()

# ---------------- Selected File ----------------

file_label = tk.Label(
    window,
    text="No image selected",
    bg="#1E1E1E",
    fg="white",
    font=("Segoe UI",11)
)

file_label.pack(pady=15)

# ---------------- Buttons ----------------

button_frame = tk.Frame(
    window,
    bg="#1E1E1E"
)

button_frame.pack(pady=15)

encrypt_btn = tk.Button(
    button_frame,
    text="Encrypt",
    width=14,
    bg="green",
    fg="white",
    font=("Segoe UI",10,"bold"),
    command=encrypt_image
)

encrypt_btn.grid(row=0,column=0,padx=10,pady=10)

decrypt_btn = tk.Button(
    button_frame,
    text="Decrypt",
    width=14,
    bg="red",
    fg="white",
    font=("Segoe UI",10,"bold"),
    command=decrypt_image
)

decrypt_btn.grid(row=0,column=1,padx=10,pady=10)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    width=14,
    font=("Segoe UI",10,"bold"),
    command=clear
)

clear_btn.grid(row=0,column=2,padx=10,pady=10)

about_btn = tk.Button(
    button_frame,
    text="About",
    width=14,
    bg="#0D6EFD",
    fg="white",
    font=("Segoe UI",10,"bold"),
    command=about
)

about_btn.grid(row=0,column=3,padx=10,pady=10)

# ---------------- Download ----------------

download_frame = tk.Frame(
    window,
    bg="#1E1E1E"
)

download_frame.pack(pady=15)

download_encrypt = tk.Button(
    download_frame,
    text="Download Encrypted",
    width=22,
    bg="#198754",
    fg="white",
    font=("Segoe UI",10,"bold"),
    command=download_encrypted
)

download_encrypt.grid(row=0,column=0,padx=10)

download_decrypt = tk.Button(
    download_frame,
    text="Download Decrypted",
    width=22,
    bg="#DC3545",
    fg="white",
    font=("Segoe UI",10,"bold"),
    command=download_decrypted
)

download_decrypt.grid(row=0,column=1,padx=10)

# ---------------- Status ----------------

status_title = tk.Label(
    window,
    text="Status",
    font=("Segoe UI",13,"bold"),
    bg="#1E1E1E",
    fg="white"
)

status_title.pack(pady=(20,5))

status_label = tk.Label(
    window,
    text="Ready",
    font=("Segoe UI",12),
    bg="#1E1E1E",
    fg="white"
)

status_label.pack()

# ---------------- Footer ----------------

footer = tk.Label(
    window,
    text="Developed by B Abhiram | SkillCraft Technology Internship Task 2",
    bg="#1E1E1E",
    fg="gray",
    font=("Segoe UI",9)
)

footer.pack(side="bottom",pady=10)

window.mainloop()