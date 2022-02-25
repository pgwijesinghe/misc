"""GRAPH 1: ENERGY"""

import pandas as pd
import matplotlib.pyplot as plt

datafile = ".\Results.xlsx"
df = pd.read_excel(datafile, 'Energy (2)')

fig, ax = plt.subplots(nrows=5, ncols=3, gridspec_kw={'wspace': 0.3, 'hspace': 0.8})

biomass_list = ["Switchgrass", "Miscanthus", "Wheat Straw", "SRC Willow", "Forest Residue"]
energy_list = ["CEcD", "CEpD", "CEel_eqD"]

row = 0  # row index of the grid
for biomass in biomass_list:  # loops through each biomass entry (main outer loop)
    i = df.index[df["Biomass type"] == biomass].tolist()[0]
    col = 0  # column index of the grid

    for energy in energy_list:  # for each biomass entry, loops through energy types (main inner loop)
        axes = ax[row, col]  # current axis (out of the 12 axes)  
        axes.set_ylim([0,18])     
        if biomass == "SRC Willow": 
            j = [int(x) for x in df.index[df["Cumulative energy demand"] == energy].tolist() if i <= x <= i+8][0]
            k, k_full = df.iloc[j:j+3, 2:12], df.iloc[j:j+3, 2:14]
            lower_bounds = k_full.iloc[:3, 11].tolist()
            upper_bounds = k_full.iloc[:3, 10].tolist()
        elif biomass == "Forest Residue": 
            j = [int(x) for x in df.index[df["Cumulative energy demand"] == energy].tolist() if i <= x <= i+5][0]
            k, k_full = df.iloc[j:j+2, 2:12], df.iloc[j:j+2, 2:14]
            lower_bounds = k_full.iloc[:2, 11].tolist()
            upper_bounds = k_full.iloc[:2, 10].tolist()
        else: 
            j = [int(x) for x in df.index[df["Cumulative energy demand"] == energy].tolist() if i <= x <= i+14][0]
            k, k_full = df.iloc[j:j+5, 2:12], df.iloc[j:j+5, 2:14]
            lower_bounds = k_full.iloc[:5, 11].tolist()
            upper_bounds = k_full.iloc[:5, 10].tolist()

        # k.plot(kind="bar", stacked=True, ax=axes, legend=None, fontsize='large')  # stacked bar plot

        if biomass == "SRC Willow": k.plot.bar(stacked=True, ax=axes, legend=None, width=0.3, fontsize='large')
        elif biomass == "Forest Residue": k.plot.bar(stacked=True, ax=axes, legend=None, width=0.2, fontsize='large')
        else: k.plot.bar(stacked=True, ax=axes, legend=None, fontsize='large')
        
        if biomass == "SRC Willow": 
            axes.vlines(0, lower_bounds[0], upper_bounds[0])
            axes.vlines(1, lower_bounds[1], upper_bounds[1])
            axes.vlines(2, lower_bounds[2], upper_bounds[2])
        elif biomass == "Forest Residue":
            axes.vlines(0, lower_bounds[0], upper_bounds[0])
            axes.vlines(1, lower_bounds[1], upper_bounds[1])
        else:
            axes.vlines(0, lower_bounds[0], upper_bounds[0])
            axes.vlines(1, lower_bounds[1], upper_bounds[1])
            axes.vlines(2, lower_bounds[2], upper_bounds[2])
            axes.vlines(3, lower_bounds[3], upper_bounds[3])
            axes.vlines(4, lower_bounds[4], upper_bounds[4])

        countries = k_full.iloc[:5, 0].tolist()
        axes.set_xticklabels(countries, rotation=0)  # setting the x-labels
        col += 1
    row += 1

for axs in ax[:,0]: axs.set_title("(a)", fontweight='bold')
for axs, row in zip(ax[:, 1], biomass_list): axs.set_title(f"{row}\n(b)", fontweight='bold')
for axs in ax[:,2]: axs.set_title("(c)", fontweight='bold')

for axs in ax[:,0]: axs.set_ylabel("$ CE_{C}D \: (GJ/t_{DM}) $", fontsize=12)
for axs in ax[:,1]: axs.set_ylabel("$ CE_{P}D \: (GJ/t_{DM}) $", fontsize=12)
for axs in ax[:,2]: axs.set_ylabel("$ CE_{el\_eq}D \: (GJ/t_{DM}) $", fontsize=12)
    
# adding the legend
arr = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*arr)]
fig.legend(lines[:9], labels[:9], loc='upper right', fontsize='medium')

plt.show()

# fig.set_size_inches(19.20, 10.80)
# fig.savefig('test.svg', format='svg', dpi=600 )