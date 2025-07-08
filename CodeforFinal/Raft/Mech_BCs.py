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

mdb.models['CombinedModel'].rootAssembly.Set(edges=
    mdb.models['CombinedModel'].rootAssembly.instances['buildplate-1'].edges.getSequenceFromMask(
    ('[#1 ]', ), ), name='Bottom_Buildplate')
mdb.models['CombinedModel'].EncastreBC(createStepName='Initial', localCsys=None
    , name='Encastre', region=
    mdb.models['CombinedModel'].rootAssembly.sets['Bottom_Buildplate'])
mdb.models['CombinedModel'].rootAssembly.Set(name='Pin_Specimen', nodes=
    mdb.models['CombinedModel'].rootAssembly.instances['Raft-1.MACROELEMENT-1'].nodes.getSequenceFromMask(
    mask=('[#ffffffff:3 #1f ]', ), ))
mdb.models['CombinedModel'].PinnedBC(createStepName='Initial', localCsys=None, 
    name='Pin_Specimen', region=
    mdb.models['CombinedModel'].rootAssembly.sets['Pin_Specimen'])