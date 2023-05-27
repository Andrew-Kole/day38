import pandas as pd
import plotly.express as px


def build_graph(path="files/data.txt"):
    frame = pd.read_csv("files/data.txt")
    dates = frame["date"]
    temperatures = frame["temperature"]
    figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperatures(C)"})
    return figure


if __name__ == "__main__":
    print(build_graph())
