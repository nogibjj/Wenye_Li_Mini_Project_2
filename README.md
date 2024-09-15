[![CI](https://github.com/nogibjj/Wenye_Li_Mini_Project_2/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Wenye_Li_Mini_Project_2/actions/workflows/cicd.yml)

This repo contains work for mini-project 2. It sets up an environment on codespaces and uses Github Actions to run a Makefile for the following: `make install`, `make format`, `make lint`, and `make test`.

Requirements are as follow:

- Python script using Pandas for descriptive statistics
- Read a dataset (CSV or Excel)
- Generate summary statistics (mean, median, standard deviation)
- Create at least one data visualization
- In addition, I include a generateed pdf of the datasets I chose using ydata-profiling.

## Format, lint, and test codes

1. Format code by using `make format` command
2. Lint code by using `make lint` command
   ![Format and Lint Image](Format_Lint.png)
3. Test code by using `make test` command
   ![Test Image](Test.png)

## Visualizations

Visualizations can be ran by using `python test_main.py`.

![Vis Image 1](Figure_1.png)
![Vis Image 2](Figure_2.png)
![Vis Image 3](Figure_3.png)

## Summary statistics of dataset

Summary reports can be generated using `python test_main.py`.

![Stats Image 3](stats.png)
