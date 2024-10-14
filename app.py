import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else np.inf  # Returning infinity for divide by zero

# Functions for scientific operations
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
st.title("Combined Scientific Graphical Calculator")

# Input fields for basic and scientific operations
st.write("### Enter the numbers:")
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# Dropdown to select the operation (basic + scientific + graphical)
operation = st.selectbox(
    "Select Operation", 
    ["Add", "Subtract", "Multiply", "Divide", "Power", "Logarithm (num1 only)", 
     "Sine (num1 only)", "Cosine (num1 only)", "Tangent (num1 only)", "Plot All Operations"]
)

# Initialize result
y_result = None
y_values = None

# Perform selected operation
if operation == "Add":
    y_result = add(num1, num2)
    y_values = add(np.linspace(-10, 10, 400), num1)
elif operation == "Subtract":
    y_result = subtract(num1, num2)
    y_values = subtract(np.linspace(-10, 10, 400), num1)
elif operation == "Multiply":
    y_result = multiply(num1, num2)
    y_values = multiply(np.linspace(-10, 10, 400), num1)
elif operation == "Divide":
    y_result = divide(num1, num2)
    y_values = divide(np.linspace(-10, 10, 400), num1)
elif operation == "Power":
    y_result = power(num1, num2)
    y_values = power(np.linspace(-10, 10, 400), num1)
elif operation == "Logarithm (num1 only)":
    y_result = log(num1)
    y_values = log(np.linspace(0.1, 10, 400))  # Adjusted for positive values
elif operation == "Sine (num1 only)":
    y_result = sin(num1)
    y_values = sin(np.linspace(-10, 10, 400))
elif operation == "Cosine (num1 only)":
    y_result = cos(num1)
    y_values = cos(np.linspace(-10, 10, 400))
elif operation == "Tangent (num1 only)":
    y_result = tan(num1)
    y_values = tan(np.linspace(-10, 10, 400))
elif operation == "Plot All Operations":
    # Plot all basic operations together on the graph
    x_values = np.linspace(-10, 10, 400)
    fig, ax = plt.subplots()
    ax.plot(x_values, add(x_values, num1), label="Add")
    ax.plot(x_values, subtract(x_values, num1), label="Subtract")
    ax.plot(x_values, multiply(x_values, num1), label="Multiply")
    ax.plot(x_values, divide(x_values, num1), label="Divide")
    ax.legend()
    ax.set_title("Basic Operations: Add, Subtract, Multiply, Divide")
    ax.set_xlabel("x")
    ax.set_ylabel("Result")
    st.pyplot(fig)

# Display the result for selected operation
if operation != "Plot All Operations" and y_result is not None:
    st.write(f"The result of {operation} is: {y_result}")

# Plot the result of the selected operation
if operation != "Plot All Operations" and y_values is not None and st.button("Plot Graph"):
    fig, ax = plt.subplots()
    ax.plot(np.linspace(-10, 10, 400), y_values)
    ax.set_title(f"Graph of {operation}")
    ax.set_xlabel("x")
    ax.set_ylabel("Result")
    st.pyplot(fig)
