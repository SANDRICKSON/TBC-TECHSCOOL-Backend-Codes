class Car:
    wheels = 4
    def __init__(self,manufacturer,model,year,engine):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.engine = engine




nissan = Car("Nissan","RX-7",1997,2.5)
nissan9 = Car("Nissan","RX-7",1997,2.5)

print(nissan.__dict__)
print(nissan==nissan9)


