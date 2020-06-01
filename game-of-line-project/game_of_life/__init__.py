#
#******************************************************************#
#   This is the Game of Life implementation.
#   The code uses the Game of Life by electronut.in as a reference!!
#******************************************************************#
def run():

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    #**********Create the pop function to re-populate the generations *************

    def pop(data):
    
        newGenaration = Genaration.copy( )
        for i in range (N):
            for j in range (N):
                total= (Genaration[(i-1)%N][(j-1)%N]+Genaration[(i-1)%N][j]+Genaration[(i-1)%N][(j+1)%N]+
                    Genaration[i][(j-1)%N]+Genaration[i][(j+1)%N]+ Genaration[(i+1)%N][(j-1)%N]+
                    Genaration[(i+1)%N][j]+ Genaration[(i+1)%N][(j+1)%N])
                
                if Genaration[i][j]== 1:
                        
                        if total>3 or total<2:
                            newGenaration[i][j]= 0
                elif total==3:
                    newGenaration[i][j]= 1

        img.set_data(newGenaration)
        Genaration[:] = newGenaration[:]
        return img

    #********Ask user for the size of the grid and the number of genarations*******

    def get_integer_value(prompt, low, high):
        """
            Asks the user for integer input and between given bounds low and high.
            """
        while True:
            try:
                value = int(input(prompt))
            except ValueError:
                print("Input was not a valid integer value.")
                continue
            if value < low or value > high:
                    print("Input was not inside the bounds (value <= {0} or value >= {1}).".format(low, high))
            else:
                    break
        return value

    N = get_integer_value("Enter the size of the grid (suqare, between 10-100): ", 10, 100)
    M = get_integer_value("Enter the number of generations (1-100000): ", 10, 1000)

    SPEED = 500
    PROB_LIFE = 40

    #************** Ask user for the initial pattern ******************************

    while True:
        pattern = int(input("Enter 1 (or 2) to run the game with a cross-shaped pattern (or a random initial pattern): "))
        if pattern == 2:
            Genaration= np.random.choice([0,1], N*N, p=[1-((PROB_LIFE)/100),(PROB_LIFE)/100]).reshape(N,N)
            break
        elif pattern == 1:
            Genaration=np.zeros((N,N), dtype=int)
            initial_pattern = np.array([[0,1,0],[1,1,1],[0,1,0]])
            Genaration[int(N/2):int(N/2)+3,int(N/2):int(N/2)+3] = initial_pattern
            break
        else:
            print("Input was not a valid integer value.")
            continue


    fig, ax = plt.subplots( )
    img = ax.imshow(Genaration)
    ani = animation.FuncAnimation( fig, pop, frames = M, interval = SPEED,
                              save_count = 10, repeat = False)
    plt.show( )
