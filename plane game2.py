import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# =============================
# 基本設定
# =============================
GRID_SIZE = 10
CELL_SIZE = 40
PREVIEW_CELL_SIZE = 20

COLOR_DEFAULT = "#DDDDDD"
COLOR_MISS = "white"
COLOR_BODY = "#5555FF"
COLOR_HEAD = "#FF4444"
COLOR_TEXT = "black"

class PlaneGame:
    def __init__(self, root):
        self.root = root
        self.root.title("尋找機頭 - 隨機變體版")
        
        self.grid_data = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.buttons = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.planes = []
        self.total_heads = 0
        self.found_heads = 0
        self.steps = 0
        self.max_steps = None
        self.game_over = False

        self.bomb_available = 1
        self.steps_per_bomb = 5
