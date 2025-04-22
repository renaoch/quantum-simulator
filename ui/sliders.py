import tkinter as tk
from tkinter import ttk

def create_sliders(root, max_time, update_callback):
    slider_frame = ttk.LabelFrame(root, text='Time Controls')
    time_slider = ttk.Scale(slider_frame, from_=0, to=max_time, orient='horizontal', command=update_callback)
    time_slider.set(0)
    time_slider.pack(padx=10, pady=10)
    slider_frame.pack(side='bottom', fill='x', padx=10, pady=10)
    return time_slider
