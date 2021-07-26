import matplotlib as mil
mil.use('TkAgg')
import matplotlib.pyplot as plt
from Main import potentiel_test 
class Basegraph(object):
    def __init__(self):
        self.Y_label = "Your y_label"
        self.X_label = "Your x_label"
        self.show_grid = True
        self.title = "Your graph title"
        
    # Start of user code -> properties/constructors for Basegraph class

    # End of user code
    def show(self):
        # Start of user code protected zone for show function body
        x_values = range(0,8760,1)
        y_values = potentiel_test.Potentiel_solaire_theo()
        plt.plot(x_values, y_values, '.')
        plt.xlabel(self.X_label)
        plt.ylabel(self.Y_label)
        plt.title(self.title)
        plt.grid(self.show_grid)
        plt.show()
        
        # End of user code	
    # Start of user code -> methods for Basegraph class

    # End of user code

