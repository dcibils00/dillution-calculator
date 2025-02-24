# Equity and Dilution Calculator

This is a simple web-based equity and dilution calculator built using Streamlit in Python. It helps founders and investors quickly understand the impact of investments on ownership percentages.

## Features

* Calculates post-money ownership percentages for founders and investors.
* Determines the dilution each founder experiences.
* Displays a cap table showing pre- and post-investment ownership.
* Handles multiple founders with individual ownership percentages.
* Includes error handling to prevent invalid inputs (e.g., post-money valuation less than pre-money + investment).
* User-friendly interface built with Streamlit.

## How to Use

  **Run the app:**
    ```bash
    pip install streamlit
    streamlit run equity_calculator.py
    ```

Open your web browser to the address displayed by Streamlit (usually `http://localhost:8501`).

## Input Fields

*   **Pre-money Valuation:** The company's value *before* the investment.
*   **Investment Amount:** The amount of money being invested.
*   **Post-money Valuation:** The company's value *after* the investment.
*   **Number of Founders:** The number of founders in the company.
*   **Founder Name:** The name of each founder.
*   **Founder Ownership (%):** The percentage of ownership each founder holds *before* the investment.

## Output

The calculator displays the following results:

*   Investor Ownership Percentage
*   New Ownership Percentage for each Founder
*   Dilution for each Founder
*   Pre-money Valuation
*   Investment Amount
*   Post-money Valuation
*   Cap Table

## Example

Let's say a company has a pre-money valuation of $5 million, receives a $3 million investment, and has a post-money valuation of $15 million.  Founder 1 owns 40%, Founder 2 owns 20%, Founder 3 owns 20%, and Founder 4 owns 10%.

The calculator will show that the investors own 20%, Founder 1 ownership is diluted to 32%, Founder 2 to 16%, Founder 3 to 16%, and Founder 4 to 8%.

## Requirements

*   Python 3.x
*   Streamlit

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

MIT

## Contact

Diego Cibils
