from PIL import Image

# Caractères ASCII utilisés pour créer l'image
ASCII_CHARS = "@%#*+=-:. "

# Image à convertir
while True:
    image_path = input("Entrer le chemin de l'image: ")
    try:
        image = Image.open(image_path)
    except FileNotFoundError as e:
        print("L'image n'a pas été trouvée!")
        continue
    break

# Redimensionnement de l'image
while True:
    try:
        new_width = int(input("Largeur de l'image final en ASCII: "))
        if new_width < 100 or new_width > 1000:
            raise ValueError
    except ValueError:
        print("Le ficher doit être compri entre 100 et 1000")
        continue
    break
width, height = image.size
new_height = int(new_width * (height / width) * 0.4)
image = image.resize((new_width, new_height))

# Convertir l'image en niveau de gris
image = image.convert("L")

# Convertion des pixels en ASCII
pixels = image.getdata()
pixels_to_ascii = [ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255] for pixel in pixels]

# Mise en forme de l'image
ascii_art = ["".join(pixels_to_ascii[i:(i + new_width)]) for i in range(0, len(pixels_to_ascii), new_width)]
ascii_art = "\n".join(ascii_art)

# Sauvegarde dans un ficher
with open("art.txt", "w") as f:
    f.write(ascii_art)
print("Ficher ASCII créer")
