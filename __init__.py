from mycroft import MycroftSkill, intent_file_handler


class ReadArduinoPot(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pot.arduino.read.intent')
    def handle_pot_arduino_read(self, message):
        self.speak_dialog('pot.arduino.read')


def create_skill():
    return ReadArduinoPot()

