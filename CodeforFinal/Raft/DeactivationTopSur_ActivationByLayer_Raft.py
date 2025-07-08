from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

# Set a number of step per Layer and Number of Layer
Number_Layer = 5

model_name = 'DFE2_2D_13_CF_PEEK_distribute5_Void18_Test'

for j in range(1,Number_Layer,1):
        
    string_1 = 'Raft_Radia_Top_Layer_{}'.format(j)
    string_2 = 'Raft_Conv_Top_Layer_{}'.format(j)
    string_3 = 'Raft_Layer_{}'.format(j+1)
            
    mdb.models[model_name].interactions[string_1].deactivate(string_3)
    mdb.models[model_name].interactions[string_2].deactivate(string_3)