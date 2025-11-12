import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile
import os
import time

st.markdown("""
            <style>
            .stApp {
            background-color: #0e1117;
            color: white;
            font-family: 'Poppins', sans-serif;
            }
            
            .css-18e3th9 {
            padding-top: 2rem;
            }
            .stButton>button {
            background-color: #2a9d8f;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 0.6em 1.2em;
            }
            .stButton>button;hover {
            background-color: #21867a;
            color:white;
            }
            [data-testid="stAppViewContainer"] {
            background-image: url("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            }
            [data-testid="stAppViewContainer"]::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.6);  /* Dark transparent overlay */
            z-index: 0;
            }

            </style>
            """, unsafe_allow_html=True)

st.set_page_config(page_title="SafeEye - Safety Detection", layout="centered")

st.sidebar.title("SafeEye Dashboard")
st.sidebar.markdown("Detect and identify safety hazards in space environments.")
st.sidebar.write("----")
st.sidebar.markdown("Model: YOLOv8s")
st.sidebar.markdown("Framework: Streamlit")
st.sidebar.markdown("Developer: Shweta Mishra and Samiksha Sharma")
st.sidebar.write("----")

if st.sidebar.button("Exit Application"):
    with st.spinner("Shutting down SafeEye..."):
        time.sleep(1.2)
    st.success("Application closed successfully.")
    time.sleep(0.8)
    os._exit(0)


st.title("Space Station Safety Object Detection")
st.write("Detects safety objects like Fire Alarm, Oxygen Tank, and more using YOLOv8s.")

model = YOLO("best.pt") 

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    img = cv2.imread(tfile.name)
    st.image(img, caption="Uploaded Image", use_container_width = True)

    with st.spinner("Running detection..."):
        results = model.predict(img, conf=0.5)
        annotated = results[0].plot()
        annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
        st.image(annotated, caption="Detection Result", use_container_width=True)


    try:
        os.remove(tfile.name)
    except PermissionError:
        pass

st.write("Or try live detection (if camera available)")
if st.button("Start Webcam Detection"):
    st.warning("Streamlit webcam detection may not work in all environments.")
    st.info("Use local OpenCV window instead if it fails.")
