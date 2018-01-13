

class Palyer(object):
      def __init__(self,bodyId,armeture):
          self.health = 100; # health of the palyer
          self.assets = list()# assets is a JSON structure of all the assets those can be hold by player by default or in game
          self.Script = list()# strore is a JSON structure of the scripts as {'script name': 'enabled'}
          ''' scripts will be stored in the scripts directory or on the web directory from where they will be fetch and download to main player 
          ther are scripts of walking ,running ,firing pickup,drop and the rest all the movments of the player'''
          
          self.AI = False
          ''' this gives the feature to the layer that it can be used as both the main player or the enemy or the pertner of the main player 
          in the game '''
          
          self.armeture = armeture# bones armeture of the player
          ''' this armeture contains all the set of bones and joints of the player's body and which join can have the maximum rotation angle 
          along its cordinates axis also have auto react control e.i. when oneis rotated or move then how it affect the motion and rotation of the 
          other its connected axis '''
            
          self.body = bodyId # this body is the 3d structure of the player and here the id of that 3d object is given here
            
          self.forge = forge # this forge provide the complete instruction about which vertises are assigned to bone
          '''  this forge actully controlls the motion of the vertex group when a bone is move or rotated and these vertex group will act 
          at the joining points of two or more vertex group'''
          
          
          
