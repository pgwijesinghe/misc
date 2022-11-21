import pandas as pd
import matplotlib.pyplot as plt

datafile = ".\Dataset.csv"
biomass_list = ["Switchgrass", "Miscanthus", "Wheat Straw", "SRC Willow"]
energy_list = ["EE", "PE", "CE"]

df = pd.read_csv(datafile)  # read from the datafile and initiate a dataframe

fig, ax = plt.subplots(nrows=4, ncols=3)  # initiating a set of axes for the plots (4x3 matrix)

row = 0  # row index of the grid
for biomass in biomass_list:  # loops through each biomass entry (main outer loop)
    i = df.index[df["Biomass"] == biomass].tolist()[0]
    col = 0  # column index of the grid
    for energy in energy_list:  # for each biomass entry, loops through energy types (main inner loop)
        axes = ax[row, col]  # current axis (out of the 12 axes)
        j = [int(x) for x in df.index[df["Energy"] == energy].tolist() if i <= x <= i+11][0]
        if biomass == "SRC Willow": k, k_full = df.iloc[j:j+3, 2:13], df.iloc[j:j+3, 2:15]
        else: k, k_full = df.iloc[j:j+4, 2:13], df.iloc[j:j+4, 2:15]
        lower_bounds = k_full.iloc[:4, 12].tolist()
        upper_bounds = k_full.iloc[:4, 11].tolist()

        k.plot(kind="bar", stacked=True, ax=axes, legend=None)  # stacked bar plot
        for idx in range(3):  # loops through each stack to plot the error bars
            axes.vlines(idx, lower_bounds[idx], upper_bounds[idx])
            if biomass != "SRC Willow": axes.vlines(idx+1, lower_bounds[idx+1], upper_bounds[idx+1])

        countries = k_full.iloc[:4, 0].tolist()
        axes.set_xticklabels(countries, rotation=0)  # setting the x-labels
        col += 1
    row += 1

# setting grid titles
for axs, col in zip(ax[0, :], energy_list):
    axs.set_title(col)

for axs, row in zip(ax[:, 0], biomass_list):
    axs.set_ylabel(f"{row}\n\n kJ", size='large')

# adding the legend
arr = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*arr)]
fig.legend(lines[:10], labels[:10], loc='upper right', fontsize='x-small')

plt.show()
