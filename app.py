import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import json
import os

st.title("Labeling UI Prototype")
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:

    # Load image as PIL for canvas background
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    # Bounding box canvas
    canvas_result = st_canvas(
        fill_color="rgba(255,0,0,0.3)",
        stroke_width=2,
        background_image=image,
        update_streamlit=True,
        height=image.height,
        width=image.width,
        drawing_mode="rect",
        key="canvas",
    )

    # Save box coordinates
    if st.button("Save Boxes"):
        if canvas_result.json_data and canvas_result.json_data["objects"]:
            annotations = {
                "filename": uploaded_file.name,
                "boxes": canvas_result.json_data["objects"]
            }

            os.makedirs("annotations", exist_ok=True)
            out_path = f"annotations/{uploaded_file.name}_boxes.json"
            with open(out_path, "w") as f:
                json.dump(annotations, f, indent=2)

            st.success(f"Saved to {out_path}")
        else:
            st.warning("No boxes drawn.")