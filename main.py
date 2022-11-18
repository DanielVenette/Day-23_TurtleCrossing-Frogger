import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from log_manager import LogManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("background_resized.png")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
log_manager = LogManager()
player = Player()
car_manager = CarManager()

screen.onkeypress(fun=player.move_up, key="Up")
screen.onkeypress(fun=player.move_back, key="Down")
screen.onkeypress(fun=player.move_right, key="Right")
screen.onkeypress(fun=player.move_left, key="Left")
screen.onkeypress(fun=log_manager.freeze_logs, key='f')
screen.onkeypress(fun=log_manager.unfreeze_logs, key='u')
screen.onkeypress(fun=player.on_your_mark, key='r')


game_is_on = True
game_speed = 0.1
while game_is_on:
    time.sleep(game_speed)
    screen.update()
    # print(player.position())

    car_manager.lane_test()
    car_manager.move_cars()
    if car_manager.detect_collision(player):
        screen.update()
        game_is_on = False
        scoreboard.game_over()
        time.sleep(3)
        try_again = screen.textinput(title="Game Over", prompt="Play Again?\ny/n")
        if try_again == 'y':
            scoreboard.reset_board()
            player.on_your_mark()
            game_speed = 0.1
            game_is_on = True
            screen.listen()

    log_manager.lane_test()
    if not log_manager.logs_frozen:
        log_manager.move_logs()

    # once player is on the river...
    if player.ycor() > 20:
        # if player has reached other side of river, they win round
        if player.ycor() >= 275:
            screen.update()
            scoreboard.pass_level()
            player.on_your_mark()
            # win game after 5 rounds
            if scoreboard.level > 5:
                screen.update()
                game_is_on = False
                scoreboard.beat_game()
                time.sleep(3)
                try_again = screen.textinput(title="You win!", prompt="Play Again?\ny/n")
                if try_again == 'y':
                    scoreboard.reset_board()
                    player.on_your_mark()
                    game_speed = 0.1
                    game_is_on = True
                    screen.listen()
            else:
                game_speed *= 0.8
        # game over if not on a log
        elif not log_manager.on_log(player):
            screen.update()
            game_is_on = False
            scoreboard.game_over()
            time.sleep(3)
            try_again = screen.textinput(title="Game Over", prompt="Play Again?\ny/n")
            if try_again == 'y':
                scoreboard.reset_board()
                player.on_your_mark()
                game_speed = 0.1
                game_is_on = True
                screen.listen()
        # if player is on a log, move player with that log
        else:
            player.setx(player.xcor() + log_manager.move_player)

    # if player leaves the game board, game over
    if abs(player.xcor()) > 300:
        screen.update()
        game_is_on = False
        scoreboard.game_over()
        time.sleep(3)
        try_again = screen.textinput(title="Game Over", prompt="Play Again?\ny/n")
        if try_again == 'y':
            scoreboard.reset_board()
            player.on_your_mark()
            game_speed = 0.1
            game_is_on = True
            screen.listen()



screen.exitonclick()
