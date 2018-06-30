import pandas as pd
import pickle

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])
concat = pd.concat([df1,df2])
print(concat)

concat = pd.concat([df1,df2,df3])
print(concat)

df4 = df1.append(df2)
print(df4)

df4 = df1.append(df3)
print(df4)

pickle_out = open('test.pickle','wb')
pickle.dump(df4, pickle_out)
pickle_out.close()


pickle_in = open('test.pickle','rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data)