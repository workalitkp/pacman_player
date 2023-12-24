import random
from minimax import Minimax
import time
import random
import curses
from Environment import Env
from Agent import Agent
from State import State

stdscr = curses.initscr()
def draw_board(stdscr, board):
    stdscr.clear()

    for row, line in enumerate(board):
        stdscr.addstr(row, 0, line)
    stdscr.addstr(11, 0, f"pacman : {pacman.pos}")
    stdscr.addstr(12, 0, f"ghost_1 : {ghost1.pos}")
    stdscr.addstr(13, 0, f"ghost_2 : {ghost2.pos}")
    stdscr.addstr(14, 0, f"util : {state.util}")
    stdscr.refresh()

def list2board(board):
    new_board = [[0 for i in range(18)] for j in range(9)]
    for i in range(9):
        for j in range(18):
            if board[i][j] == 0:
                new_board[i][j] = "."
            elif board[i][j] == 1:
                new_board[i][j] = "#"
            elif board[i][j] == 2:
                new_board[i][j] = "P"
            elif board[i][j] == 3:
                new_board[i][j] = "G"
            elif board[i][j] == 4:
                new_board[i][j] = " "
            elif board[i][j] == 5:
                new_board[i][j] = "G"
    for i in range(9):
        new_board[i] = " ".join(new_board[i])
    return new_board




# create the game and insert agents
env = Env(length=18, height=9, difficulty=1)

pacman = Agent(type="pacman", pos=[4, 4])
ghost1 = Agent(type="ghost", pos=[4, 5])
ghost2 = Agent(type="ghost", pos=[4, 3])

env.insert_agent(pacman)
env.insert_agent(ghost1)
env.insert_agent(ghost2)



# creating minimax obj with given env 
mini_max = Minimax(game=env, depth=3) # game is unnec


state=State(env=env,agent=pacman,ghost1=ghost1,ghost2=ghost2)
# ,action = mini_max.get_action(state=state)

actions = ["up", "down", "left", "right"]

while not state.is_terminal():
    draw_board(stdscr=stdscr,board=list2board(env.board))
    # time.sleep(1)
    be = pacman.closest_food(env=env)
    action = mini_max.get_action(state=state)

    env.step(action=action,agent=pacman)
    ghost1_moves = ghost1.possible_moves(env)
    ghost2_moves = ghost2.possible_moves(env)
    env.step(action=random.choice(ghost1_moves),agent=ghost1)
    env.step(action=random.choice(ghost2_moves),agent=ghost2)
    state = State(env=env,agent=pacman,ghost1=ghost1,ghost2=ghost2)
draw_board(stdscr=stdscr,board=list2board(env.board))
# draw_board(stdscr=stdscr,board=["done"])
