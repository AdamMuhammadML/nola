import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(
    "data/raw/HI-Small_Trans.csv",
    usecols=[
    "Is Laundering",
    "Payment Format",
    "Amount Paid",
    "Payment Currency"
]
)

class_counts = df["Is Laundering"].value_counts().sort_index()

class_counts.plot(kind="bar")

plt.title("Class Distribution")
plt.xlabel("Is Laundering")
plt.ylabel("Number of Transactions")

plt.tight_layout()
plt.savefig("figures/class_balance.png")

plt.close()

payment_counts = df["Payment Format"].value_counts()

payment_counts.plot(kind="bar")

plt.title("Transactions by Payment Format")
plt.xlabel("Payment Format")
plt.ylabel("Number of Transactions")

plt.tight_layout()
plt.savefig("figures/payment_formats.png")

plt.close()

usd_transactions = df[df["Payment Currency"] == "US Dollar"]

log_amounts = np.log10(usd_transactions["Amount Paid"])

log_amounts.plot(
    kind="hist",
    bins=50
)

plt.title("Distribution of US Dollar Amounts Paid")
plt.xlabel("log10(Amount Paid)")
plt.ylabel("Number of Transactions")

plt.tight_layout()
plt.savefig("figures/amount_paid_distribution.png")