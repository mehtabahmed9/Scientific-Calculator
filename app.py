import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero!"

# Function for scientific operations
def power(x, y):
    return np.power(x, y)

def log(x):
    return np.log(x) if x > 0 else "Logarithm not defined for non-positive numbers!"

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def tan(x):
    return np.tan(x)

# Streamlit app layout
st.title("Scientific Graphical Calculator")

# Input fields for the numbers
st.write("### Basic Operations")
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# Select operation for basic arithmetic
operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform basic calculation
if st.button("Calculate Basic Operation"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    
    st.write(f"The result of {operation} is: {result}")

# Scientific operations
st.write("### Scientific Operations")

# Input field for scientific operations
num = st.number_input("Enter a number for scientific functions", format="%.2f")

# Select scientific operation
sci_operation = st.selectbox("Select Scientific Function", ["Power", "Logarithm", "Sine", "Cosine", "Tangent"])

if sci_operation == "Power":
    exponent = st.number_input("Enter exponent", format="%.2f")
    if st.button("Calculate Power"):
        result = power(num, exponent)
        st.write(f"{num} raised to the power of {exponent} is: {result}")
elif sci_operation == "Logarithm":
    if st.button("Calculate Logarithm"):
        result = log(num)
        st.write(f"The natural logarithm of {num} is: {result}")
elif sci_operation == "Sine":
    if st.button("Calculate Sine"):
        result = sin(num)
        st.write(f"The sine of {num} is: {result}")
elif sci_operation == "Cosine":
    if st.button("Calculate Cosine"):
        result = cos(num)
        st.write(f"The cosine of {num} is: {result}")
elif sci_operation == "Tangent":
    if st.button("Calculate Tangent"):
        result = tan(num)
        st.write(f"The tangent of {num} is: {result}")

# Graph plotting
st.write("### Graph Plotting")

# Function input for graph plotting
function = st.selectbox("Select a function to plot", ["Sine", "Cosine", "Exponential"])

x_values = np.linspace(-10, 10, 400)
y_values = None

if function == "Sine":
    y_values = np.sin(x_values)
elif function == "Cosine":
    y_values = np.cos(x_values)
elif function == "Exponential":
    y_values = np.exp(x_values)

# Plot the selected function
if st.button("Plot Graph"):
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set_title(f"Graph of {function}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    st.pyplot(fig)
