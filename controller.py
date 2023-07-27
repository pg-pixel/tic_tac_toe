from app import game, player

class Client:
    def __call__(self):
        self.initialize_game()
           
    def initialize_game(self):
        self.GAME = game.Game() 
        
        Player1 = player.Player('X')
        Player2 = player.Player('O')  
        
        self.GAME.player_lst.append(Player1)
        self.GAME.player_lst.append(Player2) 
        
    def make_undo(self):
        self.GAME.undo()
        
    def make_move(self):
        msg, status = self.GAME.move()
        self.printer()
        Undo = input('Do you want to undo the move> Choose 1 for Undo- Choose 0 for skipping Undo: (1/0): ')
        if int(Undo):
            self.make_undo() 
        print(msg)
        return status
    
            
    def printer(self):
        
        print(f' {self.GAME.occupied[0]} |  {self.GAME.occupied[1]}  |  {self.GAME.occupied[2]}  ')
        print(f'---|-----|---')
        print(f' {self.GAME.occupied[3]} |  {self.GAME.occupied[4]}  |  {self.GAME.occupied[5]}  ')
        print(f'---|-----|---')
        print(f' {self.GAME.occupied[6]} |  {self.GAME.occupied[7]}  |  {self.GAME.occupied[8]}  ')
        
    def play_game(self):
        print("Welcome to pg's X and O game. We have 2 players x and O. Lets start the game...")
        while self.GAME.count < 9:
            status = self.make_move()
            if status:
                break 
        print('Thanks for the game.')
        ques = input('Do you want to play again? 1: Yes 0: No (1/0):')
        if int(ques) ==1:
            driver()
        else:
            exit()
            
        
def driver():
    solver = Client()
    solver()
    solver.play_game()
    
if __name__=="__main__":
    driver()
                
    
        
        