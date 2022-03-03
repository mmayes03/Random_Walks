import matplotlib.pyplot as plt
from Create_walks import RandomWalk as rw

def Walks():
    My_rw = rw(5000) #number of walks
    My_rw.fill_walk()
    point_numbers = list(range(My_rw.numberofpoints)) #keeps track of steps
    plt.scatter(My_rw.x_values, My_rw.y_values, s = 10, c = point_numbers, cmap= plt.cm.Blues, edgecolors= 'none')
    # plt.plot(My_rw.x_values, My_rw.y_values, linewidth = 1)
    plt.scatter(My_rw.x_values[0], My_rw.y_values[0], c = 'Green', s = 20) #First step
    plt.scatter(My_rw.x_values[-1], My_rw.y_values[-1], c = 'Red', s = 20)
    plt.title("Random Walks Generated")
    plt.xlabel("Forward & Backward Direction") 
    plt.ylabel("Up & Down Direction") 
    # plt.axis('off')
    # plt.axis('off')
    # plt.show()
    plt.savefig('Rand_walks.png')
def Repeat_Walks():
    Walks()
    plt.show()
    while True:
        
        Walks()
        
        user = input("Show again?")
        if user == 'no':
            break
        elif user == 'yes':
            plt.show()   
        else:
            print("Must type 'yes' or 'no'")
            
Repeat_Walks()