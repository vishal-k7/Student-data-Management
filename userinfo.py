import pandas as pd
import numpy as np
 
data = {'name': ['xy', 'abc', 'vishal', 'cds', 'hello'],
        'age': [15, 17, 20, 18, 16],
        'branch': [cse, ece,eee,mech,it],'year-sem': [1-1, 2-2, 1-2, 3-1, 4-1],'score': [95, 67, 70, 68, 86],}
 
df = pd.DataFrame(data, index = ['Acme', 'Acme', 'Bilbao', 'Bilbao', 'Bilbao'])
 
df_filtered = df.query('score>70')
print(df_filtered)