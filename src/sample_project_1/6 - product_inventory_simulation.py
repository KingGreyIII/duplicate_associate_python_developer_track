inventory = {
    "P001": [25.99, "Bread"],
    "P002": [15.50, "NoteBook"],
    "P003": [8.75, "Pen"],
    "P004": [30.00, "Fish"],
    "P005": [5.00, "Pencil"],
}

stock = {
    "P001": 12,
    "P002": 5,
    "P003": 6,
    "P004": 9,
    "P005": 18,
}
"""📝 Task Summary

Merge inventory and stock into a single dictionary.

Write a function process_product(pid, products) that:

categorises products by price (Expensive, Moderate, Cheap).

simulates sales by decreasing stock until it reaches 0.

Loop over all products and run the function.

(Bonus) Allow the user to input a product ID (P001, P002, etc.) to process just that product.

💡 Hints

Use a dictionary comprehension to merge inventory and stock.

Inside the function, access fields like product["price"], product["name"], product["stock"].

In the while loop, reduce stock by 1 until it reaches 0.

Remember to return or update stock inside the dictionary, so it doesn’t reset each time.

To check just one product, use an input() and pass the result into your function."""