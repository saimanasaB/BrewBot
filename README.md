# Coffee Machine Project

This is a simple coffee machine simulator written in Python. Users can select different types of coffee, and the machine will handle resources like water, milk, and coffee beans. It also processes payments and returns change if needed.

## Files

- `coffee_machine.py`: The main script that runs the coffee machine.
- `coffee_machine_data.py`: Contains data for the coffee machine, such as menu options and initial resources.

## How to Run

1. Make sure you have Python installed on your system.
2. Clone the repository or download the files.
3. Open a terminal and navigate to the project directory.
4. Run the following command to start the coffee machine:

```sh
python coffee_machine.py


USAGE:
The machine will prompt you to choose a drink or perform other actions.
Type espresso, latte, or cappuccino to select a drink.
Type report to see the current resources and money.
Type off to turn off the machine.
Follow the prompts to insert coins for your selected drink.


FEATURES:
Checks for sufficient resources before making a drink.
Processes coin input and calculates if the transaction is successful.
Provides change if more money is inserted than required.
Deducts resources when a drink is made and updates the report.



This project simulates a coffee machine's functionality, including resource management, payment processing, and making coffee. It can be further expanded with additional features like more drink options, better error handling, and user interfaces
