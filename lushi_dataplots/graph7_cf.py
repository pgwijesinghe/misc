"""GRAPH 7: CARBON FOOTPRINT"""

import pandas as pd
import matplotlib.pyplot as plt

datafile = ".\Results.xlsx"
df = pd.read_excel(datafile, 'Carbon footprint')

fig, ax = plt.subplots(nrows=3, ncols=2)
ax[2][1].set_visible(False)

biomass_list = ["Switchgrass", "Miscanthus", "Wheat Straw", "SRC Willow", "Forest Residue"]
country_list = ["USA", "EU", "India ", "Brazil", "UK"]
country_list_SRCW = ["USA", "EU", "UK"]
country_list_FR = ["USA", "UK"]

row,col = 0,0  # row index of the grid
for biomass in biomass_list:
    i = df.index[df["Biomass type"] == biomass].tolist()[0]

    if biomass == "Switchgrass": 
        axes = ax[0,0]
        k = df.iloc[i:i+5, 1:14]
        k_bounds = df.iloc[i:i+5, 14:16]
    elif biomass == "Miscanthus": 
        axes = ax[0,1]
        k = df.iloc[i:i+5, 1:14]
        k_bounds = df.iloc[i:i+5, 14:16]
    elif biomass == "Wheat Straw": 
        axes = ax[1,0]
        k = df.iloc[i:i+5, 1:14]
        k_bounds = df.iloc[i:i+5, 14:16]
    elif biomass == "SRC Willow": 
        axes = ax[1,1]
        k = df.iloc[i:i+3, 1:14]
        k_bounds = df.iloc[i:i+3, 14:16]
    elif biomass == "Forest Residue": 
        axes = ax[2,0]
        k = df.iloc[i:i+2, 1:14]
        k_bounds = df.iloc[i:i+2, 14:16]

    axes.set_ylim([0,3500])
    lower_bounds = k_bounds.iloc[:5, 1].tolist()
    upper_bounds = k_bounds.iloc[:5, 0].tolist()

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

    axes.set_title(biomass, fontweight='bold')
    axes.set_ylabel("CF $(kg_{CO_{2}\_eq}/t_{DM})$", fontsize=12)
    if biomass != "SRC Willow": axes.set_xticklabels(country_list, rotation=0)
    else: axes.set_xticklabels(country_list_SRCW, rotation=0)


arr = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*arr)]
fig.legend(lines[:12], labels[:12], loc='upper right', fontsize='medium')

plt.show()