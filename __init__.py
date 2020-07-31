from mycroft import MycroftSkill, intent_file_handler
import serial

class ReadArduinoPot(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pot.arduino.read.intent')
    def handle_pot_arduino_read(self, message):
        ser = serial.Serial('/dev/ttyUSB0', 115200)
        self.sensor_reading=(ser.readline()).decode('utf-8')
        datadic = {"reading": self.sensor_reading}
        self.log.info("THE SENSOR READING IS " + str(self.sensor_reading))
        self.speak_dialog('pot.arduino.read', datadic)


def create_skill():
    return ReadArduinoPot()

