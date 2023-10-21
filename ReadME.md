## SMART HOME IoT AUTOMATION SIMULATOR

This is a Python implementation of an IoT automation system that manages and controls various devices such as smart lights, thermostats, and security cameras. The system provides methods for discovering devices, adding them to the system, and executing automation tasks, such as turning on lights automatically when motion is detected.

## Requirements

```markdown
1. python 3.x
2. random module
```

## Usage

To use the IoT automation system, you can create a new instance of the AutomationSystem class and use its methods to manage and control devices. Here's an example:

```python
from main import AutomationSystem, SmartLight, Thermostat, SecurityCamera

# Create a new instance of the AutomationSystem class
my_system = AutomationSystem()

# Add devices to the system
my_system.add_camera(SecurityCamera("camera1"))
my_system.add_light(SmartLight("light1", 50))
my_system.add_thermostat(Thermostat("thermostat1"))

# Turn lights on automatically based on camera motion detection
my_system.turn_lights_automatically("camera1")

# Randomize device states
my_system.randomization()
```

In this example, we create a new instance of the AutomationSystem class and add some devices to the system. We then call the turn_lights_automatically() method to turn lights on or off based on camera motion detection, and the randomization() method to simulate changing device states over time.

## Classes

### Device

The Device class is the base class for all devices in the system. It provides methods for getting and setting the device status and ID.

### SmartLight

The SmartLight class is a subclass of the Device class. It provides methods for getting and setting the light brightness.

### Thermostat

The Thermostat class is a subclass of the Device class. It provides methods for getting and setting the thermostat temperature.

### SecurityCamera

The SecurityCamera class is a subclass of the Device class. It provides methods for getting and setting the camera status.

### AutomationSystem

The AutomationSystem class provides methods for managing and controlling devices in the system. It also provides methods for discovering devices, adding them to the system, and executing automation tasks, such as turning on lights automatically when motion is detected.

## Developer

code by : [Collins Kipkemoi]
