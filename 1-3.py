class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    def print_receipt(self):
        print(f'distance: {self.distance}, rate: {self.rate_per_km}, fare: {self.fare}')

def main():
    # your program
    driver1= TaxiRide(2)
    driver2=TaxiRide(4)
    driver1.fare=29
    driver1.distance=200
    driver2.fare = 31
    driver2.distance = 100
    driver1.print_receipt()
    driver2.print_receipt()

if __name__ == "__main__":
    main()