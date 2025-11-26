# ✋ Virtual Hand Gesture Keyboard

**Real-Time Virtual Typing Using MediaPipe + OpenCV**

This project implements a real-time virtual keyboard controlled entirely through hand gestures, using a standard webcam. It eliminates the need for a physical keyboard and lets users type characters with simple finger gestures in front of the camera.

The system uses MediaPipe for hand-tracking, OpenCV for image processing, and custom distance-based logic to detect key presses and deletion gestures.

**Output:**
<img width="1365" height="727" alt="1" src="https://github.com/user-attachments/assets/25137f04-6d31-4fcd-832b-a9c5acaecba5" />
<img width="1365" height="727" alt="2" src="https://github.com/user-attachments/assets/5f8f65a1-7a34-4b07-8e9d-50c5ace1558f" />
<img width="1365" height="726" alt="3" src="https://github.com/user-attachments/assets/0ad064a2-70d7-450d-af58-98f5e84a3827" />


**🧠 How It Works**

**1. Hand Detection**

    The webcam feed is processed frame-by-frame. MediaPipe identifies and tracks 21 key hand landmarks.

**2. Coordinate Extraction**

    Landmark positions (x, y) are captured for:

    Index Tip (8)

    Middle Tip (12)

    Thumb Tip (4)

    Base points used for area estimation

**3. Key Hover Detection**

    If the index fingertip lies within the bounding box of a key, it is visually highlighted.

**4. Gesture-Based Key Press**

    A key press is registered when:

    The distance between the index tip and the middle tip is within a small threshold

    The hand area is small enough

    The fingertip hovers over a key

**5. Backspace Gesture**

If the distance between the **index tip (8) and the thumb tip (4)** is very small (< 25 px),
The last character in the text box is removed.

**🛠️ Technologies Used**

    Python 

    OpenCV

    MediaPipe Hands

    NumPy

    Math (distance calculations)

**🚀 Usage Instructions**

**Install dependencies:**

    pip install opencv-python mediapipe numpy


**Run the program:**

    python main.py


**Controls:**

    Move your index finger over a key to highlight it.

    Bring index + middle fingertip close → press key.

    Bring index + thumb fingertip close → delete last character.

    Press Q on your keyboard to exit the program.

**📬 Contact**

If you face any problems, feel free to reach out:

Email: arafat.bd.hosen@gmail.com

**WhatsApp: +8801744805068**

**WeChat: arafat_cn**

**QQ: 3522584423**

