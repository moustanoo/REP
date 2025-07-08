from abaqus import *
from abaqusConstants import *

# Access model
model_name = 'DFE2_2D_13_CF_PEEK_distribute5_Void18_Test'
model = mdb.models[model_name]

#Set a number of step per Layer and Number of Layer
Number_Layer = 16
   
for i in range(1, Number_Layer+1):
        
        activation_name = 'Specimen_Activation1_L{}'.format(i)  # Unique name for model change
        active_set_name = 'SPECIMEN-1#ACTIVE1_L{}'.format(i)  # Set of elements to activate
        step_name = 'Specimen_Layer_{}'.format(i)  # Step in which activation occurs

        model.ModelChange(
            activeInStep=True,  # Activation means elements are turned on
            createStepName=step_name,  # Happens in step 'ReacX'
            includeStrain=False,
            name=activation_name,
            region=model.rootAssembly.sets[active_set_name],  # Activate corresponding set
            regionType=ELEMENTS
        )
