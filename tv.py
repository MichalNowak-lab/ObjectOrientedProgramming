class TV():
    def __init__(self,brand):
        self.brand=brand
        self.is_on=False
        self.channel = 1
        self.channels = []
        self.volume = 0
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def show_status(self):
        if self.channels:
            if self.channel-1<=len(self.channels):
                print(f'Is tv on: {self.is_on},channel: {self.channel} ({self.channels[self.channel-1]}),volume: {self.volume}')
            else:
                print(f'Is tv on: {self.is_on},channel: {self.channel},volume: {self.volume}')
        else:
            print(f'Is tv on: {self.is_on},channel: {self.channel},volume: {self.volume}')

    def channel_no(self,channel):
        self.channel=channel
    def set_channels(self,channel_list):
        self.channels=channel_list
    def show_channels(self):
        print('Channel list:')
        i=1
        if self.channels:
            for channel in self.channels:
                print(i,channel)
                i+=1
        else:
            print(self.channels)
    def increase_vol(self):
        if self.volume<10:
            self.volume+=1
    def decrease_vol(self):
        if self.volume >0:
            self.volume -= 1