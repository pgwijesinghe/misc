import matplotlib as mpl
from pylab import *
from qutip import *
from matplotlib import cm
import imageio
from qutip.qip.operations.gates import *

def animate_bloch(states, duration=0.1, save_all=False):

    b = Bloch()
    b.vector_color = ['r']
    b.view = [-40,30]
    images=[]
    try:
        length = len(states)
    except:
        length = 1
        states = [states]
    ## normalize colors to the length of data ##
    nrm = mpl.colors.Normalize(0,length)
    colors = cm.summer(nrm(range(length))) # options: cool, summer, winter, autumn etc.

    ## customize sphere properties ##
    b.point_color = list(colors) # options: 'r', 'g', 'b' etc.
    b.point_marker = ['o']
    b.point_size = [30]
    
    for i in range(length):
        b.clear()
        b.add_states(states[i])
        b.add_states(states[:(i+1)],'point')
        if save_all:
            b.save(dirc='tmp') #saving images to tmp directory
            filename="tmp/bloch_%01d.png" % i
        else:
            filename='temp_file.png'
            b.save(filename)
        images.append(imageio.imread(filename))
    imageio.mimsave('bloch_anim.gif', images, duration=duration)

gates = {'(identity)' : qeye(2),
        '(+pi_x)' : rx(np.pi),
        '(-pi_x)' : rx(-np.pi),
        '(+pi_y)' : ry(np.pi),
        '(-pi_y)' : ry(-np.pi),
        '(+pi/2_x)' : rx(np.pi /2),
        '(-pi/2_x)' : rx(-np.pi /2),
        '(+pi/2_y)' : ry(np.pi/2),
        '(-pi/2_y)' : ry(-np.pi/2),
        '(+pi_z)': rz(np.pi),
        '(-pi_z)': rz(-np.pi),
        '(+pi/2_z)': rz(np.pi / 2),
        '(-pi/2_z)': rz(-np.pi / 2)
        }

final_gate_seq = ['(+pi_y)', '(+pi/2_x)', '(+pi_x)', '(+pi/2_x)', '(+pi_x)', '(-pi/2_y)', '(-pi_y)', '(-pi/2_y)', '(-pi_y)', '(-pi/2_z)', '(+pi_y)']
res = basis(2,0)
states = []
for g in final_gate_seq:
    res = gates[g]*res
    states.append(res)

animate_bloch(states, duration=0.5, save_all=False)