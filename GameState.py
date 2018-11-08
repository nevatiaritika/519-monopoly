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
		self.net_wealth = 0

	def _calculateNetWealth():
