
# 🌐 ClickSafe — Stay Safe, Surf Smart 🛡️  

ClickSafe is a **simple, powerful web app** that helps you check if a URL is safe or shady. Using AI and cybersecurity APIs, it analyzes links and lets you know the risk level — so you don’t fall into phishing traps or malware messes.  

**🔗 Live Demo:** [ClickSafe on GitHub](https://ak-1344.github.io/ClickSafe/frontend/)  
**🛠️ Backend:** Hosted on [Render](https://render.com/)  

---

## 🚀 Features  

✅ **Real-time URL analysis** — Check for phishing, malware, and cyber threats.  
✅ **Threat level indicator** — Low, Medium, High, with color-coded feedback.  
✅ **Smooth and responsive UI** — Works perfectly on desktop and mobile.  
✅ **Fast and lightweight** — Powered by Express.js and VirusTotal API.  

---

## 🗂️ Project Structure  

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

## 🛠️ Tech Stack  

**Frontend:** HTML, CSS, JavaScript  
**Backend:** Node.js, Express.js, Axios  
**API:** [VirusTotal](https://www.virustotal.com/)  
**Hosting:** GitHub (Frontend), Render (Backend)  

---

## 🖥️ How to Run Locally  

1. **Clone this repo:**  
```bash
git clone https://github.com/ak-1344/ClickSafe.git
cd ClickSafe
```

2. **Set up the backend:**  
```bash
cd backend
npm install
touch .env
```
Add your API key in `.env`:  
```
VIRUSTOTAL_API_KEY=your-actual-api-key-here
```

3. **Run the backend:**  
```bash
node server.js
```
Backend will run at: `http://localhost:5000/`

4. **Open the frontend:**  
Just open `frontend/index.html` in your browser.

---

## 🌐 Deployment  

**Frontend:** Deployed on [GitHub Pages](https://github.com/)  
**Backend:** Deployed on [Render](https://render.com/)  

Make sure to update the API endpoint in `script.js` when deploying:  
```javascript
const response = await fetch('https://clicksafe-backend.onrender.com/check-url');
```

---

## 📝 Future Plans (Because Why Stop Here?)  

🚧 Better threat analysis visuals  
🚧 Detailed safety reports  
🚧 URL history & scanning logs  
🚧 Maybe even a browser extension?!  

---

## 👩‍💻 Contributing  

Feel free to fork this repo, suggest features, or report bugs. Let’s make the internet safer — together!  

---

## 🛡️ Disclaimer  

ClickSafe uses third-party APIs for threat analysis. Always double-check suspicious links and practice safe browsing. We take no responsibility for API limitations or misclassifications. Stay cautious!  

---

## 💌 A Little Love  

Built with ☕ and 🧠 by an **engineering student with big ideas**. 🚀  

---
