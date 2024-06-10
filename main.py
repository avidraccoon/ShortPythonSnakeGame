import random, tkinter as tk;key_bindings = {"<KeyPress-Right>": lambda _: cvs.change_heading(0),"<KeyPress-Up>": lambda _: cvs.change_heading(1),"<KeyPress-Left>": lambda _: cvs.change_heading(2),"<KeyPress-Down>": lambda _: cvs.change_heading(3),}
class Box:
    def __init__(self, canvas, value, x, y, size): self.canvas, self.box, self.value = canvas, canvas.create_rectangle(x*(size+3), y*(size+3), x*(size+3)+size, y*(size+3)+size, fill="black"), value
    def setValue(self, val): self.value = val;self.canvas.itemconfig(self.box, fill="red") if val == -1 else self.canvas.itemconfig(self.box, fill="green")
    def decValue(self):
        if self.value>0:self.value-=1;self.canvas.itemconfig(self.box, fill="blue")
        if self.value == 0:self.canvas.itemconfig(self.box, fill="black")
    def incValue(self): self.value += 1 if self.value > 0 else 0
class MoveCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):super().__init__(*args, **kwargs);self.posDir, self.movement, self.dim, self.died, self.length, self.d, self.ld = [[0,1], [1,0]], [(1,0), (0,-1), (-1, 0), (0, 1), (0,0), (0,0)], (15, 15), False, 1, -1, -1;self.pos, self.grid = (int(self.dim[0] / 2), int(self.dim[1] / 2)), [[Box(self, 0, x+1, y+1, 15) for x in range(self.dim[0])] for y in range(self.dim[1])];self.grid[self.pos[1]][self.pos[0]].setValue(self.length);self.plantApple();self.tick()
    def tick(self):[[cell.decValue() for cell in row] for row in self.grid];self.pos = tuple(map(lambda i, j: i+j, self.pos, self.movement[self.d]));self.checks();self.ld = self.d;self.grid[self.pos[1]][self.pos[0]].setValue(self.length);self.after(250, self.tick) if not self.died else None
    def plantApple(self):
        pos = (random.randint(0, self.dim[0] - 1), random.randint(0, self.dim[1] - 1));
        while self.grid[pos[1]][pos[0]].value != 0: pos = (random.randint(0, self.dim[0] - 1), random.randint(0, self.dim[1] - 1))
        self.grid[pos[1]][pos[0]].setValue(-1)
    def checks(self):
        if not (self.pos[0] < self.dim[0] and self.pos[0] >= 0 and self.pos[1] < self.dim[1] and self.pos[1] >= 0 and self.grid[self.pos[1]][self.pos[0]].value <= 0): self.died = True; return
        if self.grid[self.pos[1]][self.pos[0]].value == -1: self.length += 1;[[cell.incValue() for cell in row] for row in self.grid];self.plantApple()
    def change_heading(self, d): self.d = d if self.posDir[self.ld%2][d%2] == 1 else self.d
if __name__ == "__main__":root = tk.Tk();root.geometry("300x300");cvs = MoveCanvas(root);cvs.pack(fill="both", expand=True);[root.bind(key, action) for key, action in key_bindings.items()];root.mainloop()