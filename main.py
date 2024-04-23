import os
import sys
from typing import List

import pandas as pd
import plotly.express as px
import pypistats
from pyaction import io


def main(args: List[str]) -> None:
    """main function

    Args:
        args: STDIN arguments
    """

    package_name = io.read("package")
    dimension = io.read("dimensions")
    theme = io.read("theme")
    title = io.read("title")
    output_file = io.read("output")

    directory_path = os.path.dirname(output_file)

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    width, height = list(map(int, dimension.split("x")))

    pd.options.plotting.backend = "plotly"
    df = pypistats.overall(package=package_name, total=True, format="pandas")
    data = df.groupby("category").get_group("without_mirrors").sort_values("date")

    fig = px.line(
        data,
        x="date",
        y="downloads",
        width=width,
        height=height,
        title=title,
    )

    fig.update_layout(
        xaxis_title="Dates",
        yaxis_title="Downloads",
        template=theme,
        margin_b=80,
        margin_l=95,
    )

    fig.write_image(output_file)


if __name__ == "__main__":
    main(sys.argv[1:])
