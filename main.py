import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import json

# Load JSON dat
with open('Userdata.json',encoding='UTF8') as userdata_file:
    userdata = json.load(userdata_file)

with open('StreamingHistory.json',encoding='UTF8') as streaming_history_file:
    streaming_history = json.load(streaming_history_file)

with open('Inferences.json',encoding='UTF8') as inferences_file:
    inferences_data = json.load(inferences_file)

# Create a Tkinter window
root = tk.Tk()
root.title("Spotify User Data Visualization")

# Create tabs
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
notebook.add(tab1, text='User Info')
notebook.add(tab2, text='Streaming History')
notebook.add(tab3, text='Inferences')
notebook.pack()

# Tab 1: User Info
user_info_label = tk.Label(tab1, text="User Information")
user_info_label.pack()

user_info_text = tk.Text(tab1, height=10, width=40)
user_info_text.insert(tk.END, json.dumps(userdata, indent=4))
user_info_text.pack()

# Tab 2: Streaming History
streaming_history_label = tk.Label(tab2, text="Streaming History")
streaming_history_label.pack()

streaming_history_df = pd.DataFrame(streaming_history)
streaming_history_df['endTime'] = pd.to_datetime(streaming_history_df['endTime'])
streaming_history_df = streaming_history_df.sort_values(by='endTime')

fig = Figure(figsize=(8, 4))
ax = fig.add_subplot(111)
ax.plot(streaming_history_df['endTime'], streaming_history_df['msPlayed'], marker='o', linestyle='-')
ax.set_title('Streaming History')
ax.set_xlabel('Date & Time')
ax.set_ylabel('Milliseconds Played')
canvas = FigureCanvasTkAgg(fig, master=tab2)
canvas.get_tk_widget().pack()

# Tab 3: Inferences
inferences_label = tk.Label(tab3, text="User Inferences")
inferences_label.pack()

inferences_text = tk.Text(tab3, height=20, width=40)
inferences_text.insert(tk.END, '\n'.join(inferences_data['inferences']))
inferences_text.pack()

# Start the GUI main loop
root.mainloop()
