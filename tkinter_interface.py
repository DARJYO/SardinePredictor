import tkinter as tk
from tkinter import messagebox
import joblib

# Load the trained model
model = joblib.load('sardine_predictor_model.pkl')

def predict_sardines():
    try:
        temperature = float(temp_entry.get())
        salinity = float(sal_entry.get())
        
        prediction = model.predict([[temperature, salinity]])
        
        if prediction[0] == 1:
            result = "Sardines are likely to be present."
        else:
            result = "Sardines are unlikely to be present."
        
        messagebox.showinfo("Prediction Result", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Creating the Tkinter Window
root = tk.Tk()
root.title("Sardine Predictor")

# Temperature Input
tk.Label(root, text="Sea Temperature (°C)").grid(row=0, column=0)
temp_entry = tk.Entry(root)
temp_entry.grid(row=0, column=1)

# Salinity Input
tk.Label(root, text="Salinity (PSU)").grid(row=1, column=0)
sal_entry = tk.Entry(root)
sal_entry.grid(row=1, column=1)

# Predict Button
predict_button = tk.Button(root, text="Predict", command=predict_sardines)
predict_button.grid(row=2, column=0, columnspan=2)

# Run the application
root.mainloop()
