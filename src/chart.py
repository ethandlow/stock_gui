import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def plot_stock_chart(data, app, parent_widget, name):
    #Create a figure and a plotting area
    fig, ax = plt.subplots()
    ax.margins(x = 0, y = 0.05)

    #plot data
    x_data = range(0, len(data.index))
    lines = ax.plot(x_data, data['Close'])
    
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    vline = ax.axvline(x = 0, ymax = 0.97, color = "grey", alpha = 0.5)

    #labels, title, and legend
    ax.set_title(name)
    plt.tight_layout()

    #embed plot into Tkinter window
    canvas = FigureCanvasTkAgg(fig, master = parent_widget)

    last_close = round(lines[0].get_data()[1][-1], 2)

    #create label for stock price
    hover_label = tk.Label(app, text = last_close, bg="white", borderwidth=1, relief="solid")
    hover_label.pack()
    hover_label.place(relx=0.1, rely=0.1)

    def on_motion(event):
        if event.inaxes:
            #update price to track while user hovers
            price = lines[0].get_data()[1][round(event.xdata)]
            hover_label.config(text = f"{round(price, 2)}")

            #update visibility and location of vertical line
            vline.set_visible(True)
            vline.set_xdata(round(event.xdata))
        else:
            hover_label.config(text = last_close)
            vline.set_visible(False)
        canvas.draw_idle()

    canvas.mpl_connect('motion_notify_event', on_motion)

    return canvas