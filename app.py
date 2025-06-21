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

with gr.Blocks() as demo:
    gr.Markdown("## Labeling UI Prototype")
    
    annot = image_annotator( 
        label_list=["object"],
        label_colors=[(255, 0, 0)]
    )
    
    save_btn = gr.Button("Save")
    status = gr.Textbox(lines=1, label="Status")
    save_btn.click(save_boxes, inputs=annot, outputs=status)

demo.launch()