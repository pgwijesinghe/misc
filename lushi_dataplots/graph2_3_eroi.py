"""GRAPHS 2 & 3: EROI"""

import pandas as pd
import matplotlib.pyplot as plt

datafile = ".\Results.xlsx"
df_26 = pd.read_excel(datafile, 'EROI_26')
df_38 = pd.read_excel(datafile, 'EROI_38')

# df, yran = df_26, [0,7]
df, yran = df_38, [0,10]

fig, ax = plt.subplots(nrows=5, ncols=1, gridspec_kw={'wspace': 0.3, 'hspace': 0.6})

biomass_list = ["Switchgrass", "Miscanthus", "Wheat Straw", "SRC Willow", "Forest Residue"]
country_list = ["USA", "EU", "India ", "Brazil", "UK"]
country_list_SRCW = ["USA", "EU", "UK"]
country_list_FR = ["USA", "UK"]

row,col = 0,0  # row index of the grid
for biomass in biomass_list:  # loops through each biomass entry (main outer loop)
    axes = ax[row]
    axes.hlines(1, -3,5, color='black', ls='dashed')  # eroi = 1 line
    axes.set_ylim(yran)
    i = df.index[df["Biomass type"] == biomass].tolist()[0]
    a,b,c,d,lb1,lb2,lb3,ub1,ub2,ub3 = [],[],[],[],[],[],[],[],[],[]
    if biomass != "SRC Willow" and biomass != "Forest Residue":
        for country in country_list:
            j = [int(x) for x in df.index[df["Country"] == country].tolist() if i <= x <= i+14][0]
            k = df.iloc[j:j+3, 1:6]
            a.append(k.iloc[0,2])
            b.append(k.iloc[1,2])
            c.append(k.iloc[2,2])
            d.append(country)
            lb1.append(k.iloc[0,4])
            lb2.append(k.iloc[1,4])
            lb3.append(k.iloc[2,4])
            ub1.append(k.iloc[0,3])
            ub2.append(k.iloc[1,3])
            ub3.append(k.iloc[2,3])
            
    elif biomass == "SRC Willow":
        for country in country_list_SRCW:
            j = [int(x) for x in df.index[df["Country"] == country].tolist() if i <= x <= i+8][0]
            k = df.iloc[j:j+3, 1:6]
            a.append(k.iloc[0,2])
            b.append(k.iloc[1,2])
            c.append(k.iloc[2,2])
            d.append(country)
            lb1.append(k.iloc[0,4])
            lb2.append(k.iloc[1,4])
            lb3.append(k.iloc[2,4])
            ub1.append(k.iloc[0,3])
            ub2.append(k.iloc[1,3])
            ub3.append(k.iloc[2,3])

    elif biomass == "Forest Residue":
        for country in country_list_FR:
            j = [int(x) for x in df.index[df["Country"] == country].tolist() if i <= x <= i+5][0]
            k = df.iloc[j:j+3, 1:6]
            a.append(k.iloc[0,2])
            b.append(k.iloc[1,2])
            c.append(k.iloc[2,2])
            d.append(country)
            lb1.append(k.iloc[0,4])
            lb2.append(k.iloc[1,4])
            lb3.append(k.iloc[2,4])
            ub1.append(k.iloc[0,3])
            ub2.append(k.iloc[1,3])
            ub3.append(k.iloc[2,3])
            
    kk = pd.DataFrame({'EROIpe_eq': a, "EROIel_eq": b, "EROIel": c},index=d)
    if biomass != "SRC Willow" and biomass != "Forest Residue":
        kk.plot.bar(ax=axes, rot=0, legend=None, fontsize='large')
        for i in range(5):
            axes.vlines(i-0.17, lb1[i], ub1[i])
            axes.vlines(i, lb2[i], ub2[i])
            axes.vlines(i+0.17, lb3[i], ub3[i])
    elif biomass == "SRC Willow":
        kk.plot.bar(ax=axes, rot=0, legend=None, fontsize='large', width=0.3)
        for i in range(3):
            axes.vlines(i-0.095, lb1[i], ub1[i])
            axes.vlines(i, lb2[i], ub2[i])
            axes.vlines(i+0.095, lb3[i], ub3[i])
    elif biomass == "Forest Residue":
        kk.plot.bar(ax=axes, rot=0, legend=None, fontsize='large', width=0.2)
        for i in range(2):
            axes.vlines(i-0.065, lb1[i], ub1[i])
            axes.vlines(i, lb2[i], ub2[i])
            axes.vlines(i+0.065, lb3[i], ub3[i])

    axes.set_title(biomass, fontweight='bold')
    axes.set_ylabel("EROI", fontsize=12)
    row += 1

arr = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*arr)]
fig.legend(lines[:3], labels[:3], loc='upper right', fontsize='large')

plt.show()
