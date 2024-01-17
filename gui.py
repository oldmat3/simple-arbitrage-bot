import tkinter as tk
import subprocess

def on_button_click():
    selected_region_value = selected_region.get()
    bet_size_value = bet_size_entry.get()

    label.config(text=f"Settings updated: Region - {selected_region_value}, Bet Size - {bet_size_value}")

    # Call arbitrage.py using subprocess
    subprocess.Popen(["python", "arbitrage.py"])

# Create the main application window
app = tk.Tk()
app.title("Chilli Odds Bot")
app.geometry("400x400")
app.configure(bg="#dcdcdc")  # Set background color to grey

# Create a label widget
label = tk.Label(app, text="Configure arbitrage bot settings", bg="#dcdcdc")
label.pack()  # Pack the label into the window

# Entry widget for API key
apikey_label = tk.Label(app, text="Enter ODDSAPI api key:", bg="#dcdcdc")
apikey_label.pack()

apikey_entry = tk.Entry(app)
apikey_entry.pack()

# Dropdown menu for regions
regions_list = ["eu", "us", "au", "uk"]
selected_region = tk.StringVar(app)
selected_region.set(regions_list[0])  # Set default region

region_label = tk.Label(app, text="Select Region:", bg="#dcdcdc")
region_label.pack()

region_dropdown = tk.OptionMenu(app, selected_region, *regions_list)
region_dropdown.pack()



# Entry widget for bet size
bet_size_label = tk.Label(app, text="Enter bet size:", bg="#dcdcdc")
bet_size_label.pack()

bet_size_entry = tk.Entry(app)
bet_size_entry.pack()

# Create a button widget
button = tk.Button(app, text="Continue", command=on_button_click)
button.pack()  # Pack the button into the window

# Start the main event loop
app.mainloop()
