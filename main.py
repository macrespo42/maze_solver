from cell import Cell
from window import Window


def main() -> None:
    win = Window(800, 600)
    first_cell = Cell(win)
    first_cell.draw(100, 100, 500, 500)
    win.wait_for_close()


if __name__ == "__main__":
    main()
