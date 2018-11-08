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
		self.p1_net_wealth = 0
		self.p2_net_wealth = 0
		self.monopolies = [0,0,0,0,0,0,0,0,0,0]#-0-7] Colors, [8] railroads, [9] utilities

	def calculateNetWealth(self):
		#(Property Price, house price)
		properties = [
		(60,50),#"Mediterranean Avenue"
		(60,50),#"Baltic Avenue"
		(100,50),#"Oriental Avenue"
		(200,0),# "Reading Railroad"
		(100,50),#"Vermont Avenue"
		(120,50),#"Connecticut Avenue"
		(140,100),#"St. Charles Place"
		(150,0),#"Electric Company"
		(140,100),#"States Avenue"
		(160,100),#"Virginia Avenue"
		(200,0),#"Pennsylvania Railroad"
		(180,100),#"St. James Place"
		(180,100),#"Tennessee Avenue"
		(200,100),#"New York Avenue"
		(220,150),#"Kentucky Avenue"
		(220,150),#"Indiana Avenue"
		(240,150),#"Illinois Avenue"
		(200,0),#"B. & O. Railroad"
		(260,150),#"Atlantic Avenue"
		(260,150),#"Ventnor Avenue"
		(150,0),#"Water Works"
		(280,150),#"Marvin Gardens"
		(300,200),#"Pacific Avenue"
		(300,200),#"North Carolina Avenue"
		(320,200),#"Pennsylvania Avenue"
		(200,0),#"Short Line Railroad"
		(350,200),#"Park Place"
		(400,200),#"Boardwalk"
		(0,0),#Get Out of Jail Free 1
		(0,0)#Get Out of Jail Free 2
		]
		self.p1_net_wealth = 0
		self.p2_net_wealth = 0
		for i in range(len(self.status)):
			if i!= 29 or i!=28:
				if self.status[i] > 0:#player
					if self.status[i] == 7:
						self.p1_net_wealth += (properties[i][0]/2)
					elif self.status[i] > 0:
						self.p1_net_wealth += properties[i][0] + ((self.status[i]-1)*properties[i][1])
					print("P1",self.p1_net_wealth,"P2",self.p2_net_wealth)

				if self.status[i] < 0:#player 2
					if self.status[i] == -7:
						self.p2_net_wealth += (properties[i][0]/2)
					elif self.status[i] < 0:
						x = ((self.status[i]+1)*properties[i][1]*-1)
						self.p2_net_wealth += properties[i][0] + x
					print("P1",self.p1_net_wealth,"P2",self.p2_net_wealth)

	# def phaseInfo
if __name__ == '__main__':
	gs = GameState()
	gs.status[0] = -1
	gs.status[1] = 2
	gs.status[2] = 7
	gs.status[27] = -7
	gs.calculateNetWealth()
	print(gs.p1_net_wealth)
	print(gs.p2_net_wealth)