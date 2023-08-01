class cat:
    def eat(self):
        print(self.name+"吃饭")

    def drink(self):
        print(self.name+"喝水")


tom = cat()
tom.name = "Tom"
tom.eat()
tom.drink()
