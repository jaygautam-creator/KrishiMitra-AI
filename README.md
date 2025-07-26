<<<<<<< HEAD
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
=======
# KrishiMitra AI 🌾

An intelligent crop recommendation system for Indian farmers that helps them choose the most suitable and profitable crops based on their location, land size, and budget.

## Features 🚀

- **Smart Crop Recommendations** based on:
  - Location (PIN code/GPS)
  - Land area
  - Budget constraints
- **Detailed Analysis** for each recommended crop:
  - Expected Return on Investment (ROI)
  - Crop resilience score
  - Optimal sowing window
  - Weather-based insights

## Tech Stack 💻

- **Frontend**: Streamlit
- **Backend**: Python
- **ML Models**: scikit-learn, XGBoost
- **Data Sources**:
  - OpenWeatherMap API (weather data)
  - Soil Health Card (ICAR)
  - AgMarkNet (market prices)
  - ICRISAT/FAO (yield data)

## Installation 🛠️

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/krishiMitraAI.git
   cd krishiMitraAI
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   - Create a `.env` file
   - Add your OpenWeatherMap API key:
     ```
     OPENWEATHERMAP_API_KEY=your_api_key_here
     ```

5. Run the application:
   ```bash
   streamlit run app/app.py
   ```

## Project Structure 📁

```
KrishiMitra-AI/
├── app/
│   ├── app.py                  # Streamlit frontend
│   ├── recommendation.py       # Crop recommendation engine
│   └── data_preprocessing.py   # Data preprocessing pipeline
├── requirements.txt            # Project dependencies
└── README.md                  # Project documentation
```

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Future Improvements 🔮

- Multi-language support (Hindi, Marathi, Telugu, etc.)
- Integration with IoT soil sensors
- Mobile app development
- Real-time market price integration
- Community features for farmers
>>>>>>> b2cf3db (Initial commit: KrishiMitra AI application with comprehensive farmer interface)
