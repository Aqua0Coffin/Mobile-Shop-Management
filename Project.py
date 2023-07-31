import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

INVENTORY_FILE = r"C:\Inventory Data.csv"
SALES_FILE = r"C:\Sales Data.csv"

def main_menu():
    print("Welcome to the Mobile Shop Management System!")
    print("Please select an option:")
    print("1. View inventory")
    print("2. Add new product to inventory")
    print("3. Update product information")
    print("4. Delete product from inventory")
    print("5. View sales history")
    print("6. Generate sales report")
    print("7. View sales by product")
    print("8. View sales by date")
    print("9. View sales by customer")
   # print("10. View sales by employee")
    print("11. Generate bar chart of sales by product")
    print("12. Generate pie chart of sales by customer")
    print("13. Generate line graph of sales by date")
    #print("14. Generate scatter plot of sales by employee")
    print("15. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_inventory()
    elif choice == "2":
        add_product()
    elif choice == "3":
        update_product()
    elif choice == "4":
        delete_product()
    elif choice == "5":
        view_sales_history()
    elif choice == "6":
        generate_sales_report()
    elif choice == "7":
        view_sales_by_product()
    elif choice == "8":
        view_sales_by_date()
    elif choice == "9":
        view_sales_by_customer()
    elif choice == "10":
        view_sales_by_employee()
    elif choice == "11":
        generate_sales_bar_chart()
    elif choice == "12":
        generate_sales_pie_chart()
    elif choice == "13":
        generate_sales_line_graph()
    elif choice == "14":
        generate_sales_scatter_plot()
    elif choice == "15":
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def view_inventory():
    inventory_data = pd.read_csv(INVENTORY_FILE)
    print(inventory_data)

def add_product():
    inventory_data = pd.read_csv(INVENTORY_FILE)
    product_id = input("Enter product ID: ")
    product_name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = input("Enter product price: ")
    quantity = input("Enter product quantity: ")
    new_product = pd.DataFrame({
        "Product ID": [product_id],
        "Product Name": [product_name],
        "Description": [description],
        "Price": [price],
        "Quantity": [quantity]
    })
    inventory_data = pd.concat([inventory_data, new_product], ignore_index=True)
    inventory_data.to_csv(INVENTORY_FILE, index=False)
    print("Product added successfully.")

def update_product():
    inventory_data = pd.read_csv(INVENTORY_FILE)
    product_id = input("Enter product ID to update: ")
    product = inventory_data.loc[inventory_data["Product ID"] == product_id]
    product_id = input("Enter product ID to update: ")
    product = inventory_data.query("Product ID == @product_id")
    if product.empty:
        print("Product not found.")
        return
    print("Current product information:")
    print(product)
    new_product_name = input("Enter new product name (leave blank to keep current value): ")
    new_description = input("Enter new product description (leave blank to keep current value): ")
    new_price = input("Enter new product price (leave blank to keep current value): ")
    new_quantity = input("Enter new product quantity (leave blank to keep current value): ")
    if new_product_name != "":
        inventory_data.loc[inventory_data["Product ID"] == product_id, "Product Name"] = new_product_name
    if new_description != "":
        inventory_data.loc[inventory_data["Product ID"] == product_id, "Description"] = new_description
    if new_price != "":
        inventory_data.loc[inventory_data["Product ID"] == product_id, "Price"] = new_price
    if new_quantity != "":
        inventory_data.loc[inventory_data["Product ID"] == product_id, "Quantity"] = new_quantity
    inventory_data.to_csv(INVENTORY_FILE, index=False)
    print("Product updated successfully.")

def delete_product():
    inventory_data = pd.read_csv(INVENTORY_FILE)
    product_id = input("Enter product ID to delete: ")
    inventory_data = inventory_data[inventory_data["Product ID"] != product_id]
    inventory_data.to_csv(INVENTORY_FILE, index=False)
    print("Product deleted successfully.")

def view_sales_history():
    sales_data = pd.read_csv(SALES_FILE)
    print(sales_data)

def generate_sales_report():
    sales_data = pd.read_csv(SALES_FILE)
    report_data = sales_data.groupby(["Product ID", "Date"]).agg({
        "Quantity": "sum",
        "Price": "mean"
    })
    report_data.to_csv("Sales Report.csv")
    print("Sales report generated successfully.")

def view_sales_by_product():
    sales_data = pd.read_csv(SALES_FILE)
    inventory_data = pd.read_csv(INVENTORY_FILE)
    sales_by_product = sales_data.groupby("Product ID").agg({
        "Quantity": "sum",
        "Price": "mean"
    })
    sales_by_product_with_name = pd.merge(sales_by_product, inventory_data[["Product ID", "Product Name"]], on="Product ID")
    sales_by_product_with_name["Profit"] = sales_by_product_with_name["Quantity"] * sales_by_product_with_name["Price"]
    sales_by_product_with_name = sales_by_product_with_name[["Product Name", "Quantity", "Profit"]]
    print(sales_by_product_with_name)

def view_sales_by_date():
    sales_data = pd.read_csv(SALES_FILE)
    sales_by_date = sales_data.groupby("Date")["Quantity"].sum()
    print(sales_by_date)

def view_sales_by_customer():
    sales_data = pd.read_csv(SALES_FILE)
    sales_by_customer = sales_data.groupby("Customer Name")["Quantity"].sum()
    print(sales_by_customer)

#def view_sales_by_employee():
#    sales_data = pd.read_csv(SALES_FILE)
#    sales_by_employee = sales_data.groupby("Employee Name")["Quantity"].sum()
#    print(sales_by_employee)

def generate_sales_bar_chart():
    sales_data = pd.read_csv(SALES_FILE)
    inventory_data = pd.read_csv(INVENTORY_FILE)
    sales_by_product = sales_data.groupby("Product ID").agg({
        "Quantity": "sum",
        "Price": "mean"
    })
    sales_by_product_with_name = pd.merge(sales_by_product, inventory_data[["Product ID", "Product Name"]], on="Product ID")
    sales_by_product_with_name.plot(kind="bar", x="Product Name", y="Quantity")
    plt.title("Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.show()

def generate_sales_pie_chart():
    sales_data = pd.read_csv(SALES_FILE)
    sales_by_customer = sales_data.groupby("Customer Name")["Quantity"].sum()
    sales_by_customer.plot(kind="pie")
    plt.title("Sales by Customer")
    plt.ylabel("")
    plt.show()

def generate_sales_line_graph():
    sales_data = pd.read_csv(SALES_FILE)
    sales_by_date = sales_data.groupby("Date")["Quantity"].sum()
    sales_by_date.plot(kind="line")
    plt.title("Sales by Date")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.show()

#def generate_sales_scatter_plot():
#    sales_data = pd.read_csv(SALES_FILE)
#    sales_by_employee = sales_data.groupby("Employee Name").agg({
#        "Quantity": "sum",
#        "Price": "mean"
#    })
#    sales_by_employee.plot(kind="scatter", x="Quantity", y="Price")
#    plt.title("Sales by Employee")
#    plt.xlabel("Quantity")
#    plt.ylabel("Price")
#    plt.show()
#
while True:
    main_menu()