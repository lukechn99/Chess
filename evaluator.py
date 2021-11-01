from event import Event

class Evaluator:
    def __init__(self):
        self.event_map = {}
        self.initialize()

    def initialize(self, state="blank"):
        '''
        This method is called by the __init__ function. It will populate the event_map
        with each possible coordinate and an empty array to store actions at those
        coordinates. 
        '''
        for letter in range(65, 91):
            for num in range(1, 8):
                coord = chr(letter) + str(num)
                self.event_map[coord] = []
    
    def delete(self, coord, event):
        pass

    def add(self, coord, event):
        pass

    def evaluate_action(self, event):
        pass

    def evaluate(self):
        '''
        This method looks at what is possible on each square independent 
        of the board and then adds the score onto value
        '''
        value = 0
        for coord in self.event_map.keys():
            for event in self.event_map[coord]:
                value += event.get_value()
        return value
