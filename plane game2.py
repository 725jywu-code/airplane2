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

                self.top_frame = tk.Frame(root, pady=10)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.lbl_steps = tk.Label(self.top_frame, text="步數: 0", font=("Arial", 12))
        self.lbl_steps.pack(side=tk.LEFT, padx=20)
        
        self.lbl_heads = tk.Label(self.top_frame, text="剩餘機頭: 0",
                                  font=("Arial", 12, "bold"), fg="red")
        self.lbl_heads.pack(side=tk.LEFT, padx=20)
        
        self.btn_restart = tk.Button(self.top_frame, text="重新開始", command=self.ask_start_game)
        self.btn_restart.pack(side=tk.RIGHT, padx=20)

        self.btn_bomb = tk.Button(self.top_frame, text="使用炸彈 (1)", command=self.use_bomb)
        self.btn_bomb.pack(side=tk.RIGHT, padx=20)

