import tkinter as tk
from tkinter import filedialog
import cv2
import pytesseract

# Function to recognize text from an image
def recognize_text(image_path):
    image = cv2.imread(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip() if text.strip() else None

# Function to detect objects in an image
def detect_objects(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Perform object detection using OpenCV (this is a basic example)
    # Replace this with actual object detection using TensorFlow models like YOLO or SSD
    # Object detection code goes here...

    return ["object1", "object2", "object3"]  # Example detected objects

# Function to browse and process an image
def browse_image():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Image", filetypes=(("Image files", "*.jpg *.jpeg *.png"), ("All files", "*.*")))
    recognized_text = recognize_text(filename)
    detected_objects = detect_objects(filename)

    print("Recognized text:", recognized_text)
    print("Detected objects:", detected_objects)

# Create the main window
root = tk.Tk()
root.title("Educational Tool")

# Create a button to browse images
button = tk.Button(root, text="Browse Image", command=browse_image)
button.pack()

# Run the application
root.mainloop()
