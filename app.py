# app.py
import streamlit as st
import pandas as pd
from cleaning_script import direct_billing_dc, pay_lawma_dc 

st.title(" Customized Data Cleaning App ")

uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")

        st.write("📄 Raw Data", df.head())

        # Option to select which cleaning logic to apply
        cleaning_option = st.selectbox("Choose cleaning routine", ("Select", "Direct Billing", "PayLaw Billing"))

        if cleaning_option == "Direct Billing":
            cleaned_df = direct_billing_dc(df)

        elif cleaning_option == "PayLaw Billing":
            cleaned_df = pay_lawma_dc(df)

        else:
            cleaned_df = None

        if cleaned_df is not None:
            st.success("Data cleaned successfully!")
            st.write(" Cleaned Data", cleaned_df.head())

            # Download button
            csv = cleaned_df.to_csv(index=False).encode('utf-8')
            st.download_button("⬇️ Download Cleaned Data", data=csv, file_name="cleaned_data.csv", mime='text/csv')

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("""
    <hr style="border: none; height: 1px; background-color: #ccc;" />
    <div style='text-align: center; padding-top: 10px; color: grey; font-size: 0.9em;'>
        © 2025 <b>DataSentinel</b>
    </div>
""", unsafe_allow_html=True)

