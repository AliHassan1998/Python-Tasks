from smart_device_inspector.smart_device_inspector import Device, SmartPhone

d1 = Device("D101", "Dell", 1500)

s1 = SmartPhone("S201", "Apple", 2200, 8, 256)

assert len(d1) == len("Dell")
assert "install_app" in dir(s1)
assert s1.install_app("WhatsApp") is not None
