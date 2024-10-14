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
    return np.log(x) if x > 0 else np.nan  # Logarithm for positive numbers only

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
    ["Add", "Subtract", "Multiply", "Divide", "Power", 
     "Logarithm (num1 only)", "Sine (num1 only)", 
     "Cosine (num1 only)", "Tangent (num1 only)", "Plot All Operations"]
)

# Generate x values for plotting
x_values = np.linspace(-10, 10, 400)

# Initialize result and y_values for graph
y_result = None
y_values = None

# Perform selected operation and prepare for plotting
if operation == "Add":
    y_result = add(num1, num2)
    y_values = add(x_values, num2)  # Adding x values with second input for plotting
elif operation == "Subtract":
    y_result = subtract(num1, num2)
    y_values = subtract(x_values, num2)
elif operation == "Multiply":
    y_result = multiply(num1, num2)
    y_values = multiply(x_values, num2)
elif operation == "Divide":
    y_result = divide(num1, num2)
    y_values = divide(x_values, num2)
elif operation == "Power":
    y_result = power(num1, num2)
    y_values = power(x_values, num2)
elif operation == "Logarithm (num1 only)":
    y_result = log(num1)
    y_values = log(x_values)
elif operation == "Sine (num1 only)":
    y_result = sin(num1)
    y_values = sin(x_values)
elif operation == "Cosine (num1 only)":
    y_result = cos(num1)
    y_values = cos(x_values)
elif operation == "Tangent (num1 only)":
    y_result = tan(num1)
    y_values = tan(x_values)
elif operation == "Plot All Operations":
    # Plot all basic operations together on the graph
    fig, ax = plt.subplots()
    ax.plot(x_values, add(x_values, num2), label="Add")
    ax.plot(x_values, subtract(x_values, num2), label="Subtract")
    ax.plot(x_values, multiply(x_values, num2), label="Multiply")
    ax.plot(x_values, divide(x_values, num2), label="Divide")
    ax.legend()
    ax.set_title("Basic Operations: Add, Subtract, Multiply, Divide")
    ax.set_xlabel("x")
    ax.set_ylabel("Result")
    st.pyplot(fig)

# Display the result of the selected operation
if operation != "Plot All Operations" and y_result is not None:
    st.write(f"The result of {operation} is: {y_result}")

# Plot the graph for the selected operation
if operation != "Plot All Operations" and y_values is not None and st.button("Plot Graph"):
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set_title(f"Graph of {operation}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    st.pyplot(fig)
