help = input()
print(" start -> start the car \n stop -> stop the car \n quit -> Exit")
ch = input()
while ch.upper() == 'STOP':
    print("Car is not yet started")
    ch = input()
while(ch.upper() != "QUIT"):

    if(ch.upper() == 'START'):
        print("Car started. Ready to go")

    elif(ch.upper() == 'STOP'):
        print("Car stopped")

    else:
        print("Hey, I don't understand")

    ch = input()
    if (ch.upper() == 'START'):
        print("Car is already started")
        ch = input()
    else:
        print("Car is already stopped")
        ch = input()

print("Car game ends!")
