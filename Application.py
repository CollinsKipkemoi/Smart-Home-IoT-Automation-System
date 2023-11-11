import tkinter as tk
from main import SmartLight

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.light = SmartLight("Light1")

        self.status_label = tk.Label(self, text="Status: " + self.light.status)
        self.status_label.pack()

        self.brightness_label = tk.Label(self, text="Brightness: " + str(self.light.brightness))
        self.brightness_label.pack()

        self.on_button = tk.Button(self)
        self.on_button["text"] = "Turn On"
        self.on_button["command"] = self.turn_on
        self.on_button.pack(side="left")

        self.off_button = tk.Button(self)
        self.off_button["text"] = "Turn Off"
        self.off_button["command"] = self.turn_off
        self.off_button.pack(side="right")

    def turn_on(self):
        self.light.turn_on()
        self.update_labels()

    def turn_off(self):
        self.light.turn_off()
        self.update_labels()

    def update_labels(self):
        self.status_label["text"] = "Status: " + self.light.status
        self.brightness_label["text"] = "Brightness: " + str(self.light.brightness)

root = tk.Tk()
root.title("Smart Home IoT Simulator")
app = Application(master=root)
app.mainloop()