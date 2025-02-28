---

# ClickSafe — Stay Safe, Surf Smart  

ClickSafe is a simple web app that helps you check if a URL is safe or risky. Using AI and cybersecurity APIs, it analyzes links and lets you know the risk level — so you avoid phishing traps and malware.  

**Live Demo (Frontend):** Hosted on GitHub Pages  
**Backend:** Hosted on Render  

---

## Features  

- Real-time URL analysis for cyber threats  
- Threat level indicator: Low, Medium, High (color-coded)  
- Clean and responsive UI  
- Fast and lightweight — powered by Express.js and VirusTotal API  

---

## Project Structure  

```
ClickSafe
│
├── backend
│   ├── server.js           # Express backend with URL analysis API
│   ├── .env                # Environment variables (API key)
│
├── frontend
│   ├── index.html          # Main web page
│   ├── script.js           # Frontend logic and API calls
│   ├── styles.css          # Page styling
│
├── package.json            # Backend dependencies
```

---

## Tech Stack  

Frontend: HTML, CSS, JavaScript  
Backend: Node.js, Express.js, Axios  
API: VirusTotal  
Hosting: GitHub Pages (Frontend), Render (Backend)  

---

## How to Run Locally  

1. Clone this repo:  
```
git clone https://github.com/your-username/ClickSafe.git
cd ClickSafe
```

2. Set up the backend:  
```
cd backend
npm install
touch .env
```
Add your VirusTotal API key in `.env`:  
```
VIRUSTOTAL_API_KEY=your-api-key-here
```

3. Run the backend:  
```
node server.js
```
Backend runs at: `http://localhost:5000/`

4. Open the frontend:  
Just open `frontend/index.html` in your browser.

---

## Deployment  

Frontend: Hosted on GitHub Pages  
Backend: Hosted on Render  

Update the API endpoint in `script.js` for live deployment:  
```
const response = await fetch('https://clicksafe-backend.onrender.com/check-url');
```

---

## Future Plans  

- Better threat analysis visuals  
- Detailed safety reports  
- URL history & scanning logs  
- Potential browser extension  

---

## Contributing  

Feel free to fork this repo, suggest features, or report bugs. Let’s make the internet safer — together!  

---

## Disclaimer  

ClickSafe uses third-party APIs for threat analysis. Always double-check suspicious links and practice safe browsing. We take no responsibility for API limitations or misclassifications. Stay cautious!  

---

Built with love and caffeine by an engineering student with big ideas. 🚀  

---
