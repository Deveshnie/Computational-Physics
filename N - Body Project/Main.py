import N_Body
import matplotlib.pyplot as plt
import random as ran



if __name__ == "__main__":

    system = N_Body.N_Body()

    system.populate_real_space_matrix()

    system.generate_density_matrix()

    system.generate_potential_matrix()

    system.update_particle_positions()

    system.print_test()



    print
    print

    print system.Grid_Size
