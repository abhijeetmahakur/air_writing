# AirWrite — Neon AI Air-Drawing Studio

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-success?style=for-the-badge&logo=github)](https://abhijeetmahakur.github.io/air_writing/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![MediaPipe](https://img.shields.io/badge/AI-MediaPipe%20Hands-FF5722?logo=google&logoColor=white)](https://developers.google.com/mediapipe)
[![HTML5 Canvas](https://img.shields.io/badge/Graphics-HTML5%20Canvas-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
[![Windows Executable](https://img.shields.io/badge/Release-Windows%20.exe-0078D6?logo=windows&logoColor=white)](https://github.com/abhijeetmahakur/air_writing/releases/latest)

Draw, sketch, and erase in 3D mid-air using only your hand gestures and a webcam. Powered by Google MediaPipe Hands computer vision and high-performance HTML5 Canvas with neon glow effects.

---

## 🚀 Download & Quick Start

### 🌐 1. Try Live in Browser (No Install Needed!)
Launch the interactive web application immediately via GitHub Pages:  
👉 **[Open Live AirWrite Demo](https://abhijeetmahakur.github.io/air_writing/)**  
*(Requires modern browser with webcam permissions enabled).*

### 💾 2. Standalone Windows Executable (.exe)
1. Download `AirWrite.exe` from **[GitHub Releases v1.0.0](https://github.com/abhijeetmahakur/air_writing/releases/latest)**.
2. Double click `AirWrite.exe` to automatically start the local environment and launch the canvas.

### 💻 3. Run Locally from Source
```powershell
# Clone the repository
git clone https://github.com/abhijeetmahakur/air_writing.git
cd air_writing

# Option A: Run using Python (Built-in)
python app.py
# (Or: python -m http.server 8000 -> Open http://localhost:8000)

# Option B: Run using Node.js
npm start
```

---

## 📸 Screenshots & UI Showcase

<!--
  PLACEHOLDER INSTRUCTION:
  1. Open https://abhijeetmahakur.github.io/air_writing/ or run python app.py.
  2. Hold your hand in front of the webcam and draw a glowing neon word or spiral.
  3. Click 'Save' or press Win + Shift + S to take a screenshot.
  4. Save the screenshot as `demo.png` and add it to an `assets/` folder.
-->

| Mid-Air Neon Drawing in Action | Toolbar & Gesture HUD |
| :---: | :---: |
| ![AirWrite Live Drawing Demo](https://placehold.co/600x380/0A0A12/FF4DC4?text=AirWrite+Neon+Gesture+Drawing+Screenshot) | ![AirWrite Controls HUD](https://placehold.co/600x380/0F0F1C/00E5FF?text=AirWrite+Color+Palette+%26+Tools+HUD) |
| *Real-time fingertip tracking drawing radiant glowing brush strokes* | *Floating glassmorphic controls with color picker, stroke slider, and undo* |

---

## 🖐 Hand Gestures & Control Guide

| Gesture / Key | Action | Description |
| :--- | :--- | :--- |
| ☝ **Single Index Finger** | **Draw** | Raise only your index finger to draw glowing continuous lines. |
| 🖐 **Open Palm (All 5 Fingers)** | **Erase** | Open all 5 fingers to trigger the dynamic eraser circle. |
| ⌨ **`Z` Key** | **Undo** | Reverts the most recent stroke or eraser action. |
| ⌨ **`C` Key** | **Clear** | Clears the active canvas layer completely. |
| ⌨ **`G` Key** | **Ghost Mode** | Toggles ephemeral trail mode where strokes gradually fade away. |
| ⌨ **`S` Key** | **Save** | Exports composite mirrored webcam + drawing as high-res PNG. |
| ⌨ **`E` Key** | **Manual Eraser** | Switches between pen and eraser tool. |

---

## ✨ Key Features

- **Accurate Real-Time Hand Tracking:** Pinned Google MediaPipe Hands model tracking 21 3D landmarks at 60 FPS.
- **Vibrant Neon Glow Shaders:** Multi-pass canvas compositing creating radiant cyberpunk light trails.
- **Glassmorphic Floating HUD:** Quick-access swatches (Pink, Purple, Cyan, Green, Yellow, White) and stroke-size slider.
- **Ghost Trail Mode:** Dynamic fade decay simulating optical light-painting effects.
- **Composite Image Export:** High-res PNG exporter that captures both camera frame and drawn artwork simultaneously.
- **Zero Server Overhead:** Completely client-side execution — video frames never leave your local machine.

---

## 🛠 Tech Stack

| Technology | Category | Role |
| :--- | :--- | :--- |
| **Google MediaPipe Hands** | Computer Vision / AI | Real-time 21-point hand landmark and gesture detection |
| **HTML5 Canvas API** | Rendering Engine | Hardware-accelerated 2D stroke rasterization & glow filter |
| **Vanilla JavaScript (ES6+)** | Frontend Logic | Gesture state machine, math interpolations, particle emitter |
| **Vanilla CSS (Glassmorphism)** | Styling | Responsive layout, dark UI palette, backdrop-filter blur |
| **Python / PyInstaller** | Desktop Runner | Optional local packaging to standalone Windows executable |

---

## 📦 Building Standalone .exe with PyInstaller

If you wish to build the Windows executable yourself:

```powershell
pip install pyinstaller
pyinstaller --noconsole --onefile --name "AirWrite" --add-data "index.html;." app.py
```

The compiled standalone executable will be located in `dist/AirWrite.exe`.

---

## 📂 Project Structure

```
air_writing/
├── .github/
│   └── workflows/
│       └── deploy-pages.yml     # Automated GitHub Pages deployment
├── index.html                   # Complete application (Canvas, MediaPipe, UI, Logic)
├── app.py                       # Python local server & desktop launcher
├── package.json                 # Optional npm scripts definition
├── requirements.txt             # PyInstaller packaging dependencies
├── .gitignore                   # Ignore system, build, and node artifacts
├── LICENSE                      # MIT License
└── README.md                    # Documentation
```

---

## 🗺 Future Improvements

- [ ] Multi-hand dual drawing and gesture gestures (pinch to zoom/scale)
- [ ] Air color palette selection using 3D pinch gesture
- [ ] Recording mode to export animated WebM/GIF clips
- [ ] Shape recognition (auto-smoothing circles, squares, and arrows)

---

## 👨‍💻 Author

**Abhijeet Mahakur**
- GitHub: [@abhijeetmahakur](https://github.com/abhijeetmahakur)
- LinkedIn: [Abhijeet Mahakur](https://www.linkedin.com/in/abhijeetmahakur/)
- Location: Bhubaneswar, India

---

## 📄 License

This project is open-source under the [MIT License](LICENSE) - Copyright (c) 2026 Abhijeet Mahakur.
