class Car:
    def __init__(self, name, brand):
        self.n = name
        self.b = brand
    def show(self):
        print('汽车的品牌是{0}, 汽车的名称是{1}'.format(self.b, self.b))
    def run(self):
        print('汽车{}跑起来了'.format(self.n))

a = Car('m3','bmw')
a.show()
a.run()

print(id(a))


#########################################

class Car:
    number_of_people = 0
    max_people = 10
    def __init__(self, name, brand, number_of_people, max_people):
        self.n = name
        self.b = brand
        self.num = number_of_people
        self.max = max_people
    def set_people(self):
        if self.num < self.max:
            self.max = self.num
        else:
            self.num = self.max

    def increase_people(self):
        if self.num < self.max:
            self.num+=1
        else:
            self.num = self.max

    def reduce_people(self):
        
        if self.num>0:
            self.num-=1
        else:
            self.num=0

    def show(self):
        print('车上的人数为：%d' % self.num)




a = Car('m3','bmw', 10, 10)
a.set_people()
a.increase_people()
a.reduce_people()
a.show()
a.set_people()
a.increase_people()
a.reduce_people()
a.show()
a.set_people()
a.increase_people()
a.reduce_people()
a.show()
