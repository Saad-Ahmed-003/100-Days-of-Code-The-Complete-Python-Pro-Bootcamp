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
# Paste the above code in this link:- https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
