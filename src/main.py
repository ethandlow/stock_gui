import tkinter as tk
from gui import setup_gui, update_plot
from stock import fetch_stock_data, fetch_company_name
from analysis import simple_moving_average


def update_time_frame(ticker, time_frame, interval):
    #print(time_frame)
    data = fetch_stock_data(ticker, period = time_frame, interval = interval)
    name = fetch_company_name(ticker)

    update_plot(data, app, name)

def on_search_click(ticker):
    data = fetch_stock_data(ticker, period = "1d", interval = "5m")
    name = fetch_company_name(ticker)
    
    update_plot(data, app, name)

def on_close():
    app.quit()
    app.destroy()

def main():
    global app
    app = tk.Tk()
    app.title("Stock Analaysis Tool")

    setup_gui(app, on_search_click, update_time_frame)
    #on_search_click("SPY")
    
    app.protocol("WM_DELETE_WINDOW", on_close)

    app.mainloop()

if __name__ == "__main__":
    main()