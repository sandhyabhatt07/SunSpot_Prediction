# 🌞 Sunspot Prediction Dashboard

A Streamlit web app to visualize historical sunspot data and forecast future sunspot activity using the ARIMA time series model.

---

## 📊 Features

- Interactive sunspot data exploration
- Line chart of historical sunspot activity
- Forecast sunspot counts for 1 to 24 months using ARIMA
- Download forecast data as CSV
- Clean and modern dashboard UI


---

## 🧠 Model

- **ARIMA (AutoRegressive Integrated Moving Average)**
  - Automatically trained on the uploaded or built-in dataset
  - Forecasts sunspot counts based on historical monthly averages

---

## 📁 Dataset

The app expects a CSV file named `train.csv` with at least the following columns:

| Month         | Avg_sunspot_count |
|---------------|------------------|
| 2010-01-01    | 15.2             |
| 2010-02-01    | 17.4             |
| ...           | ...              |

- `Month`: Date (monthly frequency)
- `Avg_sunspot_count`: Average sunspot count for that month

---

## ⚙️ Installation & Run Locally

```bash
git clone https://github.com/sandhyabhatt07/SunSpot_Prediction.git
cd SunSpot_Prediction
pip install -r requirements.txt
streamlit run app.py
