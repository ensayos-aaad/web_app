import pandas as pd
from clases import Person, Student

studens_df = pd.read_csv('test.csv', 
                         index_col='id', 
                         dtype = {'id': 'string', 'est_name': 'string', 'cel': 'string', 'email': 'string'}
                         sep=';')


# TODO: Validar cuando el dato no se encuentra
def getStudentData(id):
    return studens_df.loc[id][['est_name', 'cel', 'email']].values.tolist()
  



if __name__ == '__main__':    
    print(getStudentData('0000'))
    print()
    
