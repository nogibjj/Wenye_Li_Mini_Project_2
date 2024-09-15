from main import (
    general_describe,
    plot_price_histogram,
    plot_number_of_reviews_histogram,
    plot_price_vs_reviews,
)

import pandas as pd

airbnb_df = pd.read_csv("listings.csv")


def test_general_describe():
    output = general_describe(airbnb_df)
    assert output is not None


def test_plot_price_histogram():
    output = plot_price_histogram(airbnb_df)


def test_plot_number_of_reviews_histogram():
    output = plot_number_of_reviews_histogram(airbnb_df)


def test_plot_price_vs_reviews():
    output = plot_price_vs_reviews(airbnb_df)


if __name__ == "__main__":
    test_general_describe()
