class TV():
    def __init__(self,brand):
        self.brand=brand
        self.is_on=False
        self.channel = 1
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def show_status(self):
        print(f'Is tv on: {self.is_on},channel: {self.channel}')
    def channel_no(self,channel):
        self.channel=channel