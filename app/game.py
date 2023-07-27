
class Game:
    def __init__(self):
        self.reset_game()
        
    def reset_game(self):
        self.count= 0
        self.index = 0 
        self.occupied = ['-' for _ in range(9)]
        self.moves = []
        self.player_lst =[]
        self.dict = {
            (0,0):0,(1,0):3,(2,0):6,
            (0,1):1,(1,1):4,(2,1):7,
            (0,2):2,(1,2):5,(2,2):8
        }
  
    def undo(self):
        ''' 
        Aim: Undo the previous move 
        return: None
        '''
        self.index^=1
        self.count -= 1
        row, column = self.moves.pop() 
        player = self.player_lst[self.index]
        player.undo_move(row, column) 
        pos = self.dict[(row, column)]
        self.occupied[pos]='-' 
        
        return 
    
    def move(self):
        '''
        aim: This Function will take user's input and will mark movements 
        return : game msg , flag (True: Game Completed, False: Game in-progress)
        '''
        player = self.player_lst[self.index] 
        print(f"Player with symbol: {player.symbol}'s chance:")
        _move_flag=True
        if self.count == 9:
            return 'Game Draw',True
        while _move_flag:
            row = int(input('Enter the row where you want to move(0/1/2): '))
            column = int(input('Enter the column where you want to move(0/1/2): '))
            
            if row>=0 and row<3 and column>=0 and column<3:
                if self.occupied[self.dict.get((row, column))]=='-':
                    
                    self.count+=1 
                     
                    self.occupied[self.dict.get((row, column))] = player.symbol
                    
                    _move_flag = False
                    self.moves.append((row, column))
                    self.index^=1 
                    
                    player.update_score(row, column)
                    if player.check_win(row, column):
                        return (player.win()), True
                    
                else:
                    print('Block already occupied') 
            else:
                print('invalid move')
                
        return 'Nice Move', False
                
        
        
        