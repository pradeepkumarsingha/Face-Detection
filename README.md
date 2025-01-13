 Real-Time Face Detection Using OpenCV

This project demonstrates real-time face detection using OpenCV's Haar Cascade Classifier. It captures video from a webcam, detects faces in the feed, and highlights them with bounding rectangles in real time.

 📦 Features
- Real-Time Detection: Detects faces in live video feeds from the webcam.  
- Face Highlighting: Draws green rectangles around detected faces.  
- Efficient Performance: Uses OpenCV's lightweight Haar Cascade model for fast processing.  

🛠️ Requirements
- Python 3.9.6
- OpenCV (`cv2`)

⚙️ Installation
1. Clone the repository:
   git clone https://github.com/pradeepkumarsingha/real-time-face-detection.git
   cd real-time-face-detection


2. Install required libraries:
   pip install opencv-python
 

3. Download the Haar Cascade XML file:
   - Ensure `haarcascade_frontalface_default.xml` is in the project directory. You can download it from [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades).

🚀 Usage
1. Run the script:
   python face_detection.py
 

2. The webcam will open, and faces will be detected and highlighted in real time.

3. Press `ESC` to exit the application.

 🖼️ How It Works
1. Load Model: The Haar Cascade model is loaded using OpenCV.  
2. Access Camera: The webcam feed is captured using `cv2.VideoCapture()`.  
3. Detect Faces: Each frame is converted to grayscale, and the classifier detects faces in the frame.  
4. Highlight Faces: Rectangles are drawn around detected faces in the original frame.  

📂 Project Structure
- `face_detection.py`: The main script for real-time face detection.
- `haarcascade_frontalface_default.xml`: Haar Cascade model file for face detection.

🛡️ License
This project is licensed under the [MIT License](LICENSE).

🤝 Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for improvements.

📞 Contact
For questions or support:  7855900487

📧 Email: mr.pradeepkumarsingha@gmail.com

