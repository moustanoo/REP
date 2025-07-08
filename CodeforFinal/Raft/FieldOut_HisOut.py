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


mdb.models['CombinedModel'].FieldOutputRequest(createStepName=
    'Raft_Layer_2&3&4', name='F-Output-2', variables=('S', 'MISES', 'E', 'THE', 
    'U', 'UT', 'NT', 'TEMP', 'RFL'))
mdb.models['CombinedModel'].FieldOutputRequest(createStepName='Raft_Layer_5', 
    name='F-Output-3', variables=('S', 'MISES', 'E', 'THE', 'U', 'UT', 'NT', 
    'TEMP', 'RFL'))


mdb.models['CombinedModel'].HistoryOutputRequest(createStepName=
    'Raft_Layer_2&3&4', name='H-Output-2', variables=('CSTRESS', 'CDISP', 
    'FTEMP'))
mdb.models['CombinedModel'].HistoryOutputRequest(createStepName='Raft_Layer_5', 
    name='H-Output-3', variables=('CSTRESS', 'CDISP', 'FTEMP'))