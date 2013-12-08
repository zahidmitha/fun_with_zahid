class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True: 
            print "\n---------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
                #or raw_input(">> "))

class Death(Scene):

    def enter(self):
        print "You're dead"
        print "Too bad dude-do you want to restart?"

        action = raw_input(">")
        if raw_input == "Yes":
            return CentralCorridor
        else:
            print "Too bad. You used to be a contender..."
            exit(0)

class EscapePod(Scene):

    def enter(self):
        print "You squeeze into the pod and blast off to the nearest planet in the hope of escape."
        print "You then realise that the pod is full of Gothons, and are gang-raped mercilessly while the air seeps out of your space suit"
        return "death"


class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons have invaded your ship."
        print "They look like Hello Kitty dolls"
        print "but don\'t let that fool you, they're scary as fuck,"
        print "and those claws are pretty sharp."
        print "What do you do"
        print "a) Run!!!"
        print "b) Make for the armoury"
        print "c) Stand and take them on hand-to-hand"
        
        hello = raw_input(">")

        if hello == "a":
            print "You coward. You run down the hall to the escape pod"
            escape_pod = EscapePod()
            escape_pod.enter()
            return "escape_pod"

        elif hello == "b":
            print "You run past all the children you have on board, leaving them at the mercy of the Gothons"
            print "Not exactly an honourable man, are you?"
            print "But, you make it to the armoury"
            return "laser_weapon_armoury"
        else:
            print "You're a REAL man/woman."
            print "Too bad they rip you to shreds"
            print "You hobble on your one remaining leg to the bridge, in the hope of diverting the ship away from its course for Earth...if the Gothons make it there, humanity (and dogs) are doomed!"
            return "bridge"




class LaserWeaponArmory(Scene):

    def enter(self):
        print "You big up the BFG (Big Friendly Gun)."
        print "Dis gon be gud."
        print "Suddenly, one of the small children from the corridor walks in. What do you do?"

        print "a) Pat him on the back and tell him not to worry"
        print "b)Shoot him in the face"
        print "c) Groom him for later...use"

        response = raw_input(">")

        if response == "a":
            print "He transforms into a Gothon. Shit."
            return "death"
        elif response == "b":
            print "He rips you a new one first"
            return "death"
        else:
            print "You tag him along to the escape pod for some private time"
            return "escape_pod"

class TheBridge(Scene):

    def enter(self):
        print "You enter the bridge"
        print "What do you do?"
        print "a) Set thrusters to full!"
        print "b)Call the ship and order an evacuation"
        print "c) Negotiate with the Gothons"

        reply = raw_input(">")

        if reply == "a":
            print "No use..."
            return "death"
        elif reply == "b":
            print "You run to the escape pod!"
            return "escape_pod"
        else:
            print "The Gothons are a civil people...the accept your surrender and merely kill yor family"
            exit(0)




class Map(object):

    scenes = {
        "central_corridor" : CentralCorridor(),
        "laser_weapon_armoury" : LaserWeaponArmory(),
        "the_bridge" : TheBridge(),
        "escape_pod" : EscapePod(),
        "death": Death()
}


    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self. start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()