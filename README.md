# Simple Bank Management System (Streamlit)

A simple **Bank Management System** built using **Python and Streamlit**, allowing users to create bank accounts and perform basic banking operations such as deposit, withdrawal, updating details, and account deletion.  
All user data is stored locally using a JSON file.


## Project Overview

This project simulates a basic banking system with a **user-friendly web interface** built using Streamlit.  
It demonstrates how core banking operations can be implemented using **object-oriented programming**, file handling, and a frontend UI.


##  Features

- Create a new bank account  
- Secure login using Account Number & PIN  
- Deposit money (with limits)  
- Withdraw money (balance-checked)  
- View account details  
- Update user information  
- Delete bank account  
- Persistent storage using `data.json`


# Simple Bank Management System (Streamlit)

A simple **Bank Management System** built using **Python and Streamlit**, allowing users to create bank accounts and perform basic banking operations such as deposit, withdrawal, updating details, and account deletion.  
All user data is stored locally using a JSON file.


##  Project Overview

This project simulates a basic banking system with a **user-friendly web interface** built using Streamlit.  
It demonstrates how core banking operations can be implemented using **object-oriented programming**, file handling, and a frontend UI.


## Features

- Create a new bank account  
- Secure login using Account Number & PIN  
- Deposit money (with limits)  
- Withdraw money (balance-checked)  
- View account details  
- Update user information  
- Delete bank account  
- Persistent storage using `data.json`



##  Project Structure

##  Backend Logic (Bank Class)

The `Bank` class handles:
- Account creation with validation
- Secure PIN-based authentication
- Deposit & withdrawal rules
- Data persistence using JSON
- Account updates and deletion

All operations update the `data.json` file in real time.

## Frontend (Streamlit)

The Streamlit UI provides:
- Sidebar-based navigation
- Input forms for all banking actions
- Success and error feedback messages
- Clean and simple user experience


## Account Rules & Validation

- Minimum age: **18 years**
- PIN must be **4 digits**
- Deposit limit: **1 to 10,000**
- Withdrawal limited to available balance
- Unique auto-generated account numbers


##  How to Run the Project

### Install Dependencies
```bash
pip install -r requirements.txt
streamlit run app.py
## Dependencies 
streamlit
pandas
numpy


