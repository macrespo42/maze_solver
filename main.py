from window import Line, Point, Window


def main() -> None:
    win = Window(800, 600)
    line = Line(Point(100, 100), Point(500, 500))
    win.draw_line(line)
    win.wait_for_close()


if __name__ == "__main__":
    main()
