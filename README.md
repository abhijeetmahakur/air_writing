
# AirWrite

AirWrite is a single-page browser drawing experiment. It uses a webcam and MediaPipe Hands to track a hand, then draws gestures on an HTML canvas.

## Requirements

- A modern browser with webcam support
- Webcam permission
- Internet access for the MediaPipe and font assets loaded from CDNs

Camera access requires a secure browser context. Use `localhost` or HTTPS rather than opening the page directly from an arbitrary `file://` URL.

## Run locally

From this repository directory, start a local static server:

```bash
python -m http.server 8000
```

Open <http://localhost:8000> and allow camera access.

## Controls

The page includes on-screen controls for color, brush settings, erasing, ghost mode, undo, clearing, and saving. Keyboard shortcuts are shown in the interface.

## Limitations

Camera availability and hand tracking depend on browser permissions, lighting, and the connected device. There is no automated test suite or build step in this repository.

No project license is included. Check the rights for bundled or externally loaded assets before redistributing them.
