from PIL import Image, ImageFont, ImageDraw

# Laad de achtergrond afeebdling in de variabele: achtergrond
achtergrond = Image.open("achtergrondmeme.jpg")

# Afmetingen opslaan in eigen variabelen
breedte = achtergrond.width
hoogte = achtergrond.height

# Laad het Impact lettertype
lettertype = ImageFont.truetype("impact.ttf", 40)

# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)

# Tekst schrijven
tekst = "Jumping in conclusions\nlike"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))

# Het resultaat tonen
achtergrond.show()

# En opslaan onder een andere naam
achtergrond.save("memetekst.jpg")

