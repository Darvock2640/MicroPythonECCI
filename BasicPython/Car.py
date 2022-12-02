class Car():
    def __init__(self, brand = "Toyota", color = "", motor_CC = 0, model = 0, kind = "", cost = 0.0):
        self.color = color
        self.motorCC = motor_CC
        self.model = model
        self.kind = kind
        self.brand = brand
        self.cost = cost
    def Print(self):
        temp = '''
Kind: {}
Brand: {}
Model: {}
Color: {}
Motor: {} cc
Cost: ${}
        '''.format(self.kind, self.brand, self.model, self.color, self.motorCC, self.cost)
        print(temp)

    def __str__(self) -> str:
        return '''
Kind: {}
Brand: {}
Model: {}
Color: {}
Motor: {} cc
Cost: ${}
            '''.format(self.kind, self.brand, self.model, self.color, self.motorCC, self.cost)
