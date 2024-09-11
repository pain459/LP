from PIL import Image, ImageDraw, ImageOps
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import os

# Convert mm to points for ReportLab (1 mm = 2.83465 points)
def mm_to_pt(mm_value):
    return mm_value * 2.83465

# Set card and A4 dimensions in mm
card_width_mm = 54
card_height_mm = 80
a4_width_mm = 210
a4_height_mm = 297

# Convert card dimensions to points for the PDF generation
card_width_pt = mm_to_pt(card_width_mm)
card_height_pt = mm_to_pt(card_height_mm)

# Resource image paths (replace these with paths to your actual resource images)
resource_images = {
    "wood": "/home/ravik/src_git/LP/projects/create_catan_cards/wood.webp",   # Replace with actual image path
    "stone": "/home/ravik/src_git/LP/projects/create_catan_cards/stone.webp", # Replace with actual image path
    "brick": "/home/ravik/src_git/LP/projects/create_catan_cards/brick.webp", # Replace with actual image path
    "sheep": "/home/ravik/src_git/LP/projects/create_catan_cards/sheep.webp", # Replace with actual image path
    "wheat": "/home/ravik/src_git/LP/projects/create_catan_cards/wheat.webp"  # Replace with actual image path
}

# Number of cards for each resource
cards_per_resource = 19
total_cards = cards_per_resource * len(resource_images)

# Function to add rounded corners to the card
def add_rounded_corners(card, radius):
    mask = Image.new('L', card.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), card.size], radius=radius, fill=255)
    rounded_card = ImageOps.fit(card, card.size, centering=(0.5, 0.5))
    rounded_card.putalpha(mask)
    return rounded_card

# Create a function to generate a card (without resource name)
def create_card(image_path, radius=20):
    # Create a blank card with transparent background
    card = Image.new('RGBA', (int(mm_to_pt(card_width_mm)), int(mm_to_pt(card_height_mm))), color=(255, 255, 255, 0))
    
    # Open resource image and convert to RGBA to handle transparency
    resource_img = Image.open(image_path).convert("RGBA")
    resource_img = resource_img.resize((card.width - 20, card.height - 50), Image.Resampling.LANCZOS)

    # Paste the resource image onto the card using its alpha channel as a mask
    card.paste(resource_img, (10, 10), resource_img)

    # Add rounded corners
    card_with_rounded_corners = add_rounded_corners(card, radius)

    return card_with_rounded_corners


# Generate the PDF file
def generate_pdf():
    c = canvas.Canvas("catan_cards_webp.pdf", pagesize=A4)

    x_offset = mm_to_pt(10)  # Small margin from the left
    y_offset = mm_to_pt(10)  # Small margin from the top
    x_margin = mm_to_pt(5)   # Space between cards horizontally
    y_margin = mm_to_pt(5)   # Space between cards vertically

    x_pos = x_offset
    y_pos = a4_height_mm * mm - y_offset - card_height_pt

    resource_names = list(resource_images.keys())

    # Loop through all resources and create cards
    for i, resource_name in enumerate(resource_names * cards_per_resource):
        card_img = create_card(resource_images[resource_name])

        # Save the card temporarily as an image file
        card_img_path = f"{resource_name}_{i}.png"
        card_img.save(card_img_path)

        # Draw the image on the PDF
        c.drawImage(card_img_path, x_pos, y_pos, card_width_pt, card_height_pt)

        # Update x and y positions for the next card
        x_pos += card_width_pt + x_margin
        if x_pos + card_width_pt > a4_width_mm * mm:
            x_pos = x_offset
            y_pos -= card_height_pt + y_margin

        # If y_pos is too low, create a new page
        if y_pos < 0:
            c.showPage()  # Create a new page
            x_pos = x_offset
            y_pos = a4_height_mm * mm - y_offset - card_height_pt

    c.save()

    # Remove temporary image files after saving the PDF
    for i, resource_name in enumerate(resource_names * cards_per_resource):
        os.remove(f"{resource_name}_{i}.png")

# Call the function to generate the PDF
generate_pdf()

print("PDF generated successfully!")
