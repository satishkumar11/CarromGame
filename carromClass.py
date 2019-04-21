from collections import defaultdict

class Board():
	def __init__(self):
		self.blackCoins = 9
		self.redCoins = 1

	def updateCoins(self, black, red):
		self.blackCoins = self.blackCoins + black
		self.redCoins = self.redCoins + red

	def checkRedCoinsAvailable(self, move):
		if(move == 3):
			if(self.redCoins == 0):
				return False
		return True

	def checkBlackCoinsAvailable(self, move):
		if(self.blackCoins > 0):
			return True
		return False

#------------------------------------------------#

class Player():
	def __init__(self):
		self.player1Score = 0
		self.player2Score = 0
		self.player1Move = []
		self.player2Move = []
	
	def checkPreviousPlay(self, turn):
		if(not turn):
			l = len(self.player1Move)
			if(l>=2):
				if(self.player1Move[l-1]<=0 and self.player1Move[l-2]<=0 and self.player1Move[l-3]<=0):
					return -1
				return 0
			return 0

		else:
			l = len(self.player2Move)
			if(l>=2):
				if(self.player2Move[l-1]<=0 and self.player2Move[l-2]<=0 and self.player2Move[l-3]<=0):
					return -1
				return 0
			return 0

	def updateScore(self, turn, score):
		if(not turn):
			self.player1Score+=score
			self.player1Move.append(score)
		else:
			self.player2Score+=score
			self.player2Move.append(score)

	def announceWinner(self):
		if(max(self.player1Score, self.player2Score)>=5):
			print("Final Score")
			print("Player1 =",self.player1Score,"Player2 =",self.player2Score)
			if(abs(self.player1Score - self.player2Score)>=3):
				if(self.player1Score>self.player2Score):
					print("Player1 is Winner")
				else:
					print("Player2 is winner")
			else:
				print("Draw")
		else:
			print("Final Score")
			print("Player1 =",self.player1Score,"Player2 =",self.player2Score)
			print("Draw")

#------------------------------------------------------------------------#

class CarromGame(Board, Player):

	def __init__(self):
		Board.__init__(self)
		Player.__init__(self)

	def rule(self):
		print("GAME RULE")
		print("1. Strike = 1 Point\n2. Multistrike = 2 Point \n3. Red strike = 3 Point\n4. Striker strike = -1 Point\n5. Defunct coin = -2 Point\n6. None = 0 Point\n")

	def calculateScore(self, move):
		if(move == 1):
			self.updateCoins(-1,0)
			return 1
		if(move == 2):
			if(self.blackCoins+self.redCoins>=2):
				return 2
			elif(self.blackCoins+self.redCoins==1):
				if(self.blackCoins == 1):
					self.updateCoins(-1,0)
				else:
					self.updateCoins(0,-1)
				return 1
		if(move == 3):
			self.updateCoins(0,-1)
			return 3
		if(move == 4):
			return -1
		if(move == 5):
			if(self.blackCoins > 0):
				self.blackCoins-=1
			else:
				self.redCoins -=1
			return -2
		if(move == 6):
			return 0

	def checkMove(self, move):
		if(move.isdigit()):
			move = int(move)
			if(move>6 or move<=0):
				return False
			return True
		else:
			return False

	def display(self):
		print("Black Coins = ",self.blackCoins,"|| Red Coins = ",self.redCoins)
		print("Player1Score = ",self.player1Score,"|| Player2Score = ",self.player2Score)
		print("Player1LastMoves",self.player1Move,"|| Player2LastMoves",self.player2Move)
		print("\n")


	def startGame(self, turn, player):
		self.rule()
		while(self.blackCoins>0 or self.redCoins>0):
			if(not turn):
				print("Player1 = ",end=" ")
				move = input()
				if(self.checkMove(move)):
					move = int(move)
					if(not self.checkRedCoinsAvailable(move)):
						print("Red is not available, please try different move")
						continue

					if(move==1 or move==2):
						if(not self.checkBlackCoinsAvailable(move)):
							print("Black Coins are exhausted, please try different move")
							continue

					score = self.calculateScore(move)
					self.updateScore(turn, score)
					if(score <=0):
						self.player1Score+=self.checkPreviousPlay(turn)
				else:
					print("Invalid Move")
					continue

			else:
				print("Player2 = ",end=" ")
				move = input()
				if(self.checkMove(move)):
					move = int(move)
					if(not self.checkRedCoinsAvailable(move)):
						print("Red is not available, please try different move")
						continue

					if(move == 1 or move == 2):
						if(not self.checkBlackCoinsAvailable(move)):
							print("Black Coins are exhausted, please try different move")
							continue
					
					score = self.calculateScore(move)
					self.updateScore(turn, score)
					if(score <=0):
						self.player2Score+=self.checkPreviousPlay(turn)
				else:
					print("Invalid Move")
					continue
			self.display()
			turn=1-turn

		self.announceWinner()

#----------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
	ob0 = CarromGame()
	ob0.startGame(0,0)