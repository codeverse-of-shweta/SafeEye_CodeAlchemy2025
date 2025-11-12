## SafeEye: Safety Equipment Detection using YOLOv8s

# Overview

SafeEye is a deep-learning model built for the CodeAlchemy 2025 Hackathon (Duality AI - Falcon Challenge).
It automatically detects seven types of safety equipment -- including Fire Alarm, Oxygen Tank, First Aid Boxes, Safety Switch Panels, and more -- in space-station-like environments.

The model uses YOLOv8s architecture, trained on the Duality Falcon Synthetic Dataset, featuring varied lighting (dark/bright) and cluttered considtions to ensure robust real-world performance.

---------------------

# Environment Setup

Insrall dependencies (Python 3.10 or higher required) :

pip install ultralytics torch torchvision torchaudio opencv-python matplotlib pyyaml

---------------------

# Folder Structure

Final_Submission/
│
├── app.py
├── train.py
├── predict.py
├── yolo_params.yaml
├── best.pt               
├── runs/
│    ├── detect/
│    │    └── train/
├── Final_Report.pdf
├── README.txt
└── requirements.txt

---------------------

# Dataset Information

- Source: Duality Falcon Synthetic Dataset
- Classes: 7 (OxygenTank, NitrogenTank, FirstAidBox, FireAlarm SafetySwitchPanel, EmergencyPhone, FireExtinguisher)
- Format: YOLO (.txt annotations)
- Split: 70% train, 20% val, 10% test
- Structure Example:
  dataset/train/images/, dataset/train/labels/, etc.

---------------------

# How to train

1. Ensure your dataset path is correct in 'yolo_params.yaml'.
2. Run the following command:
   python train.py
   or run train.py file directly

   This will create a folder:
   'runs/detect/train/'
   containing logs, curves, and 'best.pt' weights.

---------------------

# How to predict

Place test images in:
'dataset/test/images/'

Then run:
python predict.py

Predictions (images + bounding boxes + labels) will be saved in:
'prediction/images/' and 'predictions/labels/'

---------------------

## Streamlit Application:

The SafeEye Web App provides an easy-to-use interface for testing the trained YOLOv8s model in real time. Users can upload images or use a webcam to visualize detections.

# To run the application:
  python -m streamlit run app.py

  Then open the browser linnk shown in the terminal (default: http://localhost:8501)

# App Features:
- Image Upload: Upload any image and get detection results instantly.
- Webcam Detection: Live detection using connected camera (if available).
- Custom UI: Dark-themed dashboard with background image and sidebar.
- Exit Button: One-click application shutdown

----------------------

# Model performance

mAP@0.5        : 0.55
Precision      : 0.66
Recall         : 0.55
Inference Speed: ~66 ms per image (on NVIDIA RTX 3050 GPU)

---------------------

# Key Features

- Real-time inference using YOLOv8s
- Robust detection under dark, bright, and cluttered scenes
- Early stopping and hyperparameter tuning for stable convergence
- Synthetic data augmentation for better generalization
- Optimized for lightweight deployment

---------------------

# Future Scope 

- Edge deployment using ONNX or TesnorRT
- Integration with live CCTV for continuous safety monitoring
- Automated alert system when safety items are missing

---------------------

# Team Details

Team Name - Udbhav
Team Leader - Shweta Mishra
Teamm Members - Samiksha Sharma
Institute - Accurate Institute of Management and Technology
Track: Space Station Safety Challenge - Duality Falcon

--------------------

# Result Summary

> Final Model achieved
> mAP@50 = 0.55 | Precision = 0.66 | Recall = 0.55 | Real-time performance achieved

--------------------

# Additional Files:
Due to GitHub file size limits, complete training and validation result visuals (curves, confusion matrix, and predictions)
are available here:
-- [Model_Training_Results (Google Drive Link)](https://drive.google.com/file/d/1jZrlQ7xwUsGNhPKzBxRJ-1vWItB3_lmR/view?usp=drive_link)

-------------------

# Contact 
For queries or verification:
Email: shwetamishra3055@gmail.com

-------------------

# Final Note:

SafeEye demonstrates how AI can improve astronaut safety by monitoring critical equipment inside space habitats.
The model’s real-time detection capability, optimized YOLOv8s performance, and interactive Streamlit dashboard make it suitable for integration into future space station monitoring systems

--------------------