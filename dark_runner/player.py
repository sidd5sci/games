

class Palyer(object):
      def __init__(self):
          self.health = 100; # health of the palyer
          self.assets = list()# assets is a JSON structure of all the assets those can be hold by player by default or in game
          self.Script = list()# strore is a JSON structure of the scripts as {'script name': 'enabled'}
          ''' scripts will be stored in the scripts directory or on the web directory from where they will be fetch and download to main player 
          ther are scripts of walking ,running ,firing pickup,drop and the rest all the movments of the player'''
          self.AI = Fales 
          ''' this gives the feature to the layer that it can be used as both the main player or the enemy or the pertner of the main player 
          in the game '''
          
          
          
