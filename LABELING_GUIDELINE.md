# 📖 Labeling Guidelines

## Purpose  
Allows image annotation to help train defense model.

---

## Annotation Tool  
Use the provided Gradio labeling UI:

- Upload an image
- Select the label from the dropdown list
- Draw bounding boxes tightly 
- Save annotations using the **Save** button (JSON files automatically saved in `/annotations/`)

---

## Label List  

Use one of the following labels for each object annotated:

- Car  
- Large vehicle  
- Truck  
- Bus  
- Train  
- Bicycle  
- Motorized two-wheeler  
- Fixed-wing Aircraft  
- Small Aircraft  
- Cargo Plane  
- Helicopter  
- Passenger Vehicle  
- Small Car  
- Pickup Truck  
- Utility Truck  
- Cargo Truck  
- Truck w/Box  
- Truck Tractor  
- Trailer  
- Truck w/Flatbed  
- Truck w/Liquid  
- Crane Truck  
- Railway Vehicle  
- Passenger Car  
- Cargo Car  
- Flat Car  
- Tank car  
- Locomotive  
- Maritime Vessel  
- Motorboat  
- Sailboat  
- Tugboat  
- Barge  
- Fishing Vessel  
- Ferry  
- Yacht  
- Container Ship  
- Oil Tanker  
- Engineering Vehicle  
- Tower crane  
- Container Crane  
- Reach Stacker  
- Straddle Carrier  
- Mobile Crane  
- Dump Truck  
- Haul Truck  
- Scraper/Tractor  
- Front loader/Bulldozer  
- Excavator  
- Cement Mixer  
- Ground Grader  
- Hut/Tent  
- Shed  
- Building  
- Aircraft Hangar  
- Damaged Building  
- Facility  
- Construction Site  
- Vehicle Lot  
- Helipad  
- Storage Tank  
- Shipping container lot  
- Shipping Container  
- Pylon  
- Tower  
- Pedestrian  
- Pedestrian group  
- Animal  
- DJI  
- FutabaT14  
- FutabaT7  
- Graupner  
- Noise  
- Taranis  
- Turnigy  
- Other  

---

## Labeling Instructions  

- Draw tight, rectangular bounding boxes around visible, clearly identifiable objects
- Select the **most specific applicable label** from the list
- Do not annotate objects that are:
  - Obstructed beyond recognition
  - Severely blurred
  - Outside the scope of labeling targets

---

## File Saving  

- Annotations are automatically saved in the `/annotations/` folder as JSON files  
- Each JSON contains:
  - Image filename
  - List of annotated boxes with coordinates and labels

**Example:**

```json
{
  "filename": "uploaded_123456789.png",
  "boxes": [
    {
      "xmin": 50,
      "ymin": 60,
      "xmax": 200,
      "ymax": 250,
      "label": "Car"
    }
  ]
}
