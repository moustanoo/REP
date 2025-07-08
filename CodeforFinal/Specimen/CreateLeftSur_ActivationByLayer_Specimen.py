from abaqus import *
from abaqusConstants import *

#Set a model name
model_name = 'DFE2_2D_13_CF_PEEK_distribute5_Void18_Test'

# Set a number of step per Layer and Number of Layer
Number_Layer = 16

#Set a instance name
instance_name = 'SPECIMEN-1#MACROELEMENT-1'

#CreateSurface
for j in range(1, Number_Layer+1, 1):

    string_1 = 'Specimen_LeftSur_Layer{}'.format(j)
   
    mdb.models[model_name].rootAssembly.Surface(face4Elements=
            mdb.models[model_name].rootAssembly.instances[instance_name].elements.sequenceFromLabels(labels=((50*j)-49,))
            , name=string_1)
    
#CreateFilm

for k in range(1, Number_Layer+1, 1):

    string_1 = 'Specimen_Layer_{}'.format(k)
    string_2 = 'Specimen_Conv_Left_Layer{}'.format(k)
    string_3 = 'Specimen_LeftSur_Layer{}'.format(k)
    string_4 = 'Specimen_Radia_Left_Layer{}'.format(k)


    mdb.models[model_name].FilmCondition(createStepName=string_1, definition=
        EMBEDDED_COEFF, filmCoeff=0.071, filmCoeffAmplitude='', name=string_2
        , sinkAmplitude='', sinkDistributionType=UNIFORM, sinkFieldName='', 
        sinkTemperature=100.0, 
        surface=mdb.models[model_name].rootAssembly.surfaces[string_3])
        
    mdb.models[model_name].RadiationToAmbient(ambientTemperature=100.0, 
        ambientTemperatureAmp='', createStepName=string_1, distributionType=UNIFORM, 
        emissivity=0.6, field='', name=string_4, radiationType=AMBIENT, 
        surface=mdb.models[model_name].rootAssembly.surfaces[string_3])
