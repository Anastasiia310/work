from random import randrange

board = "--------------------"
game = True
print("Wanna play TTT?")
print('You are X and i am O')
player_mark = 'x'
pc_mark = 'o'
# there is no choosing mark cause when i add such function it doesnt work and pc always play by 'o'
#player_mark = input('What mark you wanna be? X or O?' )
# if player_mark == 'X' or 'x':
#    pc_mark = 'o'
#elif player_mark == 'O' or 'o':
#    pc_mark = 'x'
#print(pc_mark, player_mark)

def evaluate(board):
    a=board.find('xxx')
    b=board.find('ooo')
    if a>=0:
        print('You are winner!')
    elif b>=0:
        print('Ha! You lose, i`m a winner!')        
    else:
        board_find=''
        for i in range(20):
            if board[i]=='x' or board[i]=='o':
                board_find=board[i]+board_find
        if len(board_find)==20:
            print('DRAW!')            
        else:
            return board


def move(board, mark, position):
    if position==0:
        board_move=mark+board[1:]
    if position==19:
        board_move=board[:-1]+mark
    if position>0 and position<19:
        board_move=board[:position]+mark+board[position+1:]
    return board_move

def player_move(board):
    while True:
        pos_player=int(input('Where it will be? 0-19  '))
        if pos_player>=0 and pos_player<=19:
            if board[pos_player]=='-':
                 board_player=move(board, player_mark, pos_player)
                 break
        else:
             print('What? i don`t understan.') 
    return board_player     

def pc_move(board):
    while True:
        pos_pc=randrange(0,19)
        if board[pos_pc]=='-':
                 board_pc=move(board, pc_mark, pos_pc)
                 break
    return  board_pc

def ttt(board):
    board_start=board
    while True:
        player_input=player_move(board_start)
        c=player_input.find('xxx')
        if c>=0:
            evaluate_input=(evaluate(player_input))
            print(evaluate_input)
            break
        pc_input=pc_move(player_input)   
        evaluate_input=(evaluate(pc_input))
        d=pc_input.find('ooo')
        if d>=0:
            print(pc_input)
            break  
        board_start=evaluate_input
        print(board_start)
     
board_input='--------------------'
ttt(board_input)