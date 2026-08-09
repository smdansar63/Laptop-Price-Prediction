import streamlit as st 
import requests
import pandas as pd 


st.set_page_config(
    page_title="Laptop Price Prediction",
    page_icon="💻",
    layout="centered"
)

st.title("Laptop Price Prediction")

st.write(
    "Enter the laptop specifications below and click **Predict Price**."
)

st.sidebar.title("About")

st.sidebar.write("""
This project predicts laptop prices using an
XGBoost Regressor trained on laptop specifications.
""")


st.markdown("---")
st.caption("Made by Mohammed Ansar")

df = pd.read_csv("laptop_prices.csv")

company = st.selectbox(
    "Company",
    sorted(df["Company"].unique())
)

product = st.selectbox(
    "Product",
    sorted(df["Product"].unique())
)

typename = st.selectbox(
    "Type",
    sorted(df["TypeName"].unique())
)

inches = st.number_input(
    "Screen Size (Inches)",
    min_value=10.0,
    max_value=20.0,
    step=0.1
)

ram = st.selectbox(
    "RAM (GB)",
    sorted(df["Ram"].unique())
)

os = st.selectbox(
    "Operating System",
    sorted(df["OS"].unique())
)

weight = st.number_input(
    "Weight (kg)",
    min_value=0.5,
    max_value=5.0,
    step=0.01
)

screen = st.selectbox(
    "Screen Type",
    sorted(df["Screen"].unique())
)

screenw = st.number_input(
    "Screen Width",
    min_value=800,
    max_value=4000,
    step=1
)

screenh = st.number_input(
    "Screen Height",
    min_value=600,
    max_value=3000,
    step=1
)

touchscreen = st.selectbox(
    "Touchscreen",
    sorted(df["Touchscreen"].unique())
)

ipspanel = st.selectbox(
    "IPS Panel",
    sorted(df["IPSpanel"].unique())
)

retina = st.selectbox(
    "Retina Display",
    sorted(df["RetinaDisplay"].unique())
)

cpu_company = st.selectbox(
    "CPU Company",
    sorted(df["CPU_company"].unique())
)

cpu_freq = st.number_input(
    "CPU Frequency (GHz)",
    min_value=0.5,
    max_value=5.0,
    step=0.1
)

cpu_model = st.selectbox(
    "CPU Model",
    sorted(df["CPU_model"].unique())
)

primary_storage = st.number_input(
    "Primary Storage (GB)",
    min_value=0,
    max_value=4000,
    step=1
)

secondary_storage = st.number_input(
    "Secondary Storage (GB)",
    min_value=0,
    max_value=4000,
    step=1
)

primary_storage_type = st.selectbox(
    "Primary Storage Type",
    sorted(df["PrimaryStorageType"].unique())
)

secondary_storage_type = st.selectbox(
    "Secondary Storage Type",
    sorted(df["SecondaryStorageType"].unique())
)

gpu_company = st.selectbox(
    "GPU Company",
    sorted(df["GPU_company"].unique())
)

gpu_model = st.selectbox(
    "GPU Model",
    sorted(df["GPU_model"].unique())
)

if st.button("Predict Price"):

    input_df = pd.DataFrame({
        "Company": [company],
        "Product": [product],
        "TypeName": [typename],
        "Inches": [inches],
        "Ram": [ram],
        "OS": [os],
        "Weight": [weight],
        "Screen": [screen],
        "ScreenW": [screenw],
        "ScreenH": [screenh],
        "Touchscreen": [touchscreen],
        "IPSpanel": [ipspanel],
        "RetinaDisplay": [retina],
        "CPU_company": [cpu_company],
        "CPU_freq": [cpu_freq],
        "CPU_model": [cpu_model],
        "PrimaryStorage": [primary_storage],
        "SecondaryStorage": [secondary_storage],
        "PrimaryStorageType": [primary_storage_type],
        "SecondaryStorageType": [secondary_storage_type],
        "GPU_company": [gpu_company],
        "GPU_model": [gpu_model]
    })

    try:
        response = requests.post(
            "https://laptop-price-prediction-mbp5.onrender.com/predict",
            json=input_df.iloc[0].to_dict(),
            timeout=10
        )

        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.success(f"💻 Predicted Laptop Price: €{prediction:,.2f}")
        else:
            st.error("Prediction failed.")

    except requests.exceptions.ConnectionError:
        st.error("FastAPI server is not running. Please start the backend first.")