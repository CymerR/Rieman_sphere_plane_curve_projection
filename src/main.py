import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def parabola():
    X, Y = [], []

    for ind in range(0, 25+1):
        # parabola on [-4, 4]
        x = -4 + 8.0 / 25 * ind
        y = x**2
        X.append(x)
        Y.append(y)
    return X, Y

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Matplotlib в Tkinter")
        self.geometry("800x600")

        # Создаем панель (Frame) для графика
        self.panel = ttk.Frame(self)
        self.panel.pack(fill=tk.BOTH, expand=True)

        # Создаем фигуру Matplotlib
        self.figure = Figure(figsize=(4,3), dpi=100)
        self.ax = self.figure.add_subplot(111)
        x, y = parabola()
        self.ax.plot(x, y)

        # Встраиваем график в Tkinter-панель
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.panel)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Добавляем тулбар
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.panel)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()



