from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global img
        img = Image.open(file_path)
        img.show()

def save_image(image, file_path):
    image.save(file_path)
    messagebox.showinfo("Image Saved", f"Image saved at {file_path}")

def encrypt_image():
    key = int(key_entry.get())
    if 0 <= key <= 255:
        encrypted_img = pixel_manipulation(img, key)
        encrypted_img.show()
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if save_path:
            save_image(encrypted_img, save_path)
    else:
        messagebox.showerror("Invalid Key", "Please enter a key between 0 and 255.")

def decrypt_image():
    key = int(key_entry.get())
    if 0 <= key <= 255:
        decrypted_img = pixel_manipulation(img, key)
        decrypted_img.show()
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if save_path:
            save_image(decrypted_img, save_path)
    else:
        messagebox.showerror("Invalid Key", "Please enter a key between 0 and 255.")

def pixel_manipulation(image, key):
    width, height = image.size
    pixels = list(image.getdata())
    new_pixels = [(r ^ key, g ^ key, b ^ key) for (r, g, b) in pixels]
    new_image = Image.new("RGB", (width, height))
    new_image.putdata(new_pixels)
    return new_image

app = tk.Tk()
app.title("Simple Image Encryption Tool")

open_button = tk.Button(app, text="Open Image", command=open_image)
open_button.pack()

tk.Label(app, text="Encryption/Decryption Key (integer):").pack()
key_entry = tk.Entry(app)
key_entry.pack()

encrypt_button = tk.Button(app, text="Encrypt Image", command=encrypt_image)
encrypt_button.pack()

decrypt_button = tk.Button(app, text="Decrypt Image", command=decrypt_image)
decrypt_button.pack()

app.mainloop()
