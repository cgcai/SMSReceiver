from serial import Serial, SerialException


class ModemNotOpenException(Exception):
    pass


class SMSModem(object):
    def __init__(self, device, timeout=5):  # timeout in seconds
        self.device = Serial(device)
        self.read_timeout = timeout
        self.is_open = False

    def __send_serial_command(self, command):
        if not self.is_open:
            raise ModemNotOpenException()

        # TODO: Logic. Need to read AT+Command spec.

    def open(self):
        if not self.device.is_open:
            self.device.open()
            self.is_open = True

    def close(self):
        if self.device.is_open:
            self.device.close()
            self.is_open = False
