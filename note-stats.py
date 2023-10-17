import matplotlib.pyplot as plt

import modules.input as input
from modules.create_dataframe import create_df
import modules.generate_outputs as output


arguments = input.parse_arguments()

df = create_df(arguments.folder_path)


next = ''
while next != 'q':

    if arguments.date:
        output.show_date(df)

    if arguments.month:
        output.show_month(df)

    if arguments.hist:
        output.show_hist(df)

    if arguments.size:
        output.show_size(df)

    if arguments.heatmap:
        output.show_heatmap(df)

    plt.show()

    #print(df.info(memory_usage='deep'))

    next = input.select_next_visualization()
    arguments = input.update_args(arguments, next)

