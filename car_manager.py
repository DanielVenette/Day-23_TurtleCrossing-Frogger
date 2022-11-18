from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANE_YCOORDS = [-230, -184, -138, -93, -48]


class CarManager:

    # initialize CarManager class as a roadway with len(LANE_YCOORDS) lanes with 5 cars in each lane
    def __init__(self):
        self.lane_list = []
        for lane_num in range(5):
            self.car_list = []
            for car_num in range(5):
                car = Turtle()
                car.shapesize(1, 2)
                car.color(random.choice(COLORS))
                car.setheading(180)
                car.penup()
                car.shape("square")
                car.goto(400, LANE_YCOORDS[lane_num])
                self.car_list.append(car)
            self.lane_list.append(self.car_list)

    def print_list(self):
        print(f"Lane 4 Cars Positions:")
        for car in self.lane_list[4]:
            print(car.position())

    # test if there is any car on screen in lane 0.  If not place a car on screen, in lane
    def lane_test(self):
        for lane in self.lane_list:
            lane_ready = True
            for car in lane:
                # if car has passed entire screen, move to "parking lot"
                if car.xcor() < -280:
                    car.setx(400)
                # if any car is not at least a third of the way across the screen, lane is not ready for car release
                if 100 < car.xcor() < 400:
                    lane_ready = False
            if lane_ready:
                # 1 in 20 chance of releasing random car in lane's parking lot
                if random.randint(1, 20) == 1:
                    rand_car_choice = random.randint(0, 4)
                    # lane[rand_car_choice].setx(280)
                    if int(lane[rand_car_choice].xcor()) == 400:
                        lane[rand_car_choice].setx(280)

    def move_cars(self):
        for lane in self.lane_list:
            for car in lane:
                if car.xcor() < 400:
                    car.forward(MOVE_INCREMENT)

    def detect_collision(self, player):
        for lane in self.lane_list:
            for car in lane:
                if abs(player.xcor() - car.xcor()) < 19:
                    past_car = False
                    if player.ycor() > car.ycor():
                        past_car = True
                    # if player has passed the car on the y axis...
                    if past_car:
                        if abs(player.ycor() - car.ycor()) < 20:
                            return True
                    # if player has not passed the car on the y axis
                    else:
                        if abs(player.ycor() - car.ycor()) < 27:
                            return True
        return False
