# Test file names
FILE_01 = ('ppm-test-01-p3.ppm', 'us-ascii')  # text/plain charset=us-ascii
FILE_02 = ('ppm-test-02-p3-comments.ppm', 'iso-8859-1')  # text/plain charset=iso-8859-1
FILE_03 = ('ppm-test-03-p6.ppm', 'binary')  # application/octet-stream charset=binary
FILE_04 = ('ppm-test-04-p3-16bit.ppm', 'us-ascii')  # text/plain charset=us-ascii
FILE_05 = ('ppm-test-05-p6.ppm', 'binary')  # application/octet-stream charset=binary
FILE_06 = ('ppm-test-06-p6.ppm', 'binary')  # application/octet-stream charset=binary
FILE_07 = ('ppm-test-07-p3-big.ppm', 'iso-8859-1')  # text/plain charset=iso-8859-1
FILE_08 = ('ppm-test-08-p6-big.ppm', 'binary')  # text/plain charset=binary


def open_file(filename, charset="UTF-8"):
    if charset is 'binary':
        with open('pictures/' + filename, "rb") as file:
            for line in file:
                print(line)
    else:
        with open('pictures/' + filename, encoding=charset) as file:
            for line in file:
                print(line)


if __name__ == '__main__':
    open_file(*FILE_01)
