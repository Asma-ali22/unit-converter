# import streamlit as st

# st.title("🌍Unit Converter App")
# st.markdown("### Converts Length, Weight And Time Instantly")
# st.write("Welcome! Select a category, enter a value and get the converted result in real-time")

# category = st.selectbox("Choose a categoty", ["Length", "Weight", "Time"])

# def convert_units(category, value, unit):
#     if category == "Length":
#         if unit == "Kilometers to Miles":
#             return value * 0.621371
#         elif unit == "Miles to Kilometers":
#             return value / 0.621371
        
#     elif category == "Weight":
#         if unit == "Kilograms to pounds":
#             return value * 2.20462
#         elif unit == "Pounds to kilograms":
#             return value / 2.20462
#     elif category == "Time":
#         if unit == "Seconds to minutes":
#             return value / 60
#         elif unit == "Minutes to seconds":
#             return value * 60
#         elif unit == "Minutes to hours":
#             return value / 60
#         elif unit == "Hours to minutes":
#             return value * 60
#         elif unit == "Hours to days":
#             return value / 24
#         elif unit == "Days to hours":
#             return value * 24
#     return 0
        
# if category == "Length":
#     unit = st.selectbox("📏 Select Conversation", ["Miles to Kilometers","Kilometers to Miles"])
# elif category == "Weight":
#     unit = st.selectbox("⚖️ Select Conversation", ["Kilograms to pounds", "Pounds to kilograms"])
        
# elif category == "Time":
#     unit = st.selectbox("⏱️ Select Conversation", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

# value = st.number_input("Enter the value to convert")

# if st.button("Convert"):
#     result = convert_units(category, value, unit)
#     st.success(f"The result is {result:.2f}")
    
import streamlit as st

st.title("🌍 Unit Converter App")
st.markdown("### Converts Length, Weight, Time, and Temperature Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

# Category Selection
category = st.selectbox("Choose a category", ["Length", "Weight", "Time", "Temperature"])

# Function to convert units
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
    
    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15
        elif unit == "Fahrenheit to Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif unit == "Kelvin to Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    
    return None  # If no valid option is selected

# Sub-category selection based on category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Miles to Kilometers", "Kilometers to Miles"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏱️ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", 
                                                 "Minutes to Hours", "Hours to Minutes", 
                                                 "Hours to Days", "Days to Hours"])
elif category == "Temperature":
    unit = st.selectbox("🌡️ Select Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius", 
                                                  "Celsius to Kelvin", "Kelvin to Celsius", 
                                                  "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"])

# Input for value
value = st.number_input("Enter the value to convert", format="%.2f")

# Convert button
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid conversion selected")
