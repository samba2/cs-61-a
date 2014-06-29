import tkinter
import time

_tk_master = None
_disp_board = None

class life_display:
    """A display of a Life game. To use:
      >>> import hw6, life_gui
      >>> b = hw6.life_lists(...)
      >>> d = life_gui.life_display(b, title="My game", width=300, height=300)
      >>> d.play(20)
    Clicking on the display will toggle cells of the board.
    """

    def __init__(self, board, width=400, height=400, pixel_size=10,
                 title="Game of Life"):
        """A new graphical display of the Life game on BOARD. Use TITLE as
        the window title and initially make WIDTH x HEIGHT the size in
        pixels."""
        self._board = board
        self._tk_master = tkinter.Tk()
        self._tk_master.title("Game of Life")
        self._menubar = tkinter.Menu(self._tk_master)
        self._menubar.add_command(label="Quit", command=self._tk_master.quit)
        self._menubar.add_command(label="Step", command=self.play)
        self._menubar.add_command(label="Steps", 
                                  command=lambda: self.play(10))        
        self._tk_master.config(menu=self._menubar)

        self._disp_board = tkinter.Canvas(_tk_master, width=400, height=400,
                                          bg="black")
        self._disp_board.bind("<Button-1>", self._click)
        self._disp_board.pack()
        self.set_size(width, height, pixel_size=pixel_size)
        self.update()
    
    def set_board(self, new_board):
        """Update my board as indicated by NEW_BOARD and redisplay."""
        self._board.set_board(new_board)
        self.update()

    def play(self, generations=1, interval=0.02):
        """Advance my board by GENERATIONS generations, displaying each at
        intervals of INTERVAL seconds."""
        self.update()
        for g in range(generations):
            self._board.tick()
            self.update()
            time.sleep(interval)

    def _click(self, event):
        """Handle a mouse-click on my display by toggling the appropriate
        cell of my board."""
        r, c = event.y // self._pixel_size, event.x // self._pixel_size

        self._board.set_alive(r, c, not self._board.is_alive(r, c))
        self.update()

    def update(self):
        """Update display to reflect current state of board."""

        s = self._pixel_size
        self._disp_board.delete('gen')
        for r in range(self._board.rows):
            for c in range(self._board.cols):
                if self._board.is_alive(r, c):
                    self._disp_board.create_rectangle(c*s, r*s,
                                                      c*s+s, r*s+s,
                                                      fill="white", tags="gen")
        self._tk_master.update()

    def set_size(self, width, height, pixel_size=10):
        """Set the size of my display to WIDTH x HEIGHT pixels.  Set each cell
        to PIXEL_SIZE x PIXEL_SIZE"""
        self._disp_board.config(width=width, height=height)
        self._pixel_size = pixel_size
        self.update()
