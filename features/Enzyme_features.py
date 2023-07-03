import pandas as pd

from base import Feature, get_arguments, generate_features

Feature.dir = 'feature_variables'

class BertzCT(Feature):
    def create_features(self):
        self.train['BertzCT'] = train['BertzCT']
        self.test['BertzCT'] = test['BertzCT']

class Chi1(Feature):
    def create_features(self):
        self.train['Chi1'] = train['Chi1']
        self.test['Chi1'] = test['Chi1']

class Chi1n(Feature):
    def create_features(self):
        self.train['Chi1n'] = train['Chi1n']
        self.test['Chi1n'] = test['Chi1n']

class Chi1v(Feature):
    def create_features(self):
        self.train['Chi1v'] = train['Chi1v']
        self.test['Chi1v'] = test['Chi1v']
   
class Chi2n(Feature):
    def create_features(self):
        self.train['Chi2n'] = train['Chi2n']
        self.test['Chi2n'] = test['Chi2n']

class Chi2v(Feature):
    def create_features(self):
        self.train['Chi2v'] = train['Chi2v']
        self.test['Chi2v'] = test['Chi2v']

class Chi3v(Feature):
    def create_features(self):
        self.train['Chi3v'] = train['Chi3v']
        self.test['Chi3v'] = test['Chi3v']

class Chi4n(Feature):
    def create_features(self):
        self.train['Ch4n'] = train['Chi4n']
        self.test['Chi4n'] = test['Chi4n']

class Chi2v(Feature):
    def create_features(self):
        self.train['Chi2v'] = train['Chi2v']
        self.test['Chi2v'] = test['Chi2v']

class EState_VSA1(Feature):
    def create_features(self):
        self.train['EState_VSA1'] = train['EState_VSA1']
        self.test['EState_VSA1'] = test['EState_VSA1']
 
class EState_VSA2(Feature):
    def create_features(self):
        self.train['EState_VSA2'] = train['EState_VSA2']
        self.test['EState_VSA2'] = test['EState_VSA2']
 
class ExactMolWt(Feature):
    def create_features(self):
        self.train['ExactMolWt'] = train['ExactMolWt']
        self.test['ExactMolWt'] = test['ExactMolWt']
 
class FpDensityMorgan1(Feature):
    def create_features(self):
        self.train['FpDensityMorgan1'] = train['FpDensityMorgan1']
        self.test['FpDensityMorgan1'] = test['FpDensityMorgan1']

class FpDensityMorgan2(Feature):
    def create_features(self):
        self.train['FpDensityMorgan2'] = train['FpDensityMorgan2']
        self.test['FpDensityMorgan2'] = test['FpDensityMorgan2']

class FpDensityMorgan3(Feature):
    def create_features(self):
        self.train['FpDensityMorgan3'] = train['FpDensityMorgan3']
        self.test['FpDensityMorgan3'] = test['FpDensityMorgan3']

class HallKierAlpha(Feature):
    def create_features(self):
        self.train['HallKierAlpha'] = train['HallKierAlpha']
        self.test['HallKierAlpha'] = test['HallKierAlpha']

class HeavyAtomMolWt(Feature):
    def create_features(self):
        self.train['HeavyAtomMolWt'] = train['HeavyAtomMolWt']
        self.test['HeavyAtomMolWt'] = test['HeavyAtomMolWt']
 
class Kappa3(Feature):
    def create_features(self):
        self.train['Kappa3'] = train['Kappa3']
        self.test['Kappa3'] = test['Kappa3']

class MaxAbsEStateIndex(Feature):
    def create_features(self):
        self.train['MaxAbsEStateIndex'] = train['MaxAbsEStateIndex']
        self.test['MaxAbsEStateIndex'] = test['MaxAbsEStateIndex']
 
class MinEStateIndex(Feature):
    def create_features(self):
        self.train['MinEStateIndex'] = train['MinEStateIndex']
        self.test['MinEStateIndex'] = test['MinEStateIndex']
  
class NumHeteroatoms(Feature):
    def create_features(self):
        self.train['NumHeteroatoms'] = train['NumHeteroatoms']
        self.test['NumHeteroatoms'] = test['NumHeteroatoms']
   
class PEOE_VSA10(Feature):
    def create_features(self):
        self.train['PEOE_VSA10'] = train['PEOE_VSA10']
        self.test['PEOE_VSA10'] = test['PEOE_VSA10']
     
class PEOE_VSA14(Feature):
    def create_features(self):
        self.train['PEOE_VSA14'] = train['PEOE_VSA14']
        self.test['PEOE_VSA14'] = test['PEOE_VSA14']
      
class PEOE_VSA6(Feature):
    def create_features(self):
        self.train['PEOE_VSA6'] = train['PEOE_VSA6']
        self.test['PEOE_VSA6'] = test['PEOE_VSA6']
       
class PEOE_VSA7(Feature):
    def create_features(self):
        self.train['PEOE_VSA7'] = train['PEOE_VSA7']
        self.test['PEOE_VSA7'] = test['PEOE_VSA7']
      
class PEOE_VSA8(Feature):
    def create_features(self):
        self.train['PEOE_VSA8'] = train['PEOE_VSA8']
        self.test['PEOE_VSA8'] = test['PEOE_VSA8']
  
class SMR_VSA10(Feature):
    def create_features(self):
        self.train['SMR_VSA10'] = train['SMR_VSA10']
        self.test['SMR_VSA10'] = test['SMR_VSA10']
   
class SMR_VSA5(Feature):
    def create_features(self):
        self.train['SMR_VSA5'] = train['SMR_VSA5']
        self.test['SMR_VSA5'] = test['SMR_VSA5']
  
class SlogP_VSA3(Feature):
    def create_features(self):
        self.train['SlogP_VSA3'] = train['SlogP_VSA3']
        self.test['SlogP_VSA3'] = test['SlogP_VSA3']
    
class VSA_EState9(Feature):
    def create_features(self):
        self.train['VSA_EState9'] = train['VSA_EState9']
        self.test['VSA_EState9'] = test['VSA_EState9']
 
class fr_COO(Feature):
    def create_features(self):
        self.train['fr_COO'] = train['fr_COO']
        self.test['fr_COO'] = test['fr_COO']
      
class fr_COO2(Feature):
    def create_features(self):
        self.train['fr_COO2'] = train['fr_COO2']
        self.test['fr_COO2'] = test['fr_COO2']


if __name__ == '__main__':
    args = get_arguments()

    train = pd.read_csv('C:\\Users\\ghibl\\Enzyme_Substrate\\data\input\\train.csv')
    test = pd.read_csv('C:\\Users\\ghibl\\Enzyme_Substrate\\data\input\\test.csv')

    generate_features(globals(), args.force)