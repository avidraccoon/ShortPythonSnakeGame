import random, tkinter as tk;key_bindings = {"<KeyPress-Right>": lambda _: (lambda x: setattr(cvs, "d", (x if cvs.posDir[cvs.ld%2][x%2] == 1 else cvs.d)))(0),"<KeyPress-Up>": lambda _: (lambda x: setattr(cvs, "d", (x if cvs.posDir[cvs.ld%2][x%2] == 1 else cvs.d)))(1),"<KeyPress-Left>": lambda _: (lambda x: setattr(cvs, "d", (x if cvs.posDir[cvs.ld%2][x%2] == 1 else cvs.d)))(2),"<KeyPress-Down>": lambda _: (lambda x: setattr(cvs, "d", (x if cvs.posDir[cvs.ld%2][x%2] == 1 else cvs.d)))(3),};root = tk.Tk();root.geometry("300x300");[root.bind(key, action) for key, action in key_bindings.items()]
class Box(object):
    def __init__(self, canvas, value, x, y, size): self.canvas, self.box, self.value = canvas, canvas.create_rectangle(x*(size+3), y*(size+3), x*(size+3)+size, y*(size+3)+size, fill="black"), value
    def setValue(self, val): self.value = val;self.canvas.itemconfig(self.box, fill="red") if val == -1 else self.canvas.itemconfig(self.box, fill="green")
    def decValue(self):self.value-=1 if self.value>0 else 0;self.canvas.itemconfig(self.box, fill="blue") if self.value>0 else None;self.canvas.itemconfig(self.box, fill="black") if self.value == 0 else None
class MoveCanvas(tk.Canvas, object):
    def __init__(self, *args, **kwargs):super().__init__(*args, **kwargs);self.posDir, self.movement, self.dim, self.died, self.length, self.d, self.ld = [[0,1], [1,0]], [(1,0), (0,-1), (-1, 0), (0, 1), (0,0), (0,0)], (15, 15), False, 1, -1, -1;self.pos, self.grid = (int(self.dim[0] / 2), int(self.dim[1] / 2)), [[Box(self, 0, x+1, y+1, 15) for x in range(self.dim[0])] for y in range(self.dim[1])];self.grid[self.pos[1]][self.pos[0]].setValue(self.length);self.pos1 = None; self.solved = False;self.plantApple();self.tick()
    def tick(self):[[cell.decValue() for cell in row] for row in self.grid];self.pos = tuple(map(lambda i, j: i+j, self.pos, self.movement[self.d]));self.died = False if (self.pos[0] < self.dim[0] and self.pos[0] >= 0 and self.pos[1] < self.dim[1] and self.pos[1] >= 0 and self.grid[self.pos[1]][self.pos[0]].value <= 0) else True;self.pos = (0, 0) if not (self.pos[0] < self.dim[0] and self.pos[0] >= 0 and self.pos[1] < self.dim[1] and self.pos[1] >= 0 and self.grid[self.pos[1]][self.pos[0]].value <= 0) else self.pos;self.length += 1 if self.grid[self.pos[1]][self.pos[0]].value == -1 else 0;[[setattr(cell, "value", cell.value + (1 if cell.value>0 else 0)) for cell in row] for row in self.grid] if self.grid[self.pos[1]][self.pos[0]].value == -1 else None;self.pos1 = None;self.solved = False;self.plantApple() if self.grid[self.pos[1]][self.pos[0]].value == -1 else None;self.ld = self.d;self.grid[self.pos[1]][self.pos[0]].setValue(self.length);self.after(250, self.tick) if not self.died else None
    def plantApple(self): result = [];filtered = list(map(lambda x: filter(lambda i: i.value == 0,x), self.grid));[result.extend(el) for el in filtered];choice = random.choice(result);choice.setValue(-1);
cvs = MoveCanvas(root);cvs.pack(fill="both", expand=True);root.mainloop()
