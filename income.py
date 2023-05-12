import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from flask import Flask
from flask import send_file

app = Flask(__name__)

# prevent matplotlib from opening a gui
plt.ioff()
mpl.use('Agg')

data_source = []
header_line = []


@app.route('/')
def hello_world():

    raw_data_source = []
    new_line = []
    counter = 0

    with open('income.txt', 'r') as f:
        header_line = next(f).strip('\n')
        header: list = header_line.split(", ")
        for line in f:
            line_data: list = line.strip('\n').split(",")
            for item in line_data:
                print(item)
                new_item = int(item.replace(" ", ""))
                print(new_item)
                new_line.append(new_item)
                print(new_line)
            raw_data_source.append(new_line)
            new_line = []
            counter = counter + 1
        print(counter)
    print(raw_data_source)
    data_source = np.array(raw_data_source).reshape(counter, 4)
    print(data_source)
    print(header_line)
    print(header)

    df = pd.DataFrame(data_source)
    df.columns = [header[0], header[1], header[2], header[3]]
    sns_plot = sns.barplot(palette="ch:.5", data=df, ci=None)  # type: ignore
    sns_plot.figure.savefig("output.png")
    plt.close()
    return send_file('output.png', mimetype='image/png')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
