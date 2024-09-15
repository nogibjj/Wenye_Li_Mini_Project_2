import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport

airbnb_df = pd.read_csv("listings.csv")


def general_describe(df):
    airbnb_summary = df[
        [
            "price",
            "minimum_nights",
            "number_of_reviews",
            "reviews_per_month",
            "availability_365",
        ]
    ].describe()
    print(airbnb_summary)
    return airbnb_summary


# Function to plot histogram for price
def plot_price_histogram(df):
    # Filter out extreme outliers
    df_filtered = df[df["price"] <= 2000]
    plt.hist(df_filtered["price"], bins=30, color="skyblue", edgecolor="black")
    plt.title("Price Distribution of NYC Airbnb Listings", fontsize=16)
    plt.xlabel("Price (in USD)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()


# Function to plot histogram for number of reviews
def plot_number_of_reviews_histogram(df):
    # Filter out extreme outliers
    df_filtered = df[df["number_of_reviews"] <= 1000]
    plt.hist(
        df_filtered["number_of_reviews"], bins=30, color="lightgreen", edgecolor="black"
    )
    plt.title("Number of Reviews Distribution", fontsize=16)
    plt.xlabel("Number of Reviews")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()


# Function to plot the relationship between price and number of reviews
def plot_price_vs_reviews(df):
    # Filter out extreme outliers
    df_filtered = df[(df["number_of_reviews"] <= 1000) & (df["price"] <= 2000)]
    plt.scatter(
        df_filtered["price"], df_filtered["number_of_reviews"], alpha=0.5, color="green"
    )
    plt.title("Price vs Number of Reviews", fontsize=16)
    plt.xlabel("Price (in USD)")
    plt.ylabel("Number of Reviews")
    plt.grid(True)
    plt.show()


def generate_profile(df):
    # Generate html report of dataset
    profile = ProfileReport(df, title="NYC Airbnb Data Profiling Report")
    profile.to_file("airbnb_profile.html")