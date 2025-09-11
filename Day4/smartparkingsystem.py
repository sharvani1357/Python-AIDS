from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self, license_plate, ownername,spotStatus):
        self.__license_plate = license_plate
        self.__ownername = ownername
        self.__spotStatus=spotStatus
    def get(self):
        return f"License Plate: {self.__license_plate}, Owner Name: {self.__ownername}, Spot Status: {self.__spotStatus}"
    def set(self,license_plate,ownername,spotStatus):
        self.__license_plate = license_plate
        self.__ownername = ownername
        self.__spotStatus=spotStatus
    def display(self):
        self.get()
    def calculate_parking_fee(self,hours):
        pass
class Bike(Vehicle):
    def __init__(self, license_plate, ownername,spotStatus,helmet_required):
        super().__init__(license_plate, ownername,spotStatus)
        self.helmet_required=helmet_required
    def display(self):
        super().display()
        print(f"helmet_required {self.helmet_required}")
    def calculate_parking_fee(self,hours):
        #20 per hour
        print(f"Parking fee for Bike: ₹{20*hours}")
class Car(Vehicle):
    def __init__(self, license_plate, ownername,spotStatus,seats):
        super().__init__(license_plate, ownername,spotStatus)
        self.seats=seats
    def display(self):
        super().display()
        print(f"seats: {self.seats}")
    def calculate_parking_fee(self,hours):
        #50 per hour
        print(f"Parking fee for Bike: ₹{50*hours}")
class SUV(Vehicle):
    def __init__(self, license_plate, ownername,spotStatus,four_wheel_drive):
        super().__init__(license_plate, ownername,spotStatus)
        self.four_wheel_drive=four_wheel_drive
    def display(self):
        super().display()
        print(f"four_wheel_drive: {self.four_wheel_drive}")
    def calculate_parking_fee(self,hours):
        #70 per hour
        print(f"Parking fee for Bike: ₹{70*hours}")

class Truck(Vehicle):
    def __init__(self, license_plate, ownername,spotStatus,max_load_capacity):
        super().__init__(license_plate, ownername,spotStatus)
        self.max_load_capacity=max_load_capacity
    def display(self):
        super().display()
        print(f"max_load_capacity: {self.max_load_capacity}")
    def calculate_parking_fee(self,hours):
        #100 per hour
        print(f"Parking fee for Bike: ₹{100*hours}")

class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size  # S, M, L, XL
        self.vehicle = None  # No vehicle assigned initially
    def assign_vehicle(self, vehicle):
        if self.is_vehicle_fit(vehicle):
            self.vehicle = vehicle
            print(f"Vehicle {vehicle.get()} assigned to Spot {self.spot_id}")
        else:
            print(f"Vehicle {vehicle.get()} does not fit in Spot {self.spot_id} of size {self.size}")
    def remove_vehicle(self):
        if self.vehicle:
            print(f"Vehicle {self.vehicle.get()} removed from Spot {self.spot_id}")
            self.vehicle = None
        else:
            print(f"No vehicle to remove from Spot {self.spot_id}")
    def is_vehicle_fit(self, vehicle):
        if isinstance(vehicle, Bike) and self.size in ["S", "M", "L", "XL"]:
            return True
        elif isinstance(vehicle, Car) and self.size in ["M", "L", "XL"]:
            return True
        elif isinstance(vehicle, SUV) and self.size in ["L", "XL"]:
            return True
        elif isinstance(vehicle, Truck) and self.size == "XL":
            return True
        return False
    def display(self):
        status = "Empty" if not self.vehicle else f"Occupied by {self.vehicle.get()}"
        print(f"Spot {self.spot_id} ({self.size}): {status}")

class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []
    def add_spot(self, spot):
        self.spots.append(spot)
        print(f"Spot {spot.spot_id} of size {spot.size} added to Parking Lot {self.name}")
    def show_spots(self):
        print(f"Parking Status for {self.name}:")
        for spot in self.spots:
            spot.display()
    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if not spot.vehicle and spot.is_vehicle_fit(vehicle):
                spot.assign_vehicle(vehicle)
                return
        print(f"No suitable spot available for vehicle {vehicle.get()}")
    def unpark_vehicle(self, vehicle, hours):
        for spot in self.spots:
            if spot.vehicle == vehicle:
                spot.remove_vehicle()
                vehicle.calculate_parking_fee(hours)
                payment_method = int(input("Select Payment Method: 1. Cash 2. Card 3. UPI\nEnter choice: "))
                if payment_method == 1:
                    payment = CashPayment()
                elif payment_method == 2:
                    payment = CardPayment()
                elif payment_method == 3:
                    payment = UPIPayment()
                else:
                    print("Invalid choice")
                    return
                amount = 0
                if isinstance(vehicle, Bike):
                    amount = 20 * hours
                elif isinstance(vehicle, Car):
                    amount = 50 * hours
                elif isinstance(vehicle, SUV):
                    amount = 70 * hours
                elif isinstance(vehicle, Truck):
                    amount = 100 * hours
                payment.pay(amount)
                return
        print(f"Vehicle {vehicle.get()} not found in any spot")

class Payment:
    def pay(self,amount):
        pass
class CashPayment(Payment):
    def pay(self,amount):
        print(f"Paid ₹{amount} in cash")
class CardPayment(Payment):
    def pay(self,amount):
        print(f"Paid ₹{amount} using credit/debitcard")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Paid ₹{amount} using UPI")
lot = ParkingLot("CityMall Parking")
# Add spots of different sizeslot.add_spot(ParkingSpot(1, "S"))
lot.add_spot(ParkingSpot(2, "M"))
lot.add_spot(ParkingSpot(3, "M"))
lot.add_spot(ParkingSpot(4, "L"))
lot.add_spot(ParkingSpot(5, "XL"))

bike1 = Bike("B101", "TS01AB1234", "Rahul", True)
car1 = Car("C201", "TS05CD5678", "Priya", 5)
suv1 = SUV("S301", "TS09EF9012", "Anjali", True)
truck1 = Truck("T401", "TS11XY4455", "Ravi", 12)

lot.park_vehicle(bike1)
lot.park_vehicle(car1)    
lot.park_vehicle(suv1)    
lot.park_vehicle(truck1) 
lot.show_spots()

lot.unpark_vehicle(car1, hours=3)   

lot.show_spots()