

class game(object):

    def __init__(self):
    
      self.mainLoop = True
      self.player = Player()
      self.level = Level()
      self.enemy = list()
      
    def isMainLoopUp(self):
        return self.mainLoop
    def setMainLoop(self,changeTo)
        self.mainLoop = changeTo
    def putPalyer(self):
        self.palyer.display()
    def putLevel(self):
        self.level.display()
    def 
