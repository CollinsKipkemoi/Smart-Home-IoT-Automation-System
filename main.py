import random
import time
import datetime
import json

import tkinter as tk


class SmartHomeGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Smart Home IoT Simulator")
        self.geometry("800x1000")
        self.configure(bg="#2b2b2b")

        title_label = tk.Label(
            self,
            text="Smart Home IoT Simulator",
            font=("Helvetica", 14, "bold"),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        title_label.pack(pady=20)

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

        self.automation_status_label = tk.Label(
            self,
            text=f"Automation Status: {self.automation_status}",
            font=("Helvetica", 10),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        self.automation_status_label.pack(pady=10, side="top")

        self.devices_status_text = tk.Text(self, height=8, width=40)
        self.devices_status_text.pack(side="top")

        self.smart_light = SmartLight("Living room light")
        self.thermostat = Thermostat("Living room thermostat")
        self.security_camera = SecurityCamera("Main entrance camera")

        self.smart_light_status_var = tk.StringVar()
        self.smart_light_status_var.set(f"SmartLight Status: {self.smart_light.status}")

        self.thermostat_status_var = tk.StringVar()
        self.thermostat_status_var.set(f"Thermostat Status: {self.thermostat.status}")

        self.display_current_devices()

        living_room_brightness_label = tk.Label(
            self,
            text="Living Room Brightness",
            font=("Helvetica", 10),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        living_room_brightness_label.pack(pady=5, side="top")

        self.brightness_level_label = tk.Label(
            self,
            text="Brightness Level: 0",
            font=("Helvetica", 10),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        self.brightness_level_label.pack(pady=5, side="top")

        self.brightness_scale = tk.Scale(
            self,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            length=200,
            sliderlength=15,
            command=self.update_brightness,
        )
        self.brightness_scale.pack(pady=10)

        toggle_button = tk.Button(
            self,
            text="Toggle On/Off",
            font=("Helvetica", 10, "bold"),
            fg="#fb542b",
            bg="#2b2b2b",
            command=self.toggle_smart_light,
        )
        toggle_button.pack(pady=10)

        thermostat_temperature_label = tk.Label(
            self,
            text="Thermostat Temperature",
            font=("Helvetica", 10),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        thermostat_temperature_label.pack(pady=5, side="top")

        self.temperature_level_label = tk.Label(
            self,
            text="Temperature Level: 0",
            font=("Helvetica", 10),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        self.temperature_level_label.pack(pady=5, side="top")

        self.temperature_scale = tk.Scale(
            self,
            from_=0,
            to=40,
            orient=tk.HORIZONTAL,
            length=200,
            sliderlength=15,
            command=self.update_temperature,
        )
        self.temperature_scale.pack(pady=10)

        thermostat_toggle_button = tk.Button(
            self,
            text="Toggle On/Off",
            font=("Helvetica", 10, "bold"),
            fg="#fb542b",
            bg="#2b2b2b",
            command=self.toggle_thermostat,
        )
        thermostat_toggle_button.pack(pady=10)

        security_camera_status_label = tk.Label(
            self,
            text="Security Camera Status",
            font=("Helvetica", 10),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        security_camera_status_label.pack(pady=5, side="top")

        self.motion_status_label = tk.Label(
            self,
            text="Motion Status: No motion",
            font=("Helvetica", 10),
            fg="#fb542b",
            bg="#2b2b2b",
        )
        self.motion_status_label.pack(pady=5, side="top")

        motion_button = tk.Button(
            self,
            text="Random Detect Motion",
            font=("Helvetica", 10, "bold"),
            fg="#fb542b",
            bg="#2b2b2b",
            command=self.toggle_motion,
        )
        motion_button.pack(pady=10)

        security_camera_toggle_button = tk.Button(
            self,
            text="Toggle On/Off",
            font=("Helvetica", 10, "bold"),
            fg="#fb542b",
            bg="#2b2b2b",
            command=self.toggle_security_camera,
        )
        security_camera_toggle_button.pack(pady=10)

        self.sensor_data_text = tk.Text(self, height=8, width=40)
        self.sensor_data_text.pack(side="top")

        self.security_camera_status_var = tk.StringVar()
        self.security_camera_status_var.set("Off")

    def log_sensor_data(self, device):
            data = device.get_data()
            self.sensor_data_text.insert(tk.END, f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {data}\n")
            self.sensor_data_text.yview(tk.END)

    def update_brightness(self, value):
        self.smart_light.adjust_brightness(float(value))
        self.brightness_level_label["text"] = f"Brightness Level: {value}"
        self.smart_light_status_var.set(f"SmartLight Status: {self.smart_light.status}")
        self.update_status_textarea()
        self.log_sensor_data(self.smart_light)

    def toggle_smart_light(self):
        if self.smart_light.status == "on":
            self.smart_light.turn_off()
            self.smart_light.adjust_brightness(0)
        else:
            self.smart_light.turn_on()

        self.smart_light_status_var.set(f"SmartLight Status: {self.smart_light.status}")
        self.brightness_scale.set(self.smart_light.brightness)
        self.update_status_textarea()
        self.log_sensor_data(self.smart_light)

    def update_temperature(self, value):
        self.thermostat.set_temperature(float(value))
        self.temperature_level_label["text"] = f"Temperature Level: {value}"
        self.thermostat_status_var.set(f"Thermostat Status: {self.thermostat.status}")
        self.update_status_textarea()
        self.log_sensor_data(self.thermostat)

    def toggle_thermostat(self):
        if self.thermostat.status == "on":
            self.thermostat.turn_off()
            self.thermostat.set_temperature(0)
        else:
            self.thermostat.turn_on()

        self.thermostat_status_var.set(f"Thermostat Status: {self.thermostat.status}")
        self.temperature_scale.set(self.thermostat.temperature)
        self.update_status_textarea()
        self.log_sensor_data(self.thermostat)

    def toggle_automation_status(self):
        if self.automation_status == "Off":
            self.automation_status = "On"
        else:
            self.automation_status = "Off"
        self.automation_status_label["text"] = f"Automation Status: {self.automation_status}"
        self.display_current_devices()

    def toggle_security_camera(self):
        if self.security_camera.status == "On":
            self.security_camera.turn_off()
            self.security_camera.set_security_status("No motion")
        else:
            self.security_camera.turn_on()

        self.security_camera_status_var.set(
            "On" if self.security_camera.status == "on" else "Off"
        )
        self.update_status_textarea()
        self.log_sensor_data(self.security_camera)

    def toggle_motion(self):
        status = random.choice(["Detected motion", "No motion"])
        self.security_camera.set_security_status(status)

        self.motion_status_label["text"] = f"Motion Status: {status}"
        self.update_status_textarea()
        self.log_sensor_data(self.security_camera)

    def display_current_devices(self):
        self.devices_status_text.delete(1.0, tk.END)
        devices = [self.smart_light, self.thermostat]
        for device in devices:
            self.devices_status_text.insert(tk.END, f"{device.id}: {device.device_type}    Status: {device.status}\n")

    def update_status_textarea(self):
        self.devices_status_text.delete(1.0, tk.END)
        devices = [self.smart_light, self.thermostat, self.security_camera]
        for device in devices:
            status_info = f"{device.id}: {device.device_type}    Status: {device.status}"

            if isinstance(device, SmartLight):
                status_info += f"    Brightness: {device.brightness}"
            elif isinstance(device, Thermostat):
                status_info += f"    Temperature: {device.temperature}"
            elif isinstance(device, SecurityCamera):
                status_info += f"    Security Status: {device.get_security_status()}"

            self.devices_status_text.insert(tk.END, status_info + "\n")


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
    def device_type(self):
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
    def device_type(self):
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
        self.__device_type = "SecurityCamera"

    @property
    def device_type(self):
        return self.__device_type

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
