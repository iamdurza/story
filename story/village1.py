'''The Village


    You walk down the road to the village, and are greeted by a guard at the entrance. He ask's you 'Who are you and why have you come to
    our village?' You answer him that you are just passing through, but seek shelter, hot food and probz some mead. 
'''


prompt = 'f=forward, b=back'
forward = 'install'
on_west = "house-west"


def parse(s):
    line = s.action_line
    if "what" in line:
        print("You heard me.")
    elif "ouest" in line:
        s.action = "west"

