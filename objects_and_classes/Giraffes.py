class Animals:
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('Eating food')
    def left_foot_forward(self):
        print('left foot forward')
    def left_foot_backward(self):
        print('left foot backward')
    def right_foot_forward(self):
        print('right foot forward')
    def right_foot_backward(self):
        print('right foot backward')
class mammals(animals):
    def milking_young(self):
        print('milking young')
class giraffes(mammals):
    def __init__(self, spots):
        self.giraffe_spots = spots
    def eat_leaves_from_trees(self):
        self.eat_food()
    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat_food()
    def dance_a_jig(self):
        self.left_foot_forward()
        self.left_foot_backward()
        self.right_foot_forward()
        self.right_foot_backward()
        self.left_foot_backward()
somadasa = giraffes(100)
print(somadasa.giraffe_spots)
sumanasiri = giraffes(150)
print(sumanasiri.giraffe_spots)
somadasa.find_food()
sumanasiri.dance_a_jig()

