import pandas as pd
import os

with open('./I94_SAS_Labels_Descriptions.SAS') as f:
    f_content = f.read()
    f_content = f_content.replace('\t', '')

def code_mapper(file, idx):
    f_content2 = f_content[f_content.index(idx):]
    f_content2 = f_content2[:f_content2.index(';')].split('\n')
    f_content2 = [i.replace("'", "") for i in f_content2]
    dic = [i.split('=') for i in f_content2[1:]]
    df = pd.DataFrame([[i[0].strip(), i[1].strip()] for i in dic if len(i) == 2])
    if not  os.path.exists('./code_mapper'):
        os.mkdir('./code_mapper')
    if idx.find('cntyl')>0:
        df.columns = ['code', 'country']
        df.to_csv('./code_mapper/i94cit_res.csv', index = False)
    elif idx.find('addrl')>0:
        df.columns = ['code', 'state']
        df.to_csv('./code_mapper/i94addr.csv', index = False)
    elif idx.find('prtl')>0:
        df.columns = ['code', 'port_of_entry']
        df.to_csv('./code_mapper/i94port.csv', index = False)
    elif idx.find('mode')>0:
        df.columns = ['code', 'transportation']
        df.to_csv('./code_mapper/i94mode.csv', index = False)
    else:
        df.columns = [0, 1]
    return df

i94cit_res = code_mapper(f_content, "i94cntyl")
i94port = code_mapper(f_content, "i94prtl")
i94mode = code_mapper(f_content, "i94model")
i94addr = code_mapper(f_content, "i94addrl")

