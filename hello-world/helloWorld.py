def yourname(name):
    if name == '':
        print ('Hello, Welcome!')
        return
    print ('Hello,' , name ,'!')
    return

if __name__ == "__main__":
    typedname = input('Enter your name : ')
    yourname(typedname)