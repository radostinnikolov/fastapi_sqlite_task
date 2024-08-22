import sqlalchemy
import pandas as pd

engine=sqlalchemy.create_engine('sqlite:////app/db/db_service2.db') # ensure this is the correct path for the sqlite file.


info = pd.read_sql('select * from user_info',engine)
names = info.loc[:,"sender_name"].values.tolist()
emails = info.loc[:,"sender_email"].values.tolist()
phones = info.loc[:,"sender_phone"].values.tolist()
for i in range(len(names)):
    print(
        f'''
        To: {emails[i]}
        Hello, {names[i]},
        Your order was received. You will receive SMS on {phones[i]} when the package is delivered to the receiver.
        '''
    )