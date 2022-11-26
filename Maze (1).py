def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
        if right_is_clear():
            turn_right()
            move()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
