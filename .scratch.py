
import pandas as pd

df_real = pd.read_csv('data/datasets_One_Year_of_FitBitChargeHR_Data.csv', index_col=0, parse_dates=True)

#df_rael.index = pd.to_datetime(df_real['Date'])


df_bar = df_real[['Minutes_sitting', 'Minutes_of_slow_activity', 'Minutes_of_moderate_activity',
             'Minutes_of_intense_activity']]

stacked = df_bar.stack().reset_index().rename(columns={
    'level_1': 'Activity',
    0: 'Minutes'
})


# stacked['Activity'] = stacked['Activity'].map(lambda x: x.lstrip('_').rstrip('Minutesof'))
stacked['Activity'] = stacked['Activity'].str.replace('Minutes_of_', '')

print(stacked)
print(stacked.columns)

