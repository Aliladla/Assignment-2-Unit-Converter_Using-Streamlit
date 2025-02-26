import streamlit as st
import pandas as pd

def length_converter(value, from_unit, to_unit):
    length_units = {"meter": 1, "kilometer": 1000, "centimeter": 0.01, "millimeter": 0.001, "mile": 1609.34, "yard": 0.9144, "foot": 0.3048, "inch": 0.0254}
    return value * (length_units[to_unit] / length_units[from_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {"kilogram": 1, "gram": 0.001, "milligram": 0.000001, "pound": 0.453592, "ounce": 0.0283495}
    return value * (weight_units[to_unit] / weight_units[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value

def time_converter(value, from_unit, to_unit):
    time_units = {"second": 1, "minute": 60, "hour": 3600, "day": 86400, "week": 604800, "month": 2628000}
    return value * (time_units[to_unit] / time_units[from_unit])

def main():
    st.title("Multi-Unit Converter")
    conversion_type = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature", "Time"])
    
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    
    from_unit, to_unit, result = None, None, None
    
    if conversion_type == "Length":
        from_unit = st.selectbox("From Unit", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
        to_unit = st.selectbox("To Unit", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
    
    elif conversion_type == "Weight":
        from_unit = st.selectbox("From Unit", ["kilogram", "gram", "milligram", "pound", "ounce"])
        to_unit = st.selectbox("To Unit", ["kilogram", "gram", "milligram", "pound", "ounce"])
    
    elif conversion_type == "Temperature":
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    
    elif conversion_type == "Time":
        from_unit = st.selectbox("From Unit", ["second", "minute", "hour", "day", "week", "month"])
        to_unit = st.selectbox("To Unit", ["second", "minute", "hour", "day", "week", "month"])
    
    if st.button("Convert"):
        if conversion_type == "Length":
            result = length_converter(value, from_unit, to_unit)
        elif conversion_type == "Weight":
            result = weight_converter(value, from_unit, to_unit)
        elif conversion_type == "Temperature":
            result = temperature_converter(value, from_unit, to_unit)
        elif conversion_type == "Time":
            result = time_converter(value, from_unit, to_unit)
        
        st.success(f"Converted Value: {result:.2f} {to_unit}")

if __name__ == "__main__":
    main()
