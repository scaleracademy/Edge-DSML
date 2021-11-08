class Contestant:

    def __init__(self, switch=False):
        self.switch = switch
        self.selection = None

    def select_cup(self, cup_count):
        self.selection = int(random.uniform(0, cup_count))
        return self.selection

    def wanna_switch(self, new_cup):
        if self.switch:
            return new_cup
        else:
            return self.selection
        
        
class Host:

    def __init__(self, cup_count=3):
        assert cup_count >= 3
        self._prize_index = int(random.uniform(0, cup_count))
        self.cup_count = cup_count

    def present_cups(self):
        return self.cup_count

    def eliminate_others_and_present_one_cup(self, contestant_selection):
        if contestant_selection == self._prize_index:
            while True:
                alternative_cup = int(random.uniform(0, self.cup_count))
                if alternative_cup != contestant_selection:
                    return alternative_cup
        else:
            return self._prize_index

    def reveal_if_winner(self, final_selection):
        if final_selection == self._prize_index:
            return True
        else:
            return False