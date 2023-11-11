import random
import time
import datetime
import json

import tkinter as tk


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
            command=self.toggle_automation_status
        )
        automation_status_button.pack(pady=10, side="top")

        # Automation Status Label
        self.automation_status_label = tk.Label(
            self,
            text=f"Automation Status: {self.automation_status}",
            font=("Helvetica", 10),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        self.automation_status_label.pack(pady=10, side="top")

        # Devices Status Text Area
        self.devices_status_text = tk.Text(self, height=8, width=40)
        self.devices_status_text.pack(side="top")

        # Create instances of devices
        self.smart_light = SmartLight("Living room light")
        self.thermostat = Thermostat("Living room thermostat")

        # StringVar to track the status
        self.smart_light_status_var = tk.StringVar()
        self.smart_light_status_var.set(f"SmartLight Status: {self.smart_light.status}")

        self.thermostat_status_var = tk.StringVar()
        self.thermostat_status_var.set(f"Thermostat Status: {self.thermostat.status}")

        # Display current devices
        self.display_current_devices()

        # Living Room Brightness Label
        living_room_brightness_label = tk.Label(
            self,
            text="Living Room Brightness",
            font=("Helvetica", 10),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        living_room_brightness_label.pack(pady=5, side="top")

        # Brightness Level Label
        self.brightness_level_label = tk.Label(
            self,
            text="Brightness Level: 0",  # Initial brightness level
            font=("Helvetica", 10),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        self.brightness_level_label.pack(pady=5, side="top")

        # Brightness Adjustment Scale
        self.brightness_scale = tk.Scale(
            self,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            length=200,
            sliderlength=15,
            command=self.update_brightness,  # Update brightness of SmartLight
        )
        self.brightness_scale.pack(pady=10)

        # Toggle On/Off Button
        toggle_button = tk.Button(
            self,
            text="Toggle On/Off",
            font=("Helvetica", 10, "bold"),
            fg="#fb542b",
            bg="#2b2b2b",
            command=self.toggle_smart_light,
        )
        toggle_button.pack(pady=10)

        # Thermostat Temperature Label
        thermostat_temperature_label = tk.Label(
            self,
            text="Thermostat Temperature",
            font=("Helvetica", 10),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        thermostat_temperature_label.pack(pady=5, side="top")

        # Temperature Level Label
        self.temperature_level_label = tk.Label(
            self,
            text="Temperature Level: 0",  # Initial temperature level
            font=("Helvetica", 10),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        self.temperature_level_label.pack(pady=5, side="top")

        # Temperature Adjustment Scale
        self.temperature_scale = tk.Scale(
            self,
            from_=0,
            to=40,
            orient=tk.HORIZONTAL,
            length=200,
            sliderlength=15,
            command=self.update_temperature,  # Update temperature of Thermostat
        )
        self.temperature_scale.pack(pady=10)

        # Toggle On/Off Button for Thermostat
        thermostat_toggle_button = tk.Button(
            self,
            text="Toggle On/Off",
            font=("Helvetica", 10, "bold"),
            fg="#fb542b",
            bg="#2b2b2b",
            command=self.toggle_thermostat,
        )
        thermostat_toggle_button.pack(pady=10)

    def update_brightness(self, value):
        self.smart_light.adjust_brightness(float(value))  # Update brightness of SmartLight
        self.brightness_level_label["text"] = f"Brightness Level: {value}"  # Update label
        self.smart_light_status_var.set(f"SmartLight Status: {self.smart_light.status}")  # Update status label
        self.update_status_textarea()  # Update status in textarea

    def toggle_smart_light(self):
        if self.smart_light.status == "On":
            self.smart_light.turn_off()
            self.smart_light.adjust_brightness(0)  # Set brightness to 0 when turned off
        else:
            self.smart_light.turn_on()

        self.smart_light_status_var.set(f"SmartLight Status: {self.smart_light.status}")  # Update status label
        self.brightness_scale.set(self.smart_light.brightness)  # Update brightness scale
        self.update_status_textarea()  # Update status in textarea

    def update_temperature(self, value):
        self.thermostat.set_temperature(float(value))  # Update temperature of Thermostat
        self.temperature_level_label["text"] = f"Temperature Level: {value}"  # Update label
        self.thermostat_status_var.set(f"Thermostat Status: {self.thermostat.status}")  # Update status label
        self.update_status_textarea()  # Update status in textarea

    def toggle_thermostat(self):
        if self.thermostat.status == "On":
            self.thermostat.turn_off()
            self.thermostat.set_temperature(0)  # Set temperature to 0 when turned off
        else:
            self.thermostat.turn_on()

        self.thermostat_status_var.set(f"Thermostat Status: {self.thermostat.status}")  # Update status label
        self.temperature_scale.set(self.thermostat.temperature)  # Update temperature scale
        self.update_status_textarea()  # Update status in textarea

    def update_status_textarea(self):
        self.devices_status_text.delete(1.0, tk.END)
        devices = [self.smart_light, self.thermostat]
        for device in devices:
            status_info = f"{device.id}: {device.device_type}    Status: {device.status}"

            if isinstance(device, SmartLight):
                status_info += f"    Brightness: {device.brightness}"
            elif isinstance(device, Thermostat):
                status_info += f"    Temperature: {device.temperature}"

            self.devices_status_text.insert(tk.END, status_info + "\n")

    def toggle_automation_status(self):
        if self.automation_status == "Off":
            self.automation_status = "On"
        else:
            self.automation_status = "Off"
        self.automation_status_label["text"] = f"Automation Status: {self.automation_status}"
        self.display_current_devices()

    def display_current_devices(self):
        self.devices_status_text.delete(1.0, tk.END)
        devices = [self.smart_light, self.thermostat]
        for device in devices:
            self.devices_status_text.insert(tk.END, f"{device.id}: {device.device_type}    Status: {device.status}\n")


class Device:
    def __init__(self, device_id: str):
        self.__device_id = device_id
        self.__status = "off"

    @property
    def status(self):
        return self.__status

    @property
    def id(self):
        return self.__device_id

    def turn_on(self):
        if self.__status == "off":
            self.__status = "on"

    def turn_off(self):
        if self.__status == "on":
            self.__status = "off"


class SmartLight(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.__brightness = 0
        self.__device_type = "SmartLight"

    @property
    def brightness(self):
        return self.__brightness

    @property
    def device_type(self):  # Add this property
        return self.__device_type

    def log_data(self):
        data = self.get_data()
        with open("sensor_data.json", "a") as f:
            json.dump(data, f)
            f.write("\n")

    def adjust_brightness(self, brightness: float):
        if brightness > 100 or brightness < 0:
            raise LightException(
                "Brightness level cannot be more than 100 or less than 0"
            )
        if brightness > 0:
            self.turn_on()
        self.__brightness = brightness
        if brightness == 0:
            self.turn_off()
        self.log_data()

    def gradual_dimming(self, target_brightness: int, duration: float):
        if target_brightness > self.brightness:
            raise LightException(
                "The target brightness cannot be greater than the brightness of the device"
            )
        elif target_brightness < 0:
            raise LightException("Target brightness cannot be less than 0")
        else:
            steps = (self.brightness - target_brightness) / duration
            while self.brightness > target_brightness:
                self.adjust_brightness(self.brightness - steps)
                time.sleep(1)
                self.log_data()
                print(self.__str__())

    def __str__(self) -> str:
        return f"Device: Smart Light Device Id: {self.id} Brightness: {self.brightness} Status: {self.status}"

    def get_data(self):
        return f"time: {datetime.datetime.now().isoformat()}  device_id: {self.id} status: {self.status} brightness:  {self.brightness}"


class Thermostat(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.temperature = 0
        self.__device_type = "Thermostat"

    def set_temperature(self, temp):
        if temp > 40 or temp < 0:
            raise ValueError("Temperature cannot be more than 40 or less than 0")
        else:
            if temp > 0:
                self.turn_on()
                self.temperature = temp
                self.log_data()
            else:
                self.turn_off()
                self.temperature = temp
                self.log_data()

    @property
    def device_type(self):  # Add this property
        return self.__device_type

    def log_data(self):
        data = self.get_data()
        with open("sensor_data.json", "a") as f:
            json.dump(data, f)
            f.write("\n")

    def get_data(self):
        return f"time: {datetime.datetime.now().isoformat()} device_id: {self.id} status: {self.status}  temperature: {self.temperature}"

    def __str__(self):
        return f"Device: Thermostat Device Id: {self.id} Temperature: {self.temperature} Status: {self.status}"


class SecurityCamera(Device):
    def __init__(self, device_id: str):
        super().__init__(device_id)
        self.__securityStatus = "No motion"

    def get_security_status(self):
        return self.__securityStatus

    def set_security_status(self, status):
        self.__securityStatus = status
        self.log_data()

    def log_data(self):
        data = self.get_data()
        with open("sensor_data.json", "a") as f:
            json.dump(data, f)
            f.write("\n")

    def get_data(self):
        return f"time: {datetime.datetime.now().isoformat()} device_id: {self.id} status: {self.status} security_status: {self.get_security_status()}"

    def __str__(self):
        return f"Device: Security Camera Device Id: {self.id} Security Status: {self.__securityStatus} Status: {self.status}"


class AutomationSystem:
    def __init__(self):
        self.cameras = []
        self.thermostats = []
        self.lights = []

    def discover_devices(self):
        pass

    def add_device(self, device: Device):
        if isinstance(device, SecurityCamera):
            self.cameras.append(device)
        elif isinstance(device, Thermostat):
            self.thermostats.append(device)
        elif isinstance(device, SmartLight):
            self.lights.append(device)

    def turn_lights_automatically(self, camera_id):
        for camera in self.cameras:
            if camera.id() == camera_id:
                if camera.get_security_status() == "Detected motion":
                    for light_bulb in self.lights:
                        light_bulb.turn_on()
                else:
                    for light_bulb in self.lights:
                        light_bulb.turn_off()

    def randomization(self):
        for dev in self.lights and self.cameras:
            if isinstance(SmartLight, dev):
                brightness = random.randint(0, 100)
                dev.adjust_brightness(brightness)

            elif isinstance(Thermostat, dev):
                temp = random.randint(0, 100)
                dev.set_temperature(temp)

            elif isinstance(SecurityCamera, dev):
                status = random.choice(["Detected motion", "No motion"])
                dev.set_security_status(status)


class LightException(Exception):
    pass


gui = SmartHomeGUI()
gui.mainloop()
