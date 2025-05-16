from fighters.fighter import Fighter

class FighterPlayer (Fighter):

    def __init__(self,player, x, y, flip, data, sprite_sheet, animation_steps):
        super.__init__(player, x, y, flip, data, sprite_sheet, animation_steps)