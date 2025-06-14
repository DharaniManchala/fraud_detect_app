import streamlit as st
import pandas as pd
import joblib
import json
import os
import hashlib
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ----------------------------
# Helper Functions
# ----------------------------

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists("users.json") or os.path.getsize("users.json") == 0:
        return {}
    with open("users.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)

def authenticate(email, password):
    users = load_users()
    hashed = hash_password(password)
    return email in users and users[email] == hashed

def register_user(email, password):
    users = load_users()
    if email in users:
        return False
    users[email] = hash_password(password)
    save_users(users)
    return True

def save_user_history(email, df):
    os.makedirs("history", exist_ok=True)
    df.to_csv(f"history/{email.replace('@', '_at_')}.csv", index=False)

def load_user_history(email):
    path = f"history/{email.replace('@', '_at_')}.csv"
    if os.path.exists(path):
        return pd.read_csv(path)
    return None

# ----------------------------
# App Config
# ----------------------------

st.set_page_config(page_title="Fraud Detection App", layout="wide")
model = joblib.load("model/fraud_model.pkl")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "email" not in st.session_state:
    st.session_state.email = ""

# ----------------------------
# Login/Sign-up Page
# ----------------------------

if not st.session_state.authenticated:
    st.title("🔐 Login / Sign Up")

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            if authenticate(email, password):
                st.success("✅ Login successful!")
                st.session_state.authenticated = True
                st.session_state.email = email
                st.rerun()
            else:
                st.error("❌ Invalid credentials!")

    with tab2:
        email = st.text_input("New Email", key="signup_email")
        password = st.text_input("New Password", type="password", key="signup_pass")
        if st.button("Sign Up"):
            if register_user(email, password):
                st.success("✅ Account created! Please login.")
            else:
                st.error("❌ Email already exists!")

    st.stop()

# ----------------------------
# Main App (after login)
# ----------------------------

st.title("💳 Credit Card Fraud Detection")

st.markdown("Upload your credit card transactions to detect fraud using a trained ML model.")

uploaded_file = st.file_uploader("📂 Upload CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Uploaded Data")
    st.dataframe(df.head())

    # Preprocessing
    df_clean = df.copy()
    if "Class" in df_clean.columns:
        df_clean.drop(columns=["Class"], inplace=True)
    df_clean.fillna(0, inplace=True)
    df_clean = df_clean.select_dtypes(include=["number"])

    # Prediction
    prob = model.predict_proba(df_clean)[:, 1]
    pred = model.predict(df_clean)

    df["Fraud Probability"] = prob
    df["Predicted Fraud?"] = pred

    # Save user history
    save_user_history(st.session_state.email, df)

    # Results
    st.subheader("🔍 Predictions")
    st.dataframe(df[["Fraud Probability", "Predicted Fraud?"]].head())

    # Download
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    st.markdown(f'<a href="data:file/csv;base64,{b64}" download="fraud_output.csv">📥 Download Results</a>', unsafe_allow_html=True)

    # Charts
    st.subheader("📊 EDA and Visualization")
    fig1 = px.histogram(df, x="Predicted Fraud?")
    st.plotly_chart(fig1)

    fig2 = px.pie(df, names="Predicted Fraud?")
    st.plotly_chart(fig2)

    if len(df_clean.columns) >= 10:
        top_corr = df_clean.corr().abs().sum().sort_values(ascending=False).head(10).index
        fig3, ax = plt.subplots()
        sns.heatmap(df_clean[top_corr].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig3)

    # Top 10 Important Features
    st.subheader("⭐ Top 10 Important Features")
    try:
        importances = model.feature_importances_
        feature_names = df_clean.columns
        feature_df = pd.DataFrame({
            'Feature': feature_names,
            'Importance': importances
        }).sort_values(by='Importance', ascending=False).head(10)

        fig_feat = px.bar(feature_df, x='Importance', y='Feature', orientation='h', title='Top 10 Features')
        st.plotly_chart(fig_feat)

    except AttributeError:
        st.warning("Model does not support feature importances (e.g., Logistic Regression).")

# ----------------------------
# Previous History
# ----------------------------

st.subheader("🕘 Your Previous History")
hist = load_user_history(st.session_state.email)
if hist is not None:
    st.dataframe(hist.head())
else:
    st.info("No previous history found.")

# ----------------------------
# About
# ----------------------------

st.sidebar.title("📌 About")
st.sidebar.info("""
🔐 Custom login system  
📊 Predict fraud from uploaded transactions  
📥 Download results  
📈 Automatic EDA (charts, heatmaps)  
⭐ Feature importance chart  
🕘 User-specific history tracking

Built with ❤️ using Streamlit.
""")