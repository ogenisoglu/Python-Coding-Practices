#240201049

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Ball Crush

from random import randint
import time

def display_board(board):
    stri=""
    for i in board:
        for j in i:
            stri+=str(j)+" "#we are transforming board to string which is readable
        stri+="\n"
    print (stri)

def display_ball_positions(ball_positions):
    new=[]
    for i in range(len(ball_positions)):
        new.append((ball_positions[i][0]+1,ball_positions[i][1]+1))#lists starts from 0 in python; therefore, we have to increase by 1 when printing ball positions.
    print("\n"+str(new)+"\n")

def choose_ball(board):
    new=[]
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                new.append((i,j))# this function takes just board as input so i have to realize ball positions again
                
    while True:
        entry=str(input("Which ball?  ")).split(",")
        try:
            ball_pos=(int(entry[0])-1,int(entry[1])-1)# python lists start from 0, i have to decrease input by 1
            if ball_pos in new:# i use try-except here, because if input doesn't include a digit, it turns an error
                break
            else:
                print("It is not a ball position")
        except:
            print("It is not a ball position")
    return ball_pos

def get_valid_moves(pos,len_board):
    moves=["w","a","s","d"]
    if pos[0]==0:
        moves.remove("w")
    if pos[1]==0:
        moves.remove("a")
    if pos[0]==4:
        moves.remove("s")# it creates a list included all moves(w,a,s,d) and controls "is there any wall nearby?"
                         #if there are, eliminates them from move list in every turn of while loop in main function
    if pos[1]==4:
        moves.remove("d")
    return moves

def make_move(board,pos,valid_moves,ball_positions):
    move = str(input("\nYour move?  "))
    while not move in valid_moves:
        move=str(input("Enter a valid direction!\nYour move?  "))
    x,y=pos[0],pos[1]
    move_last=(x,y)# i have to save last location of selected ball to delete it and put new one instead of it
    if move=="s":
        x+=1
    elif move=="w":
        x-=1
    elif move=="d":
        y+=1
    elif move=="a":
        y-=1
    move=(x,y)
    if check_collision(board,move):
        delete_ball(board,move_last,ball_positions)#collision! so we have to delete and never add it or others back
    else:
        delete_ball(board,move_last,ball_positions)#it deletes last ball from list and ball_positions
        ball_positions.append(move)# there no collision here so we have to add new move to ball_positions

    board[x][y]=1 #adding new ball location to map

def delete_ball(board, pos, ball_positions):
    board[pos[0]][pos[1]]=0#this function deletes ball from ball_positions and map
    ball_positions.remove(pos)
def check_collision(board,pos):
    new=[]
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                new.append((i,j))#i did this process to tell ball locations in map to program
    if pos in new:
        return True#"is there any ball location same with new move?" 
    else:
        return False
    
def main():
    len_board = 5
    board = [[0 for col in range(len_board)] for row in range(len_board)]

    while True:
        ball_positions = [(randint(0, len_board-1), randint(0, len_board-1)) for i in range(3)]
        if len(ball_positions) == len(set(ball_positions)):
            break
    
    for pos in ball_positions:
        board[pos[0]][pos[1]] = 1

    start_time = time.time()
    
    while True:
        display_ball_positions(ball_positions)
        display_board(board)
        
        if len(ball_positions) == 1:
            break
        
        ball_pos = choose_ball(board)
        
        valid_moves = get_valid_moves(ball_pos, len(board))
        print("Valid moves:", valid_moves)
        
        make_move(board, ball_pos, valid_moves, ball_positions)
        
    end_time = time.time()

    minutes, seconds = divmod(end_time-start_time, 60)
    hours, minutes = divmod(minutes, 60)
    print("Game Over!")
    print("Passed time= {:02d}:{:02d}:{:02d}".format(int(hours), int(minutes),int(seconds)))
    x = str(input())
main()
