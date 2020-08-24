names = ['% Iron Feed', '% Silica Feed', 'Starch Flow', 'Amina Flow',
       'Ore Pulp Flow', 'Ore Pulp pH', 'Ore Pulp Density',
       'Flotation Column 01 Air Flow', 'Flotation Column 02 Air Flow',
       'Flotation Column 03 Air Flow', 'Flotation Column 04 Air Flow',
       'Flotation Column 05 Air Flow', 'Flotation Column 06 Air Flow',
       'Flotation Column 07 Air Flow', 'Flotation Column 01 Level',
       'Flotation Column 02 Level', 'Flotation Column 03 Level',
       'Flotation Column 04 Level', 'Flotation Column 05 Level',
       'Flotation Column 06 Level', 'Flotation Column 07 Level',
       '% Iron Concentrate', '% Silica Concentrate']


ts = 175
for x in range(1,data_mining.shape[1]):
  data = [] #clear data 
  n = 0 #set counter

  while n*ts <= round(data_mining.shape[0]):
    sample_mean_value = data_mining.iloc[(ts*n):(ts*(n+1)),x].mean()  #sampling data and save mean of n*ts elements
    data += [sample_mean_value]   #save sampling into a list
    data_array = np.array(data)   #list to array
    data_array= np.transpose(data_array)  #transpose
    df = pd.DataFrame(data_array)   #array to dataframe
    n += 1  #counter up 

  if x == 1:
    df_first = df
  if x == 2:
    new_df = pd.concat([df_first, df], axis = 1)
  if x > 2: 
    new_df = pd.concat([new_df, df], axis=1) 

new_df.columns = names
