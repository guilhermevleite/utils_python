import numpy as NP
import seaborn as SNS
import pandas as PD
import matplotlib.pyplot as PLT


df = PD.read_csv('./caca.csv')
new_df = []

for idx, row in df.iterrows():
    n_row = row.tolist()
    cp_row = []

    total = n_row[0] + n_row[1] + n_row[2] + n_row[3]

    n_row[3] = (n_row[3] * 100) / total
    n_row[2] = (n_row[2] * 100) / total
    n_row[1] = (n_row[1] * 100) / total
    n_row[0] = (n_row[0] * 100) / total

    # print('0\t', 100 - n_row[3] - n_row[2] - n_row[1])
    # cp_row.append(100 - n_row[3] - n_row[2] - n_row[1])
    print('row\t', n_row[0], n_row[1], n_row[2], n_row[3], n_row[4])
    print('3\t', 100)
    cp_row.append(100)
    print('2\t', 100 - n_row[0])
    cp_row.append(100 - n_row[0])
    print('1\t', 100 -  n_row[0] - n_row[1])
    cp_row.append(100 - n_row[0] - n_row[1])

    print('4\t', n_row[3])
    cp_row.append(n_row[3])
    cp_row.append(n_row[4])
    # if (n_row[0] > n_row[1]):
    #     n_row[1] += n_row[0]
    #
    # if (n_row[1] > n_row[2]):
    #     n_row[2] += n_row[1]

    new_df.append(cp_row)

dfo = PD.DataFrame(new_df, columns=df.columns)

# print(df)
# print(dfo)

# SNS.set_context("poster")
SNS.set_style("white")
#SNS.set_theme()

f, ax = PLT.subplots(figsize=(24,16))
SNS.set_color_codes("deep")

SNS.barplot(x="experiment", y="SS", data=dfo, label="SS", color="g")

SNS.barplot(x="experiment", y="SC", data=dfo, label="SC", color="orange")

SNS.barplot(x="experiment", y="MS", data=dfo, label="MS", color="b")

SNS.barplot(x="experiment", y="MC", data=dfo, label="MC", color="r")

ax.legend(ncol=1, loc="upper right", frameon=False)

ax.set(xlim=(-0.5, 6),
       ylabel="% Organoids",
       xlabel="[ ] Irradiated Riboflavin")

PLT.title("Bile Acids")

SNS.despine(left=True, bottom=True)

# PLT.tight_layout()
PLT.show()
