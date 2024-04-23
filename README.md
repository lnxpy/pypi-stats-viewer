## PyPI Stats Viewer <img alt="action-badge" src="https://img.shields.io/badge/PyPI Stats Viewer-white?logo=github-actions&label=GitHub%20Action&labelColor=white&color=0064D7"> <a href="https://github.com/lnxpy/pyaction"><img alt="pyaction" src="https://img.shields.io/badge/PyAction-white?label=Made%20with&labelColor=white&color=0064D7"></a>

This action generates a chart out of the rates of your PyPI Python packages. You can save the output and show it in the README file in various forms.

### Usage
```yml
name: Stats Chart Updater

on:
  schedule:
    - cron: '0 0 1 * *' # runs every month

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4
        
      - uses: lnxpy/pypi-stats-viewer@v1
        with:
          package: <package-name>
          dimensions: <size>
          theme: <theme>
          title: <bar-title>
          output: <path-to-file>

      - uses: EndBug/add-and-commit@v9
        with:
          default_author: github_actions
          message: chart is updated
```

### Inputs

| Input 	| Description 	| Required 	| Default 	| Choices 	|
|---	|---	|---	|---	|---	|
| `package` 	| package name 	| yes 	| - 	| (`str`) 	|
| `dimensions` 	| image size 	| no 	| `1200x400` 	| (`height` and `weight`) in form of `1234x5678` 	|
| `theme` 	| chart theme 	| no 	| `plotly_white` 	| (`ggplot2`, `seaborn`, `simple_white`, `plotly`, `plotly_white`, `plotly_dark`, `presentation`, `xgridoff`, `ygridoff`, `gridon`, `none`) 	|
| `title` 	| chart title 	| no 	| `PyPI Package Stats` 	| (`str`) 	|
| `output` 	| path to output 	| no 	| `assets/stats.svg` 	| (`str`) 	|

### License
This action is licensed under some specific terms. Check [here](LICENSE) for more information.