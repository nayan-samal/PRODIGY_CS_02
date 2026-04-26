# PRODIGY_CS_02
Image encryption and decryption tool using pixel manipulation in Python.

# Image Encryption Tool - Task 02

This project implements a simple image encryption and decryption tool using pixel manipulation in Python. It modifies pixel values using a key to transform the image and reverses the process to restore the original image.

## Features
- Encrypt images using a key-based pixel shift
- Decrypt images using the same key
- Works with RGB images
- Simple and reversible approach

## How It Works
Each pixel in the image has RGB values (0–255).  
Encryption adds a key value to each channel, while decryption subtracts the same key.

## How to Run

1. Install required library:
   ```bash
   pip install pillow
