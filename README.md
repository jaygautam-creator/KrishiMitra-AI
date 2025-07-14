# 🌱 KrishiMitra AI

Free, open-source crop recommendation system using Machine Learning and weather data to help Indian farmers choose the most suitable and profitable crops.

---

## ✅ Features
- Input: farmer's PIN code / GPS, land size, and budget
- Output: top 2–3 crop recommendations with:
  - Estimated ROI
  - Resilience score
  - Best sowing window
- Easy-to-use web interface (Streamlit)

---

## 🛠 Tech stack
- Python, scikit-learn, XGBoost
- Streamlit (for frontend)
- OpenWeatherMap API (weather data)
- SQLite / CSV (data storage)

---

## 📦 Project structure
```

KrishiMitra-AI/
├── app/
│   ├── app.py                  # Streamlit web app
│   ├── recommendation.py       # Crop recommendation logic
│   └── data\_preprocessing.py   # Data cleaning (to implement)
├── requirements.txt           # Python dependencies
└── README.md

````

---

## 🚀 How to run locally
1. Clone the repo:
```bash
git clone https://github.com/jaygautam-creator/KrishiMitra-AI.git
cd KrishiMitra-AI
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
streamlit run app/app.py
```

The app will open in your browser at [http://localhost:8501](http://localhost:8501)

---

## ☁ Deploy on Streamlit Cloud

* Go to [https://share.streamlit.io](https://share.streamlit.io)
* New app → select this repo
* Main file: `app/app.py`
* Click Deploy → get free public URL

---

## 📊 Data sources (free/open):

* Soil Health Card (ICAR)
* Market prices (AgMarkNet)
* Weather forecast (OpenWeatherMap free tier)
* Crop yield data (ICRISAT, FAO, Kaggle)

---

## 🧩 Next steps

* Train ML models to replace dummy data
* Connect live weather and soil data
* Improve UI and add language support
* Deploy and test with real farmers

---

## 👩‍💻 Author

[Jay Gautam](https://github.com/jaygautam-creator)
