import ks

# Initialize KeyShot
scene = ks.Scene()

# Define material lists for permutations
metal_colors = ["Metal_Blue", "Metal_Silver", "Metal_Black", "Metal_White", "Metal_Red"]
granite_colors = ["Granite_Gray", "Granite_Black", "Granite_Brown", "Granite_White", "Granite_Green", "Granite_Beige"]

# Set paths
output_folder = "C:/KeyShot_Renders/"

# Set up camera and lighting (assume a predefined setup)
scene.setCamera("Default Camera")
scene.setLighting("Default Lighting")

# Load product model
product_path = "C:/KeyShot_Models/Table.ksp"
scene.open(product_path)

# Assign materials and render each combination
for metal in metal_colors:
    for granite in granite_colors:
        # Assign materials to parts
        scene.setMaterial("Metal_Part", metal)  # Metal part ID
        scene.setMaterial("Granite_Part", granite)  # Granite part ID

        # Set output filename based on material names
        output_name = f"{output_folder}Table_{metal}_{granite}.png"

        # Render image
        render_settings = {
            "width": 1920,
            "height": 1080,
            "samples": 64
        }
        scene.render(output_name, **render_settings)

# Save and clean up
scene.save()
scene.close()
