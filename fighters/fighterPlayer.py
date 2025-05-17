from fighter import Fighter

class FighterPlayer (Fighter):
    def __init__(self,player, x, y, flip, data, sprite_sheet, animation_steps,name):
        super.__init__(player, x, y, flip, data, sprite_sheet, animation_steps)
        self.name = name

    def getName(self):
        return self.name