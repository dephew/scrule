# -*- coding: UTF-8 -*-
#####################################################
#A simple screen rule with only tkinter moudle.     #
#Moving and resizing a window to measure the screen.#
#Run this script (scrule.py) directly under Python. #
#By dhy(denghy@shutcm.edu.cn) 2024.11.29            #
#####################################################
import tkinter as tk

tips = """
-------------------------
[Moving Window]
Title draging or (Shift+)arrow keys.
[Resizing Window]
Border draging or Ctrl+arrow keys.
[Transparent]
Mouse wheel scrolling or "a"/"z".
[Show/Hide Info]
Double clicking or "i"  to toggle.
[Copy Info]
Right clicking or Ctrl+c.
[Full Screen]
Pressing "f" to toggle.
[Locate Center]
Pressing "c".
[Quit]
Clicking the close icon or "q".
"""

alpha = 0.7
x,y,w,h,sw,sh = 0,0,0,0,0,0
pos_ttl,pos_txt = "",""
Info_show,Full_screen = True,False

def adjust_trans(event):
    global alpha
    if event.delta > 0:  # scroll backward
        alpha = max(alpha - 0.1, 0.3)  
    else:                # scroll forward
        alpha = min(alpha + 0.1, 0.9)      
    root.attributes('-alpha', alpha)

def move_up(event):
    _y = max(y - 1, 0)
    root.geometry(f"+{x}+{_y}")

def move_down(event):
    _y = min(y + 1, sh - h)
    root.geometry(f"+{x}+{_y}")

def move_left(event):
    _x = max(x - 1, 0)
    root.geometry(f"+{_x}+{y}")

def move_right(event):
    _x = min(x + 1, sw - w)
    root.geometry(f"+{_x}+{y}")

def move_up_fast(event):
    _y = max(y - 50, 0)
    root.geometry(f"+{x}+{_y}")

def move_down_fast(event):
    _y = min(y + 50, sh - h)
    root.geometry(f"+{x}+{_y}")

def move_left_fast(event):
    _x = max(x - 50, 0)
    root.geometry(f"+{_x}+{y}")

def move_right_fast(event):
    _x = min(x + 50, sw - w)
    root.geometry(f"+{_x}+{y}")
    
def width_zoom_in(event):
    _w = max(w - 1, 26)
    root.geometry(f"{_w}x{h}")

def width_zoom_out(event):
    _w = min(w + 1, sw - x)
    root.geometry(f"{_w}x{h}")

def height_zoom_in(event):
    _h = max(h - 1, 1)
    root.geometry(f"{w}x{_h}")

def height_zoom_out(event):
    _h = min(h + 1, sh - y)
    root.geometry(f"{w}x{_h}")

def width_zoom_in_fast(event):
    _w = max(w - 20, 26)
    root.geometry(f"{_w}x{h}")

def width_zoom_out_fast(event):
    _w = min(w + 20, sw - x)
    root.geometry(f"{_w}x{h}")

def height_zoom_in_fast(event):
    _h = max(h - 20, 1)
    root.geometry(f"{w}x{_h}")

def height_zoom_out_fast(event):
    _h = min(h + 20, sh - y)
    root.geometry(f"{w}x{_h}")

def show_info(event):
    global Info_show
    Info_show = not Info_show
    info.toggle_label(event)  
        
def copy_info(event):
    root.clipboard_clear()
    root.clipboard_append(pos_txt)
    root.update()

def key_chars(event):
    global alpha,Full_screen
    
    if event.char in "aA":     #increase transparent      
        alpha = max(alpha - 0.1, 0.3)
        root.attributes('-alpha', alpha)
    elif event.char in "cC":   #center the window
        root.geometry(f"+{int((sw-w)/2)}+{int((sh-h)/2)}")
    elif event.char in "fF":   #full screen
        #print(root.state())
        if not Full_screen:
            root.attributes("-fullscreen", True)
        else:
            root.attributes("-fullscreen", False)
        Full_screen = not Full_screen   
        print(root.state())    
    elif event.char in "iI":   #show/hode info
        show_info(event)      
    elif event.char in "qQ":   #exit
        quit()
    elif event.char in "zZ":   #decrease transparent
        alpha = min(alpha + 0.1, 0.9)
        root.attributes('-alpha', alpha)
    else:
        pass

def update_info():
    global pos_ttl,pos_txt,x,y,w,h,sw,sh

    x = root.winfo_x()
    y = root.winfo_y()
    w = root.winfo_width()
    h = root.winfo_height()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    pos_ttl = f"({x},{y}) w {w}, h {h+26}"
    pos_txt = f"Left(x): {x}\nTop(y): {y}\n Width: {w} ({sw})\nHeight: {h+26} ({sh})"
    root.title(pos_ttl)
    if Info_show:
        info.label.config(text=pos_txt+tips)

    root.after(300,update_info)

class InfoLabel:
    global pos_txt,Info_show
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(root, text="", bg="lightblue", font=("Arial", 10), anchor="nw", justify="left", padx=5, pady=5)
        self.label.pack(fill=tk.BOTH, expand=True)

    def toggle_label(self, event=None):        
        if Info_show:
            self.label.pack(fill=tk.BOTH, expand=True)  # 重新显示 Label            
        else:
            self.label.pack_forget()  # 隐藏 Label 
            
class Main:  
    def __init__(self):
        self.root = tk.Tk() 
        self.root.title("")
        self.root.geometry("400x374+500+100")
        self.root.attributes("-transparentcolor", "white")
        self.root.attributes("-alpha", alpha)
        self.root.attributes("-toolwindow", True)
        self.root.wm_attributes('-topmost', 1)

        self.root.bind("<Key>", key_chars)
        self.root.bind("<MouseWheel>", adjust_trans) # for Windows/MacOS
        self.root.bind("<Button-4>", adjust_trans)   # for Linux
        self.root.bind("<Button-5>", adjust_trans)   # for Linux
        self.root.bind('<Up>', move_up)
        self.root.bind('<Down>', move_down)
        self.root.bind('<Left>', move_left)
        self.root.bind('<Right>', move_right)
        self.root.bind('<Shift-Up>', move_up_fast)
        self.root.bind('<Shift-Down>', move_down_fast)
        self.root.bind('<Shift-Left>', move_left_fast)
        self.root.bind('<Shift-Right>', move_right_fast)
        self.root.bind('<Control-Up>', height_zoom_in)
        self.root.bind('<Control-Down>', height_zoom_out)
        self.root.bind('<Control-Left>', width_zoom_in)
        self.root.bind('<Control-Right>', width_zoom_out)
        self.root.bind('<Control-Shift-Up>', height_zoom_in_fast)
        self.root.bind('<Control-Shift-Down>', height_zoom_out_fast)
        self.root.bind('<Control-Shift-Left>', width_zoom_in_fast)
        self.root.bind('<Control-Shift-Right>', width_zoom_out_fast)
        self.root.bind("<Double-1>", show_info)
        self.root.bind('<Button-3>', copy_info)
        self.root.bind('<Control-c>', copy_info)
        self.root.bind('<Control-C>', copy_info)
        
if __name__ == '__main__':
    main = Main() 
    root = main.root
    info = InfoLabel(root)
    update_info()  
    root.mainloop()
