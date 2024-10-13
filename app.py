{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMT8hkFT18ZpI0Rd7h8MKA+",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mehtabahmed9/Scientific-Calculator/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tg5eCJLGdmmE",
        "outputId": "b218d720-02b1-4c27-dcb6-64a00e9f0f42"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Select operation:\n",
            "1. Add\n",
            "2. Subtract\n",
            "3. Multiply\n",
            "4. Divide\n",
            "Enter choice (1/2/3/4): 3\n",
            "Enter first number: 6\n",
            "Enter second number: 9\n",
            "6.0 * 9.0 = 54.0\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "\n",
        "# Function for addition\n",
        "def add(x, y):\n",
        "    return x + y\n",
        "\n",
        "# Function for subtraction\n",
        "def subtract(x, y):\n",
        "    return x - y\n",
        "\n",
        "# Function for multiplication\n",
        "def multiply(x, y):\n",
        "    return x * y\n",
        "\n",
        "# Function for division\n",
        "def divide(x, y):\n",
        "    if y != 0:\n",
        "        return x / y\n",
        "    else:\n",
        "        return \"Cannot divide by zero!\"\n",
        "\n",
        "# Streamlit app layout\n",
        "st.title(\"Simple Calculator\")\n",
        "\n",
        "# User input for numbers\n",
        "num1 = st.number_input(\"Enter first number\", format=\"%.2f\")\n",
        "num2 = st.number_input(\"Enter second number\", format=\"%.2f\")\n",
        "\n",
        "# Selection of operation\n",
        "operation = st.selectbox(\"Select Operation\", (\"Add\", \"Subtract\", \"Multiply\", \"Divide\"))\n",
        "\n",
        "# Perform calculation based on user input\n",
        "if st.button(\"Calculate\"):\n",
        "    if operation == \"Add\":\n",
        "        result = add(num1, num2)\n",
        "    elif operation == \"Subtract\":\n",
        "        result = subtract(num1, num2)\n",
        "    elif operation == \"Multiply\":\n",
        "        result = multiply(num1, num2)\n",
        "    elif operation == \"Divide\":\n",
        "        result = divide(num1, num2)\n",
        "\n",
        "    # Display the result\n",
        "    st.write(f\"The result is: {result}\")\n"
      ]
    }
  ]
}