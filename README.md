<h1 align="center">💳 Credit Card Fraud Detection App</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-Deployed-success?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Enabled-blueviolet?style=for-the-badge&logo=scikitlearn" />
  <img src="https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python" />
</p>

<p align="center">
  <b>🚀 Real-time credit card fraud detection with ML, visual insights, and user-specific tracking.</b><br>
  <a href="https://frauddetectapp-erutjappeyfnztb6gnsbvds.streamlit.app"><strong>🔗 Live Demo »</strong></a><br>
  <i>Built with ❤️ by Dharani Manchala</i>
</p>

---

## 🔍 Overview

A smart web application that allows users to upload credit card transaction data in CSV format and instantly detect fraudulent activity using a trained machine learning model. Features include secure login, real-time predictions, visual analytics, and downloadable results.

---

## ✨ Key Features

- 🔐 **Secure Login & Signup** — Passwords are hashed and securely stored
- 📂 **Upload CSV Files** — Analyze transaction datasets for fraud
- 🧠 **ML Model** — Trained on real credit card data with `scikit-learn`
- 📊 **Visual Analytics** — Interactive charts (Plotly, Seaborn, Matplotlib)
- 📥 **Downloadable Predictions** — Save fraud results to CSV
- 🔁 **Upload New File** — Seamless re-upload without page refresh
- 🕘 **User-Specific History** — Auto-saves your results for future reference

---

## 🧠 Tech Stack

| Category     | Tools / Libraries                          |
|--------------|---------------------------------------------|
| Language     | Python 3.9+                                 |
| Web Framework| Streamlit                                  |
| ML Model     | Scikit-learn, Joblib                        |
| Visualization| Plotly, Seaborn, Matplotlib                 |
| Storage      | JSON (for login), CSV (for user history)    |
| Security     | hashlib (password hashing)                  |
| Deployment   | Streamlit Cloud                             |

---

## 🚀 How to Use

1. 🔐 **Log In or Sign Up**
2. 📁 **Upload** a credit card transaction `.csv` file
3. ⚙️ **Model runs** to detect fraudulent entries
4. 📊 **Results shown** with prediction, probability & charts
5. 📥 **Download** the CSV result or
6. 🔁 Click **Upload Another File** to analyze new data
7. 🕘 **History is saved** automatically for each user

---

## 📁 Project Structure


fraud-detection-app/
├── app.py # Main Streamlit app
├── model/
│ └── fraud_model.pkl # Trained ML model
├── history/ # Stores user upload history
├── users.json # Stores login credentials (hashed)
├── requirements.txt # Python dependencies
└── .streamlit/ # Streamlit configuration



---

## 📬 Author

**👨‍💻 Dharani Manchala**  
🎓 B.Tech CSE | ML & Full Stack Enthusiast  
📧 dharanimanchala48@gmail.com  
🌐 [GitHub](https://github.com/dharanimanchala)

---

## 🔗 Live Demo

Click below to explore the live app now:

👉 **[frauddetectapp-erutjappeyfnztb6gnsbvds.streamlit.app](https://frauddetectapp-erutjappeyfnztb6gnsbvds.streamlit.app)**

---

## 💡 Why This Project Matters

✅ Demonstrates real-world ML deployment  
✅ Covers secure auth, session state, and file management  
✅ Interactive and production

