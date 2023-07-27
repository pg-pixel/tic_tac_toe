
class Player:
    def __init__(self, symbol):
        self.symbol = symbol 
        self.row_score = [0, 0, 0]
        self.column_score = [0, 0, 0]
        self.diagonal_score = 0 
        self.rev_diagonal_score = 0 
        
    def update_score(self, row, column):
        ''' 
        Aim: Update the score of the player 
        Return: None 
        ''' 
        self.row_score[row]+=1 
        self.column_score[column]+=1 
        if row==column:
            self.diagonal_score+=1 
            
        if column == 2 - row :
            self.rev_diagonal_score+=1  
            
        return 
            
    def check_win(self, row, column):
        ''' 
        Aim: Checks if player is a winner or not in O(1) TC 
        return: Boolen (True : Winner, False: Not a winnr)
        ''' 
        if self.row_score[row]==3 or self.column_score[column]==3 or self.diagonal_score==3 or self.rev_diagonal_score==3:
            return True 
        return False 
    
    def win(self):
        ''' 
        Aim: return winning msg
        '''
        return f'Player with symbol: {self.symbol} won...'
    
    def undo_move(self, row, column):
        ''' 
        Aim: On undo move, reduces score counted 
        Return : None
        ''' 
        self.row_score[row]-=1 
        self.column_score[column]-=1 
        if row==column:
            self.diagonal_score-=1 
            
        if column == 2 - row :
            self.rev_diagonal_score-=1
            
        return 
        
            
    