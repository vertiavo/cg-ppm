from tkinter import Tk, PhotoImage, Canvas, NW, Scrollbar, RIGHT, NS

# Test file names
FILE_01 = ('ppm-test-01-p3.ppm', 'us-ascii')  # text/plain charset=us-ascii
FILE_02 = ('ppm-test-02-p3-comments.ppm', 'iso-8859-1')  # text/plain charset=iso-8859-1
FILE_03 = ('ppm-test-03-p6.ppm', 'binary')  # application/octet-stream charset=binary
FILE_04 = ('ppm-test-04-p3-16bit.ppm', 'us-ascii')  # text/plain charset=us-ascii
FILE_05 = ('ppm-test-05-p6.ppm', 'binary')  # application/octet-stream charset=binary
FILE_06 = ('ppm-test-06-p6.ppm', 'binary')  # application/octet-stream charset=binary
FILE_07 = ('ppm-test-07-p3-big.ppm', 'iso-8859-1')  # text/plain charset=iso-8859-1
FILE_08 = ('ppm-test-08-p6-big.ppm', 'binary')  # text/plain charset=binary


def open_file(filename, charset='UTF-8'):
    directory = 'pictures/'
    if charset is 'binary':
        with open(directory + filename, 'rb') as file:
            t = tokenize(file)
            read_p6(t)
    else:
        with open(directory + filename, encoding=charset) as file:
            t = tokenize(file)
            read_p3(t)


def tokenize(file):
    for line in file:
        if line[0] is not '#':
            for t in line.split():
                if t is '#' or t.startswith('#'):
                    break
                else:
                    yield t


def read_p3(token):
    next_token = lambda: next(token)
    assert 'P3' == next_token(), 'Invalid PPM type'

    width, height, max_value = (int(next_token()) for i in range(3))
    root = Tk()
    image = PhotoImage(width=width, height=height)
    for h in range(0, height):
        for w in range(0, width):
            if max_value is 255:
                mask = '#%02x%02x%02x'
            else:
                mask = '#%04x%04x%04x'

            color = mask % tuple(int(next_token()) for i in range(3))
            image.put(color, (w, h))

    canvas = Canvas(root, width=600, height=500)
    canvas.grid(row=0, column=0, sticky='news')
    vertical_scrollbar = Scrollbar(root, orient='vertical', command=canvas.yview)
    vertical_scrollbar.grid(row=0, column=1, sticky='nes')
    horizontal_scrollbar = Scrollbar(root, orient='horizontal', command=canvas.xview)
    horizontal_scrollbar.grid(row=1, column=0, sticky='ews')
    canvas.configure(yscrollcommand=vertical_scrollbar.set)
    canvas.configure(xscrollcommand=horizontal_scrollbar.set)
    canvas.create_image(0, 0, image=image, anchor=NW)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()


def read_p6(token):
    next_token = lambda: next(token)
    assert 'P6' == next_token(), 'Invalid PPM type'


if __name__ == '__main__':
    open_file(*FILE_02)
