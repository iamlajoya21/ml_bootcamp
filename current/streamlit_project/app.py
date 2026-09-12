import joblib
import numpy as np
import pandas as pd
import streamlit as st

MODEL_PATH = "model_artifacts/model.joblib"
FEATURE_NAMES = ["feature_1", "feature_2", "feature_3"]

st.set_page_config(page_title="Fraud Model Explorer", page_icon="🔍", layout="centered")


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


model = load_model()

st.title("🔍 Fraud Model Explorer")
st.caption("A data app for interacting with the fraud_v1_logreg model")

tab_single, tab_batch = st.tabs(["Single prediction", "Batch (CSV) prediction"])

with tab_single:
    st.subheader("Enter feature values")
    col1, col2, col3 = st.columns(3)
    with col1:
        feature_1 = st.slider("Account age (years)", 0.0, 10.0, 2.0, 0.1)
    with col2:
        feature_2 = st.number_input("Transactions (24h)", min_value=0, max_value=200, value=5)
    with col3:
        feature_3 = st.number_input("Avg transaction amount", min_value=0.0, max_value=100000.0, value=10.0)

    if st.button("Predict", type="primary"):
        X = np.array([[feature_1, feature_2, feature_3]])
        pred = int(model.predict(X)[0])
        proba = float(model.predict_proba(X)[0][pred])

        m1, m2 = st.columns(2)
        m1.metric("Prediction", "Fraud" if pred == 1 else "Legit")
        m2.metric("Confidence", f"{proba:.1%}")

        coefs = model.coef_[0]
        contributions = pd.DataFrame({
            "feature": FEATURE_NAMES,
            "value": [feature_1, feature_2, feature_3],
            "contribution": [feature_1 * coefs[0], feature_2 * coefs[1], feature_3 * coefs[2]],
        }).set_index("feature")
        st.bar_chart(contributions["contribution"])

with tab_batch:
    st.subheader("Upload a CSV for batch scoring")
    st.caption("Expected columns: feature_1, feature_2, feature_3")
    uploaded = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded is not None:
        df = pd.read_csv(uploaded)
        missing = set(FEATURE_NAMES) - set(df.columns)
        if missing:
            st.error(f"Missing columns: {missing}")
        else:
            X = df[FEATURE_NAMES].to_numpy()
            preds = model.predict(X)
            probas = model.predict_proba(X)
            df["prediction"] = preds
            df["probability"] = [probas[i][p] for i, p in enumerate(preds)]

            st.dataframe(df, use_container_width=True)
            st.bar_chart(df["prediction"].value_counts())

            csv_bytes = df.to_csv(index=False).encode("utf-8")
            st.download_button("Download scored CSV", csv_bytes, "scored.csv", "text/csv")
