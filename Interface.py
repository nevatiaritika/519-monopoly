class Agent:	
	def getBMSTDecision(self,state):
		#args: GameState Object
		#rtype: Action Object
		#Definition: 
		return None

	def auctionProperty(self,state):
		#args: GameState Object
		#rtype: Action
		#G
		return None

	def buyProperty(self,state):
		#args: GameState Object
		#rtype: Action
		return None

	def jailDecision(self,state):
		#args: GameState Object
		#rtype: Action
		return None

	def respondTrade(self,state):
		#args: GameState Object
		#rtype: Action
		return None
	def recieveState(self,state):

		return None

class GameState:
	def __init__(self):
		self.turn = 0
		self.status = [0 for i in range(30)]
		self.position = [0,0]
		self.cash = [0,0]
		self.phase = None#Phase when the game begins, this will be changed later
		self.phase_info = None
		self.debt = 0
		self.previous_states = []