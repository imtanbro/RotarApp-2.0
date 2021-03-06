import pandas as pd
import random
import string
from Auth.models import Account

def get_random_password_string(length):
    password_characters = string.ascii_letters + string.digits + '@' + '-'
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

csvFile = 'usernames.csv'
df = pd.read_csv(csvFile)

df['rc']='rc'
df['username'] = df['rc']+df['Name2']
for row, index in df.iterrows() :
    username = str(index['username']).lower().replace(' ','')
    password = get_random_password_string(8)
    df.at[row,'password']=password
    df.at[row,'username']=username
df.drop('rc',axis=1,inplace=True)

df.to_csv('credentials.csv',index=False) 


# Query
# SELECT sum(FemaleCount) AS Number 
# FROM SecReport_membermatrix 
# JOIN SecReport_report ON SecReport_membermatrix.reportId_id = SecReport_report.reportId
# WHERE SecReport_membermatrix.attribute_id=4 and SecReport_report.month_id=9;