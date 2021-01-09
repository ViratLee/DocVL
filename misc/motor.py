class Motor:
    def __init__(self, *args):
    	if args:
            self.type = args[0]
            self.color = args[1]
    def __str__(self):
    	return f" this car is {self.color} {self.type}"
if __name__ == '__main__':
	motor = Motor('Toyota','orange')
	print(motor)#this car is orange Toyota