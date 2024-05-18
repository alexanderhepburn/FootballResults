import matplotlib.pyplot as plt
import pandas as pd


class Plot:
    def create_bar(self, x1: list, x2: list, y1: pd.Index, y2: pd.Index, yAll: pd.Index, x1_name: str, x2_name: str,
                   plot_number: int,
                   title: str):
        plt.figure(figsize=(10, 6))
        # Width of a bar
        width = 0.4

        plt.bar(y1 - (width / 2), x1, width=width, color='skyblue',
                label=x1_name)
        plt.bar(y2 + (width / 2), x2, width=width, color='purple',
                label=x2_name)
        plt.legend(loc="best")
        plt.title(title)
        plt.xticks(yAll)
        plt.grid(axis='y', alpha=0.7)

        plt.savefig(f'tmp/plot{plot_number}.png')
