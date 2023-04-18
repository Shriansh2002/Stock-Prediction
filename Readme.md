# Stock Prediction App

This repository contains a Python script to predict the closing price of Apple stock using **Linear Regression**. The script uses data from a CSV file `AAPL.csv` to train a linear regression model and then predicts the closing price for the test data.

## Table of Contents

-   [Prerequisites](#prerequisites)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Contributing](#contributing)
-   [License](#license)

## Prerequisites

-   Python 3.x
-   Pandas
-   NumPy
-   Matplotlib
-   Scikit-learn

## Installation

1. Clone this repository to your local machine using

    ```bash
    git clone https://github.com/Shriansh2002/Stock-Prediction.git
    ```

2. Install the required packages using

    ```bash
    pip install -r requirements.txt
    ```

## Usage

-   Put your `AAPL.csv` file in the same directory as the script.
-   Run the script using `python apple_stock_prediction.py.`
-   The script will train a linear regression model on the training data and predict the - closing price for the test data.
-   The root mean squared error (RMSE) of the prediction will be displayed on the console.
-   A plot will also be displayed showing the predicted closing prices and the actual closing prices.

## Contributing

-   Fork this repository to your own GitHub account and then clone it to your local device.
-   Create a new branch:
    ```bash
    git checkout -b my-new-feature
    ```
-   Make changes and test them.
-   Submit a pull request detailing the changes made and any additional information about the feature.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
