import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import data file
#  *  for importing .txt file add ' delimiter="\t" ' to the pd.read_csv() function
data = pd.read_csv('intensity analysis_Main (1).txt', delimiter="\t")

# get channels list from 'data'
Channels = list(data.columns)[2:11]

# remove objects out of gate ('Cell')
data = data[data['Cells'] == 1].reset_index(drop=True)

# create dataframe for plotting (containing 'Well ' and all Mean Intensity columns)
plot_data = pd.DataFrame()
plot_data['Well'] = data['Well ']
for c in Channels:
    plot_data[c] = data[c]

# export mean intensity and std for each well in each channel
wells = pd.unique(plot_data['Well'])  # get list of wells
output_dataframe_MEAN = pd.DataFrame()
output_dataframe_STD = pd.DataFrame()
for w in wells:
    cur_well_data = plot_data[plot_data['Well'] == w].drop('Well', 1)
    output_dataframe_MEAN = output_dataframe_MEAN.append(cur_well_data.mean(), ignore_index=True)
    output_dataframe_STD = output_dataframe_STD.append(cur_well_data.std(), ignore_index=True)
# add 'Well' column to the output dataframes
output_dataframe_MEAN.insert(0, "Well", wells)
output_dataframe_STD.insert(0, "Well", wells)
# export dataframes to csv
output_dataframe_MEAN.to_csv('output mean.csv', index=0)
output_dataframe_STD.to_csv('output std.csv', index=0)


### Plot (plot for each channel) ###

plot_data_melted = pd.melt(plot_data, id_vars='Well', value_vars=Channels,
                           var_name='Channels', value_name='Mean Intensity')

# full data
sns.barplot(x='Well', y="Mean Intensity", hue="Channels", data=plot_data_melted).set_title("Full data plot")
plt.show()

# full data in subplots for each channel
fig, ax = plt.subplots(len(Channels))
i = 0  # index of subplot
for p in Channels:
    g = sns.barplot(data=plot_data, x='Well', y=p, ax=ax[i])
    i += 1










sns.barplot(data=data, x='Well ', y='Mean Intensity 561nm').set_title('Mean Intensity 561nm, full data')
plt.show()

sns.barplot(data=data, x='Well ', y='Mean Intensity 488nm').set_title('Mean Intensity 488nm, full data')
plt.show()

sns.barplot(data=data, x='Well ', y='Mean Intensity 405nm').set_title('Mean Intensity 405nm, full data')
plt.show()

sns.barplot(data=data, x='Well ', y='Mean Intensity mTsapphire').set_title('Mean Intensity mTsapphire, full data')
plt.show()

sns.barplot(data=data, x='Well ', y='Mean Intensity LSSmOrange').set_title('Mean Intensity LSSmOrange, full data')
plt.show()

sns.barplot(data=data, x='Well ', y='Mean Intensity CyOFP405FR').set_title('Mean Intensity CyOFP405FR, full data')
plt.show()

sns.barplot(data=data, x='Well ', y='Mean Intensity CyOFP488FR').set_title('Mean Intensity CyOFP488FR, full data')
plt.show()

sns.barplot(data=data, x='Well ', y='Mean Intensity TagRFP675').set_title('Mean Intensity TagRFP675, full data')
plt.show()

sns.barplot(data=data, x='Well ', y='Mean Intensity 640nm').set_title('Mean Intensity 640nm, full data')
plt.show()




# # sampled data plot
# sampled_data_for_plot = pd.read_csv('Sampled data for plotting.csv')
# sns.barplot(data=sampled_data_for_plot, x='Well ', y='Mean Intensity GFP')














