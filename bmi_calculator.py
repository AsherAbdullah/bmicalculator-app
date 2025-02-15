import streamlit as st

# Set up the title
st.title("💪 BMI Calculator")

# Description
st.write("Calculate your **Body Mass Index (BMI)** and find out your weight category.")

# Input fields
weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (meters):", min_value=0.5, format="%.2f")

# Calculate BMI when user clicks the button
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)  # BMI formula
        st.write(f"### 📊 Your BMI: **{bmi:.2f}**")

        # Determine BMI category
        if bmi < 18.5:
            st.warning("You are **Underweight** 🟡")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a **Normal weight** ✅")
        elif 25 <= bmi < 29.9:
            st.warning("You are **Overweight** 🟠")
        else:
            st.error("You are **Obese** 🔴")

        st.info("**Note:** BMI is a general guide and may not be accurate for all individuals (e.g., athletes).")
    else:
        st.error("Please enter valid values for weight and height.")

