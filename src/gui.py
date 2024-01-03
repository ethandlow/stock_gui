import tkinter as tk
from stock import fetch_stock_data
from analysis import simple_moving_average
from chart import plot_stock_chart

def setup_gui(app, on_search_click, update_time_frame):
    label = tk.Label(app, text = "Enter Stock Symbol: ")
    label.pack()

    entry = tk.Entry(app)
    entry.pack()

    button = tk.Button(app, text = "Search", command = lambda: on_search_click(ticker = entry.get()))
    button.pack()

    global plot_frame
    plot_frame = tk.Frame(app)
    plot_frame.pack()

    global plot_canvas
    plot_canvas = None

    tf_button_frame = tk.Frame(app)
    tf_button_frame.pack(side = "bottom", anchor = "sw")

    tf_buttons = ["1D", "1W", "1M", "3M", "YTD", "1Y", "5Y", "MAX"]
    for tf in tf_buttons:
        time_frame = tf
        match tf:
            case "1D":
                interval = "5m"
            case "1W":
                time_frame = "5d"
                interval = "1h"
            case "1M":
                time_frame = "1mo"
                interval = "1h"
            case "3M":
                time_frame = "3mo"
                interval = "1d"
            case "YTD":
                interval = "1d"
            case "1Y":
                interval = "1d"
            case "5Y":
                interval = "1wk"
            case "MAX":
                interval = "1mo"
        button = tk.Button(app, text = tf, 
                           command = lambda time_frame = time_frame.lower(), interval = interval: 
                           update_time_frame(ticker = entry.get(), time_frame = time_frame, interval = interval))
        button.pack(side = "left")    

    return entry

def update_plot(data, app, name):
    global plot_frame
    global plot_canvas

    if plot_canvas is not None:
        plot_canvas.get_tk_widget().destroy()

    # Create a new plot canvas
    plot_canvas = plot_stock_chart(data, app, plot_frame, name)

    # Add the canvas to the GUI using the grid system
    canvas_widget = plot_canvas.get_tk_widget()
    canvas_widget.pack()

    plot_canvas.draw()
