from PIL import Image

# ASCII characters used to create the image
ASCII_CHARS = "@%#*+=-:. "

# Image to convert
while True:
    image_path = input("Enter the path to the image: ")
    try:
        image = Image.open(image_path)
    except FileNotFoundError as e:
        print("Image not found!")
        continue
    break

# Resize the image
while True:
    try:
        new_width = int(input("Final ASCII image width: "))
        if new_width < 100 or new_width > 1000:
            raise ValueError
    except ValueError:
        print("Le ficher doit être compri entre 100 et 1000")
        continue
    break
width, height = image.size
new_height = int(new_width * (height / width) * 0.4)
image = image.resize((new_width, new_height))

# Convert the image to grayscale
image = image.convert("L")

# Convert pixels to ASCII
pixels = image.getdata()
pixels_to_ascii = [ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255] for pixel in pixels]

# Format the ASCII image
ascii_art = ["".join(pixels_to_ascii[i:(i + new_width)]) for i in range(0, len(pixels_to_ascii), new_width)]
ascii_art = "\n".join(ascii_art)

# Save to a file
with open("art.txt", "w") as f:
    f.write(ascii_art)
print("ASCII file created")
