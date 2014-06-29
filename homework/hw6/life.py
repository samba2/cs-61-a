import io
import time

_NEIGHBORS = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)

class life:
    """A game of Conway's Life.  The board is finite and toroidal (that is, the cells
    on the right edge are immediately to the left of the cells on the left, and the
    cells of the first row are immediately below those of the last.)"""

    def __init__(self, nrows, ncols):
        """Default initialization of an NROWS x NCOLS board."""
        self._nrows = nrows
        self._ncols = ncols

    def __str__(self):
        """A (printable) string that displays the current contents of the board."""
        out = io.StringIO()
        for r in range(self.rows):
            for c in range(self.cols):
                print('*' if self.is_alive(r, c) else '-', end='', file=out)
            print(file=out)
        return out.getvalue()

    def set_board(self, board):
        """Sets the values of is_alive(r, c) from the values extracted from BOARD,
        which should be a sequence (iterable) of sequences (iterables)
        returning values representing occupied or unoccupied Life cells.
        Each element of BOARD (up to SELF.rows elements) is used to fill
        consecutive rows of SELF with up to SELF.cols values each. The
        values iterated by the rows of BOARD are interpreted according to
        the live_value method.  Any leftover rows or columns from BOARD are
        discarded.  Any unfilled cells of SELF are set unoccupied."""

        for r in range(self.rows):  # init with false
            for c in range(self.cols):
                self.set_alive(r, c, False)

        for r, row in enumerate(board):
            if r >= self.rows:
                break
            for c, val in enumerate(row):
                if c >= self.cols:
                    break
                self.set_alive(r, c, life.live_value(val))

    def is_alive(self, r, c):
        """True iff there is an organism alive at column C of row R.  R and C
        wrap around, as on a toroidal board."""
        return self._is_alive(r % self.rows, c % self.cols)

    def set_alive(self, r, c, livep):
        """Set is_alive(R, C) to LIVEP."""
        self._set_alive(r % self.rows, c % self.cols, livep)

    def neighbors(self, r, c):
        """The number of living neighbors of the cell at column C of row R."""
        sum = 0
        for i, j in _NEIGHBORS:
            sum += bool(self.is_alive(r+i, c+j))
        return sum

    def survives(self, r, c):
        """True iff the next generation will have an occupant at R, C."""
        return life.will_live(self.is_alive(r, c), self.neighbors(r, c))

    @property
    def rows(self):
        return self._nrows

    @property
    def cols(self):
        return self._ncols

    @staticmethod
    def will_live(now_alive, neighbors):
        """True iff a cell with NEIGHBORS live neighboring cells, and that
        currently contains a live organism iff NOW_ALIVE is true, will
        contain a living organism in the next generation."""
        return (now_alive and 2 <= neighbors <= 3) or \
               (not now_alive and neighbors == 3)

    @staticmethod
    def live_value(v):
        """True iff V is an external representation of a live organism in
        a life board.  Live organisms are either 1-character strings
        other than " ", "_", or ".", or else true, non-string values."""
        if type(v) is str and len(v) >= 1:
            return v[0] not in ' ._'
        else:
            return bool(v)

    # Methods that must be overridden in each subtype.

    def _is_alive(self, r, c):
        """True iff there is an organism alive at column C of row R.  R and C
        must be within the bounds of the board."""
        raise NotImplemented

    def _set_alive(self, r, c, livep):
        """Set is_alive(R, C) to True iff LIVEP is a true value.  R and C must be
        within the bounds of the board."""
        raise NotImplemented

    def tick(self):
        """Update the board to the next generation."""
        raise NotImplemented

