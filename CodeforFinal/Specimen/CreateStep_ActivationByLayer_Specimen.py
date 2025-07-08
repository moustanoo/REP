from abaqus import *
from abaqusConstants import *

# Access the model
model_name = 'DFE2_2D_13_CF_PEEK_distribute5_Void18_Test'
model = mdb.models[model_name]

# Define the first step after Initial
initial_step = 'Raft_Layer_5'  
Step_name = 'Specimen_Layer_1'

# Create Specimen_Layer_1 as the first step after Initial
model.CoupledTempDisplacementStep(
    deltmx=10.0, initialInc=0.005, maxInc=5000, maxNumInc=100000, minInc=1e-12, 
    name='Specimen_Layer_1', previous='Raft_Layer_5', timePeriod=5000
)

# Set Reac1_L1 as the reference for the next steps
previous_step = Step_name  

# Set the number of steps per layer and the number of layers
Number_Layer = 16

# Loop to create steps per layer
for i in range(2, Number_Layer + 1):  # Loop over layers
    
    step_name = 'Specimen_Layer_{}'.format(i)  # Construct step name
        
    model.CoupledTempDisplacementStep(
        deltmx=10.0, initialInc=0.0025, maxInc=2500, minInc=1e-12,maxNumInc=100000, 
        name=step_name, previous=previous_step,  # Link to previous step correctly
        timePeriod=2500
        )  

    previous_step = step_name  # Update previous_step for proper step chaining

print("Step sequence created successfully.")
