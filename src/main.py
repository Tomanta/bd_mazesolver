from graphics import Window, Point, Line

def main():
    win = Window(800, 600)

    p1 = Point(5,5)
    p2 = Point(20,15)
    l1 = Line(p1, p2)

    p3 = Point(20,15)
    p4 = Point(150,159)
    l2 = Line(p3, p4)

    p5 = Point(20,15)
    p6 = Point(75,262)
    l3 = Line(p5, p6)


    win.draw_line(l1, fill_color="red")
    win.draw_line(l2, fill_color="blue")
    win.draw_line(l3, fill_color="green")

    win.wait_for_close()

if __name__ == "__main__":
    main()