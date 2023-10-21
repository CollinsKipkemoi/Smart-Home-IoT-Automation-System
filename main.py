import random


class Device:
    def __init__(self, device_id: str):
        self.__device_id = device_id
        self.__status = "off"

    def get_status(self):
        return self.__status

    def get_id(self):
        return self.__device_id

    def turn_on(self):
        if self.__status == "off":
            self.__status = "on"

    def turn_off(self):
        if self.__status == "on":
            self.__status = "off"


class SmartLight(Device):
    def __init__(self, device_id, brightness):
        super().__init__(device_id)
        self.__brightness = brightness

    def get_brightness(self):
        return self.__brightness

    def adjust_brightness(self, brightness):
        self.__brightness = brightness


class Thermostat(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.temperature = 0

    def set_temperature(self, temp):
        self.temperature = temp


class SecurityCamera(Device):
    def __init__(self, device_id: str):
        super().__init__(device_id)
        self.__securityStatus = "No motion"

    def get_security_status(self):
        return self.__securityStatus

    def set_security_status(self, status):
        self.__securityStatus = status


class AutomationSystem:
    def __init__(self):
        self.__cameras = []
        self.__thermostats = []
        self.__lights = []

    def discover_devices(self):
        pass

    def add_camera(self, cam: SecurityCamera):
        self.__cameras.append(cam)

    def add_light(self, light: SmartLight):
        self.__lights.append(light)

    def add_thermostat(self, thermostat: Thermostat):
        self.__thermostats.append(thermostat)

    def turn_lights_automatically(self, camera_id):
        for camera in self.__cameras:
            if camera.get_id() == camera_id:
                if camera.get_security_status() == "Detected motion":
                    for light in self.__lights:
                        light.turn_on()
                else:
                    for light in self.__lights:
                        light.turn_off()

    def randomization(self):
        for dev in self.__lights and self.__cameras:
            if isinstance(SmartLight, dev):
                brightness = random.randint(0, 100)
                dev.adjust_brightness(brightness)

            elif isinstance(Thermostat, dev):
                temp = random.randint(0, 100)
                dev.set_temperature(temp)

            elif isinstance(SecurityCamera, dev):
                status = random.choice(["Detected motion", "No motion"])
                dev.set_security_status(status)
