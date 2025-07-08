from abaqus import *
from abaqusConstants import *

# Access the model
model_name = 'DFE2_2D_13_CF_PEEK_distribute5_Void18_Test'
model = mdb.models[model_name]

# Define initial step name
initial_step = 'Initial'  

previous_step = initial_step  # Start from 'Reac1_L1'

#Layer_1
step_name_1 = 'Raft_Layer_1'
model.CoupledTempDisplacementStep(
        name=step_name_1,
        previous=previous_step,
        deltmx=10.0,
        initialInc=0.012827,
        maxInc=1282.7,
        minInc=1e-10,
        maxNumInc=10000,
        timePeriod=1282.7
)

#Layer_2
step_name_2 = 'Raft_Layer_2'
model.CoupledTempDisplacementStep(
        name=step_name_2,
        previous=step_name_1,
        deltmx=10.0,
        initialInc=0.01952078,
        maxInc=1952.078,
        minInc=1e-10,
        maxNumInc=10000,
        timePeriod=1952.078
)

#Layer_3
step_name_3 = 'Raft_Layer_3'
model.CoupledTempDisplacementStep(
        name=step_name_3,
        previous=step_name_2,
        deltmx=10.0,
        initialInc=0.01952078,
        maxInc=1952.078,
        minInc=1e-10,
        maxNumInc=10000,
        timePeriod=1952.078
)

#Layer_4
step_name_4 = 'Raft_Layer_4'
model.CoupledTempDisplacementStep(
        name=step_name_4,
        previous=step_name_3,
        deltmx=10.0,
        initialInc=0.051005,
        maxInc=5100.5,
        minInc=1e-10,
        maxNumInc=10000,
        timePeriod=5100.5
)

#Layer_5
step_name_5 = 'Raft_Layer_5'
model.CoupledTempDisplacementStep(
        name=step_name_5,
        previous=step_name_4,
        deltmx=10.0,
        initialInc=0.051005,
        maxInc=5100.5,
        minInc=1e-10,
        maxNumInc=10000,
        timePeriod=5100.5
)

print("All steps created successfully.")
