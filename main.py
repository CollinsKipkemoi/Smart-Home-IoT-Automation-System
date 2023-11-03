import random
import time


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

    @property
    def brightness(self):
        return self.__brightness

    def adjust_brightness(self, brightness: int):
        if brightness > 100 or brightness < 0:
            raise LightException(
                "Brightness level cannot be more than 100 or less than 0"
            )
        if brightness > 0:
            self.turn_on()
        self.__brightness = brightness
        if brightness == 0:
            self.turn_off()

    def gradual_dimming(self, target_brightness: int, duration: float):
        if target_brightness > self.brightness:
            raise LightException("The target brightness cannot be greater than the brightness of the device")
        elif target_brightness < 0:
            raise LightException("Target brightness cannot be less than 0")
        else:
            steps = (self.brightness - target_brightness) / duration
            while self.brightness > target_brightness:
                self.adjust_brightness(self.brightness - steps)
                time.sleep(1)
                print(self.__str__())

    def __str__(self) -> str:
        return f"Device: Smart Light Device Id: {self.id} Brightness: {self.brightness} Status: {self.status}"


class Thermostat(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.temperature = 0

    def set_temperature(self, temp):
        if temp > 40 or temp < 0:
            raise ValueError("Temperature cannot be more than 40 or less than 0")
        else:
            if temp > 0:
                self.turn_on()
                self.temperature = temp
            else:
                self.turn_off()
                self.temperature = temp

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


auto = AutomationSystem()
cam = SecurityCamera("Camera1")
light = SmartLight("Light1")
thermo = Thermostat("Thermostat1")
# print(light.__str__())
# light.adjust_brightness(40)
# print(light.__str__())
# light.adjust_brightness(0)
# print(light.__str__())

# auto.add_device(cam)
# auto.add_device(light)
# auto.add_device(thermo)

print(light.__str__())
light.adjust_brightness(30)
print(light.__str__())
light.gradual_dimming(0, 10)
