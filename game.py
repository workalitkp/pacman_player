import random
from minimax import Minimax
import time
import random
import curses
from Environment import Env
from Agent import Agent
from State import State

env = Env(length=18, height=9, difficulty=1)

pacman = Agent(type="pacman", pos=[0, 0])
ghost1 = Agent(type="ghost", pos=[0, 1])
ghost2 = Agent(type="ghost", pos=[0, 16])


env.insert_agent(pacman)
env.insert_agent(ghost1)
env.insert_agent(ghost2)


# env.step(pacman,"up")
# env.step(pacman,"right")
# env.step(pacman,"down")
mini_max = Minimax(game=env, depth=5)
# env.step(minimax.get_action(state=state))
cnt = 1
actions = ["up", "down", "left", "right"]

def draw_board(stdscr, board):
    stdscr.clear()

    for row, line in enumerate(board):
        stdscr.addstr(row, 0, line)

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

stdscr = curses.initscr()
state=State(env=env,agent=pacman,ghost1=ghost1,ghost2=ghost2)
# ,action = mini_max.get_action(state=state)

while not state.is_terminal():
    draw_board(stdscr=stdscr,board=list2board(env.board))
    time.sleep(0.2)
    action = mini_max.get_action(state=state)
    # env.step(action=action,agent=pacman)
    env.step(action=random.choice(actions),agent=ghost1)
    env.step(action=random.choice(actions),agent=ghost2)
    state = State(env=env,agent=pacman,ghost1=ghost1,ghost2=ghost2)

draw_board(stdscr=stdscr,board=["done"])
