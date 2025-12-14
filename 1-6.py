class Phone():
    def __init__(self,charge,state,inUse):
        self.charge = charge
        self.state=state
        self.inUse=inUse
    def changeState(self,state):
        self.state=state
        print(f'Phone is now {self.state}')
    def changeBattery(self,charge):
        self.charge=charge
        print(f'Battery {charge}%')
    def isInUse(self,inUse):
        self.inUse=inUse
        print(f'Phone in use: {inUse}')
def main():
    phone=Phone('87%','Turned on', True)
    print(f'Battery {phone.charge}')
    print(f'State: {phone.state}')
    print(f'In use: {phone.inUse}')
main()