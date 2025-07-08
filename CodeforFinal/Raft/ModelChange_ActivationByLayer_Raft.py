from abaqus import *
from abaqusConstants import *

# Access model
model_name = 'DFE2_2D_13_CF_PEEK_distribute5_Void18_Test'
model = mdb.models[model_name]

model.ModelChange(
            activeInStep=False,  # Activation means elements are turned on
            createStepName='Raft_Layer_1',  
            includeStrain=False,
            name='Raft_Active_L1',
            region=model.rootAssembly.sets['Raft_Deac'],  # Activate corresponding set
            regionType=ELEMENTS
                )       

model.ModelChange(
            activeInStep=True,  # Activation means elements are turned on
            createStepName='Raft_Layer_2',  
            includeStrain=False,
            name='Raft_Active_L2',
            region=model.rootAssembly.sets['RAFT-1#MACROELEMENT-1.MACRO-LAYER-2'],  # Activate corresponding set
            regionType=ELEMENTS
                )

model.ModelChange(
            activeInStep=True,  # Activation means elements are turned on
            createStepName='Raft_Layer_3',  
            includeStrain=False,
            name='Raft_Active_L3',
            region=model.rootAssembly.sets['RAFT-1#MACROELEMENT-1.MACRO-LAYER-3'],  # Activate corresponding set
            regionType=ELEMENTS
                )

model.ModelChange(
            activeInStep=True,  # Activation means elements are turned on
            createStepName='Raft_Layer_4',  
            includeStrain=False,
            name='Raft_Active_L4',
            region=model.rootAssembly.sets['RAFT-1#MACROELEMENT-1.MACRO-LAYER-4'],  # Activate corresponding set
            regionType=ELEMENTS
                )

model.ModelChange(
            activeInStep=True,  # Activation means elements are turned on
            createStepName='Raft_Layer_5',
            includeStrain=False,
            name='Raft_Active_L5',
            region=model.rootAssembly.sets['RAFT-1#MACROELEMENT-1.MACRO-LAYER-5'],
            regionType=ELEMENTS
                )       