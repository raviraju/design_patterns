from .abs_auto import AbsAuto

class MarutiCar(AbsAuto):

	def start(self):
		print('%s running with good mileage!' % self.name)

	def stop(self):
		print('%s shutting down.' % self.name)