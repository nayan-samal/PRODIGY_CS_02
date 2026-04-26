from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save(output_path)
    print("Encrypted image saved as", output_path)

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save(output_path)
    print("Decrypted image saved as", output_path)

choice = input("Encrypt (E) or Decrypt (D): ").lower()
input_path = input("Enter input image path: ")
output_path = input("Enter output image path: ")
key = int(input("Enter key (0-255): "))

if choice == 'e':
    encrypt_image(input_path, output_path, key)
elif choice == 'd':
    decrypt_image(input_path, output_path, key)
else:
    print("Invalid choice")