from rules import VALUES as v

class Event:
    def __init__(self, actor, action):
        '''
        actor is either White or Black
        action is kind of like chess notation, but more information rich, 
        it is in the form of [actor_piece, move/take/promote, reactor_piece]
        '''
        self.actor = actor
        self.action = action

    def get_value(self):
        '''
        Returns the value of the event, for example 1 if a black pawn is 
        captured and -1 if a black pawn is captured
        '''
        return int(self.actor == "White") * v(self.action[2])
        

