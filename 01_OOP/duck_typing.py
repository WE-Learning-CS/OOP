class Truck:
  def drive(self):
    print("Driving Truck")

  def stop(self):
    print("Stoping Truck")


class Bus:
	def drive(self):
		print("Driving Bus")

	def stop(self):
		print("Stoping Bus")


class RaceCar:
	def drive(self):
		print("Driving RaceCar")

	def stop(self):
		print("Stoping RaceCar")


def drive_car(car):
	car.drive()


truck = Truck()
bus = Bus()
race_car = RaceCar()

drive_car(truck) # Driving Truck
drive_car(bus) # Driving Bus
drive_car(race_car) # Driving RaceCar