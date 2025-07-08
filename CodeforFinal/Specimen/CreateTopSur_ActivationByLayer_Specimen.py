from abaqus import *
from abaqusConstants import *

#Set a model name
model_name = 'DFE2_2D_13_CF_PEEK_distribute5_Void18_Test'

# Set a number of step per Layer and Number of Layer
Number_Layer = 16

#Set a instance name
# instance_name = 'Specimen-1.MACROELEMENT-1'


for j in range(1, Number_Layer+1, 1):
    
    string_1 = 'Specimen_TopSur_Layer{}'.format(j)
    string_2 = 'Specimen_Layer_{}'.format(j)
    string_3 = 'Specimen_Conv_Top_Layer_{}'.format(j)
    string_4 = 'Specimen_Radia_Top_Layer_{}'.format(j)
    set_name = 'SPECIMEN-1#MACROELEMENT-1.MACRO-LAYER-{}'.format(j)
 
    mdb.models[model_name].rootAssembly.Surface(
    face3Elements=mdb.models[model_name].rootAssembly.sets[set_name].elements,name=string_1) 
    
    mdb.models[model_name].FilmCondition(createStepName=string_2, definition=
    EMBEDDED_COEFF, filmCoeff=0.071, filmCoeffAmplitude='', name=string_3
    , sinkAmplitude='', sinkDistributionType=UNIFORM, sinkFieldName='', 
    sinkTemperature=100.0, 
    surface=mdb.models[model_name].rootAssembly.surfaces[string_1])
    
    mdb.models[model_name].RadiationToAmbient(ambientTemperature=100.0, 
    ambientTemperatureAmp='', createStepName=string_2, distributionType=UNIFORM, 
    emissivity=0.6, field='', name=string_4, radiationType=AMBIENT, 
    surface=mdb.models[model_name].rootAssembly.surfaces[string_1])

print("Surface TopCreate!!")