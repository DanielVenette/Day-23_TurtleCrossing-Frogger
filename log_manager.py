from turtle import Turtle
import random

MOVE_INCREMENT = 10
LANE_YCOORDS = [50, 96, 142, 188, 234]


class LogManager:

    # initialize LogManager class as a river with len(LANE_YCOORDS) lanes with 5 logs in each lane
    def __init__(self):
        self.logs_frozen = False
        self.lane_list = []
        self.move_player = 0
        for lane_num in range(5):
            self.log_list = []
            for log_num in range(5):
                log = Turtle()
                log.shapesize(1.5, 7)
                log.color("brown")
                log.setheading(180)
                log.penup()
                log.shape("square")
                # set initial position for even laned logs
                if lane_num % 2 == 0:
                    log.goto(400, LANE_YCOORDS[lane_num])
                    log.setheading(180)
                # set initial position for odd-laned logs
                else:
                    log.goto(-400, LANE_YCOORDS[lane_num])
                    log.setheading(0)
                self.log_list.append(log)
            self.lane_list.append(self.log_list)

    def print_list(self):
        print(f"Lane 3 Log Positions:")
        for log in self.lane_list[3]:
            print(log.position())

    # test if there is any log on screen in lane 0.  If not place a log on screen, in lane
    def lane_test(self):
        lane_number = 0
        for lane in self.lane_list:
            lane_ready = True
            for log in lane:
                # for even numbered lanes
                if lane_number % 2 == 0:
                    # if log has passed entire screen, move to "parking lot"
                    if log.xcor() < -350:
                        log.setx(400)
                    # if any log is not at least a third of the way across the screen, lane is not ready for log release
                    if 100 < log.xcor() < 400:
                        lane_ready = False
                # for odd numbered lanes
                else:
                    # if log has passed entire screen, move to "parking lot"
                    if log.xcor() > 350:
                        log.setx(-400)
                    # if any log is not at least a third of the way across the screen, lane is not ready for log release
                    if -100 > log.xcor() > -400:
                        lane_ready = False
            if lane_ready:
                # 1 in 20 chance of releasing random log in lane's parking lot
                if random.randint(1, 20) == 1:
                    rand_log_choice = random.randint(0, 4)
                    # lane[rand_log_choice].setx(280)
                    # release even-laned log
                    if lane_number % 2 == 0:
                        if int(lane[rand_log_choice].xcor()) == 400:
                            lane[rand_log_choice].setx(350)
                    # release odd-laned log
                    else:
                        if int(lane[rand_log_choice].xcor()) == -400:
                            lane[rand_log_choice].setx(-350)
            lane_number += 1

    def move_logs(self):
        for lane in self.lane_list:
            for log in lane:
                if -400 < log.xcor() < 400:
                    log.forward(MOVE_INCREMENT)

    def on_log(self, player):
        lane_number = 0
        for lane in self.lane_list:
            for log in lane:
                if abs(player.xcor() - log.xcor()) <= 70 and abs(player.ycor() - log.ycor()) <= 1:
                    # print(f"Log y: {log.ycor()}, Player y: {player.ycor()}")
                    # print(f"Log x: {log.xcor()}, Player x: {player.xcor()}")
                    if lane_number % 2 == 0:
                        self.move_player = -MOVE_INCREMENT
                    else:
                        self.move_player = MOVE_INCREMENT
                    return True
            lane_number += 1
        return False

    def freeze_logs(self):
        self.logs_frozen = True

    def unfreeze_logs(self):
        self.logs_frozen = False
