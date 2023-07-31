# Mobile Shop Management System Documentation

The Mobile Shop Management System is a Python-based application that allows users to manage inventory and sales data for a mobile shop. The system provides a simple command-line interface that offers various functionalities to perform tasks related to inventory and sales management.

## Features

The Mobile Shop Management System offers the following features:

1. **View Inventory**: Allows users to view the current inventory, displaying product details such as product ID, name, description, price, and quantity.

2. **Add New Product to Inventory**: Enables users to add a new product to the inventory. Users are prompted to input product details, and the new product is appended to the existing inventory data.

3. **Update Product Information**: Allows users to update product information by providing the product ID. Users can modify the product name, description, price, or quantity.

4. **Delete Product from Inventory**: Enables users to remove a product from the inventory based on its product ID.

5. **View Sales History**: Allows users to view the sales history, displaying sales data such as product ID, date, quantity, and price.

6. **Generate Sales Report**: Generates a sales report by grouping sales data by product ID and date, calculating the total quantity sold and average price per product. The report is saved in a CSV file.

7. **View Sales by Product**: Displays the total quantity sold and total profit for each product based on sales data.

8. **View Sales by Date**: Displays the total quantity sold on each date based on sales data.

9. **View Sales by Customer**: Displays the total quantity sold for each customer based on sales data.

10. **Generate Sales Bar Chart**: Generates a bar chart to visualize sales data, displaying the total quantity sold for each product.

11. **Generate Sales Pie Chart**: Generates a pie chart to visualize sales data, displaying the total quantity sold for each customer.

12. **Generate Sales Line Graph**: Generates a line graph to visualize sales data, displaying the total quantity sold on each date.

## Dependencies

The Mobile Shop Management System relies on the following Python libraries:

- pandas: Used for data manipulation, reading/writing CSV files, and data analysis.
- numpy: Required by pandas for numerical operations.
- matplotlib: Used to generate various types of charts for data visualization.

## How to Use

1. Clone the repository to your local machine.
2. Ensure you have Python installed (Python 3.6 or higher is recommended).
3. Install the required dependencies by running the following command in the terminal:

```
pip install pandas numpy matplotlib
```

4. Run the main script `mobile_shop_management.py` using Python:

```
python mobile_shop_management.py
```

5. The main menu will be displayed, presenting the available options. Enter the desired option number to perform the corresponding task.

## Note

Some functionalities like `view_sales_by_employee()` and `generate_sales_scatter_plot()` are currently commented out, indicating they are either not fully implemented or not relevant for the current use case. If you intend to use those features, uncomment the relevant sections and implement the respective code.

## Contribution

This project is open for contributions. If you find any issues or have ideas for improvements, feel free to create a pull request or submit an issue on the GitHub repository.

## License

This Mobile Shop Management System is released under the MIT License. See the `LICENSE` file for more details.

---

You can copy the above documentation and save it as a `README.md` file in your GitHub repository for the Mobile Shop Management System. Make sure to modify it according to your actual repository structure and requirements.
