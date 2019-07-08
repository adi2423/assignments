def output(original, pre):

    if len(original) == 0:
        print (pre)
        return
    if len(original) == 1:
        print (pre + chr(96 + int(original)))
        return
    if int(original[0:2]) < 27:
        new_chr = chr(96 + int(original[0:2]))
        output(original[2:], pre + new_chr)
    new_chr = chr(96 + int(original[0:1]))
    output(original[1:], pre + new_chr)

if __name__ == '__main__':
    output('1123', '')
