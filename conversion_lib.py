class conversion:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def temperature(self):
        a = self.a
        b = self.b 
        try:
            degree=round((9*self.a)/5+32,1)
            degree1=round((9*self.b)/5+32,1)
            print(f"Your given temperature {a}degree in Fahrenheit is:{degree}°F")
            print(f"Your given temperature {b}degree in Fahrenheit is:{degree1}°F")
            celcius1 =round((self.a-32)*5/9,1)
            celcius =round((self.b-32)*5/9,1)
            print(f"Your given temperature {a}F in Degree Celcius is:{celcius1}°C")
            print(f"Your given temperature {b}F in Degree Celcius is:{celcius}°C")
        except Exception as e:
            print(e)

    def weights(self):
        a = self.a 
        b = self.b 
        try:
            weight = self.a*2.205
            weight1 = self.b*2.205
            print(f"Your given weight {a}kg converted to :{round(weight,2)} Lbs")
            print(f"Your given weight {b}kg converted to :{round(weight1,2)} Lbs")      
            weight2 = self.a/2.205
            weight3 = self.b/2.205
            print(f"Your given weight {a}Lbs converted to :{round(weight2,2)}Kgs")
            print(f"Your given weight {b}Lbs converted to :{round(weight3,2)}Kgs")
        except Exception as e:
            print(e)

    def liquids(self):
        a=self.a 
        b=self.b 
        try:
            quantity = self.a*1000
            quantity1 = self.b*1000
            print(f"Your given quantity {a}ltr converted to :{quantity} ml")
            print(f"Your given quantity {b}ltr converted to :{quantity1} ml")
            quantity2 = self.a/1000
            quantity3 = self.b/1000
            print(f"Your given quantity {a}ml converted to :{quantity2} ltr")
            print(f"Your given quantity {b}ml converted to :{quantity3} ltr")
        except Exception as e:
            print(e)

    
