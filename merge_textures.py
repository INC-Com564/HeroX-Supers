from PIL import Image

# Load all textures
wingpack = Image.open('addonpacks/NexGEN26/assets/techpowers/textures/item/wingpack.png').convert('RGBA')
texture = Image.open('addonpacks/NexGEN26/assets/techpowers/textures/item/texture.png').convert('RGBA')
texture_2 = Image.open('addonpacks/NexGEN26/assets/techpowers/textures/item/texture_2.png').convert('RGBA').resize((32, 32), Image.NEAREST)
texture_3 = Image.open('addonpacks/NexGEN26/assets/techpowers/textures/item/texture_3.png').convert('RGBA').resize((32, 32), Image.NEAREST)
texture_4 = Image.open('addonpacks/NexGEN26/assets/techpowers/textures/item/texture_4.png').convert('RGBA').resize((32, 32), Image.NEAREST)
greenwing = Image.open('addonpacks/NexGEN26/assets/techpowers/textures/item/greenwing.png').convert('RGBA').resize((32, 32), Image.NEAREST)
stripes = Image.open('addonpacks/NexGEN26/assets/techpowers/textures/item/stripes.png').convert('RGBA').resize((32, 32), Image.NEAREST)

# Create composite by layering
composite = wingpack.copy()
composite = Image.alpha_composite(composite, texture)
composite = Image.alpha_composite(composite, greenwing)
composite = Image.alpha_composite(composite, stripes)
composite = Image.alpha_composite(composite, texture_2)
composite = Image.alpha_composite(composite, texture_3)
composite = Image.alpha_composite(composite, texture_4)

# Save
composite.save('addonpacks/NexGEN26/assets/techpowers/textures/item/wingpack_combined.png')
print("Created wingpack_combined.png")
