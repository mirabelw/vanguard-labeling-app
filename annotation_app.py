import gradio as gr
from gradio_image_annotation import image_annotator
import json, os, time

def save_boxes(annot):
    if not annot or "boxes" not in annot:
        return "No image or boxes provided."
    filename = f"uploaded_{int(time.time())}.png"
    annotations = {"filename": filename, "boxes": []}
    for box in annot["boxes"]:
        annotations["boxes"].append({
            "xmin": box["xmin"],
            "ymin": box["ymin"],
            "xmax": box["xmax"],
            "ymax": box["ymax"],
            "label": box.get("label", "")
        })
    os.makedirs("annotations", exist_ok=True)
    path = f"annotations/{filename}_boxes.json"
    with open(path, "w") as f:
        json.dump(annotations, f, indent=2)
    return f"Saved to {path}"

# Full label list you provided
labels = [
    "Car", "Large vehicle", "Truck", "Bus", "Train", "Bicycle", "Motorized two-wheeler",
    "Fixed-wing Aircraft", "Small Aircraft", "Cargo Plane", "Helicopter", "Passenger Vehicle",
    "Small Car", "Pickup Truck", "Utility Truck", "Cargo Truck", "Truck w/Box", "Truck Tractor",
    "Trailer", "Truck w/Flatbed", "Truck w/Liquid", "Crane Truck", "Railway Vehicle",
    "Passenger Car", "Cargo Car", "Flat Car", "Tank car", "Locomotive", "Maritime Vessel",
    "Motorboat", "Sailboat", "Tugboat", "Barge", "Fishing Vessel", "Ferry", "Yacht",
    "Container Ship", "Oil Tanker", "Engineering Vehicle", "Tower crane", "Container Crane",
    "Reach Stacker", "Straddle Carrier", "Mobile Crane", "Dump Truck", "Haul Truck",
    "Scraper/Tractor", "Front loader/Bulldozer", "Excavator", "Cement Mixer", "Ground Grader",
    "Hut/Tent", "Shed", "Building", "Aircraft Hangar", "Damaged Building", "Facility",
    "Construction Site", "Vehicle Lot", "Helipad", "Storage Tank", "Shipping container lot",
    "Shipping Container", "Pylon", "Tower", "Pedestrian", "Pedestrian group", "Animal",
    "DJI", "FutabaT14", "FutabaT7", "Graupner", "Noise", "Taranis", "Turnigy", "Other"
]

# One color per label (all red for now)
colors = [(255, 0, 0)] * len(labels)

with gr.Blocks() as demo:
    gr.Markdown("## Labeling UI Prototype")
    
    annot = image_annotator( 
        label_list=labels,
        label_colors=colors
    )
    
    save_btn = gr.Button("Save")
    status = gr.Textbox(lines=1, label="Status")
    save_btn.click(save_boxes, inputs=annot, outputs=status)

demo.launch()
