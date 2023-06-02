from rembg import remove
from PIL import Image

i = "icon.png"

output_path = "new_icon.png"

inp = Image.open(i)

output = remove(inp)
output.save(output_path)