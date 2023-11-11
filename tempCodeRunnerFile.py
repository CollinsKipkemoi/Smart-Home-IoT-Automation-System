class SmartHomeGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Smart Home IoT Simulator")
        self.geometry("400x200")
        self.configure(bg="#2b2b2b")

        # Title Label
        title_label = tk.Label(
            self,
            text="Smart Home IoT Simulator",
            font=("Helvetica", 14, "bold"),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        title_label.pack(pady=20)

        # Automation Status Button
        self.automation_status = "Off"
        automation_status_button = tk.Button(
            self,
            text="Automation: On/Off",
            font=("Helvetica", 10, "bold"),
            fg="#fb542b",
            bg="#2b2b2b",
            command=self.toggle_automation_status  # Bind the function to the button
        )
        automation_status_button.pack(pady=10)

        # Automation Status Label
        self.automation_status_label = tk.Label(
            self,
            text=f"Automation Status: {self.automation_status}",
            font=("Helvetica", 10),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        self.automation_status_label.pack(pady=10)

        # Devices Status Text Area
        self.devices_status_text = tk.Text(self, height=8, width=40)
        self.devices_status_text.pack(side=tk.BOTTOM)
        
       