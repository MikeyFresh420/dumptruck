
def antmarch():
    return "The ants go marching "

numList = ["one by one", "two by two", "three by three", "four by four",
           "five by five", "six by six", "seven by seven", "eight by eight",
           "nine by nine", "ten by ten"]

actions = [" have some fun ", " tie his shoe ", " take a knee ", " shut the door ", " give high-fives ",
           " pick up sticks ", " look to heaven ", " fill a crate ", " draw a line ",
           " think again "]

def hurrah():
    return " Hurrah!! Hurrah!!"

def little():
    return "The little one stops to"

def ending():
    print("And they all go marching down...\nInto the ground\nTo get out\nof the rain\n Boom, Boom, Boom!!!")

def main():

    for i in range(9):
        print(antmarch() + numList[i] + hurrah())
        print(antmarch() + numList[i] + hurrah())
        print(antmarch() + numList[i] )
        print(little() + actions[i])
        ending()
        print()





main()
