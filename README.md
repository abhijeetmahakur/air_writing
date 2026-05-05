
# NEON Air Writing - Advanced Cyberpunk Edition

## 🚀 Features
- **Neon Glowing Trails**: Multi-layer Gaussian blur glow with brightness bloom overlay
- **Trailing Light Effect**: Exponential fade on stroke segments (older points dim)
- **Smooth Glowing Lines**: Catmull-Rom spline interpolation for curves
- **Pulsing Glow Animation**: 2Hz sine wave thickness/alpha pulse
- **Gesture Controls**: 1 finger = DRAW, 2 = TOOL, 5 = CLEAR (debounced stability)
- **Performance Optimized**: ROI blur, buffer=1, LINE_AA, frame time monitoring (30+fps)
- **Utility Features**:
  - FPS counter + mode/points display
  - Save canvas `'s'` -> air_drawing_save_001.png
  - `'b'` cycle neon brushes, `'c'` clear, `'q'` quit
- **Sound Feedback**: Uncomment `winsound.Beep(800, 20)` in draw_trail

## Tech Stack
MediaPipe Hands + OpenCV + NumPy + SciPy (spline smooth)

## Setup & Run
```bash
pip install opencv-python mediapipe numpy scipy
python air_writing.py
```

## Controls
- **Draw**: 1 finger up (index or any)
- **Gestures**: Stable finger count changes mode (DRAW/TOOL/CLEAR)
- **Keyboard**: `b` brush cycle | `c` clear | `s` save PNG | `q` quit

Cyberpunk neon air drawing with smooth real-time effects!
