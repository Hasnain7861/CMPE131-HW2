class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def heyThere(a):
        print(f" hey ")


blueCar = Car("blue", 23)
# print(f" the car {blueCar.color}")
blueCar.heyThere()

def test(aNumber):
    aNumber = 10
    print(aNumber)

y = 5
test(y)
print(y)

def test2(aList):
    aList.append(1)
    print(aList)

y2 = [5]
test2(y2)
print(y2)

someStr = "hepllo"
someStr2 = "hello"

print(someStr.equals(someStr2))