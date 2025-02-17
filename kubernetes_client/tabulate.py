from tabulate import tabulate

data = [["Alpha", 10, 3.14159], ["Beta", 2000, 2.71828], ["Gamma", 300, 1.41421]]

headers = ["Name", "Count", "Value"]

print("=== Default ===")
print(tabulate(data, headers=headers))

print("\n=== Fancy Grid, Right Align Numbers, 2 Decimal ===")
print(
    tabulate(
        data, headers=headers, tablefmt="fancy_grid", numalign="right", floatfmt=".2f"
    )
)

print("\n=== HTML Table ===")
print(tabulate(data, headers=headers, tablefmt="html"))
