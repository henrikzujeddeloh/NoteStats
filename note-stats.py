import matplotlib.pyplot as plt

from modules.parse_arguments import parse_arguments
from modules.create_dataframe import create_df
import modules.generate_outputs as output


args = parse_arguments()

df = create_df(args.folder_path)

if args.date:
    output.show_date(df)

if args.month:
    output.show_month(df)

if args.hist:
    output.show_hist(df)

if args.size:
    output.show_size(df)

if args.heatmap:
    output.show_heatmap(df)

plt.show()

print(df.info(memory_usage='deep'))
