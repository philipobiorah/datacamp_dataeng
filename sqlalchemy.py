#import necessary modules
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Chinook.sqlite')




table_names = engine.table_names()

print(table_names)
#output: ['Album', 'Artist', 'Customer', 'Employee', 'Genre', 'Invoice', 'InvoiceLine', 'MediaType', 'Playlist', 'PlaylistTrack', 'Track']




#Open engine connection: con
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")

    #Save the reuslts of the query to DataFrame: df
    # df = pd.DataFrame(rs.fetchall())

    #retrrive e records 
    df = pd.DataFrame(rs.fetchmany(size=3))

print(df.head())