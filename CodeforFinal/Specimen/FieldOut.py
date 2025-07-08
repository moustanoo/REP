from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from mesh import *
from visualization import *
from connectorBehavior import *

#Set a model name
model_name = 'DFE2_2D_13_CF_PEEK_distribute5_Void18_Test'

# Set a number of step per Layer and Number of Layer
Number_Layer = 16

for k in range(1, Number_Layer+1, 1):

    string_1 = 'Specimen_Layer_{}'.format(k)
    string_2 = 'F-Output-{}'.format(k+5)

    mdb.models[model_name].FieldOutputRequest(createStepName=
        string_1, name=string_2, variables=('CDISP', 'CSTRESS', 'E', 
        'MISES', 'NT', 'RFL', 'S', 'TEMP', 'THE', 'U', 'UT'))