import os

import pandas as pd

INPUT_DIR = "/app/input"


def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".csv"):
            print("==============================")
            print("Analysis for {}".format(filename))
            print("------------------------------")
            analyze_csv(os.path.join(INPUT_DIR, filename))
            print("==============================")


def analyze_csv(file_path):
    # Load CSV
    df = pd.read_csv(file_path, sep=";", encoding="utf-8")

    # Extract month-year for grouping
    df["Buchungstag"] = pd.to_datetime(df["Buchungstag"].astype(str).str.strip(), format="%Y-%m-%d", errors="coerce")
    df["Month"] = df["Buchungstag"].dt.to_period("M")

    # Overall balance overview
    print("\n💰 Average end-of-month account balance:")
    end_of_month_balances = df.sort_values("Buchungstag").groupby("Month")["Saldo nach Buchung"].last()
    print(f"{end_of_month_balances.mean():.2f}")

    # Top 5 vendors by total spend
    print("\n🏆 Top 10 vendors by total spend:")
    top_vendors = df.groupby("Name Zahlungsbeteiligter")["Betrag"].sum().reindex(
        df.groupby("Name Zahlungsbeteiligter")["Betrag"].sum().abs().sort_values(ascending=False).index
    ).head(10)
    print(top_vendors)

    # Monthly cash flow overview
    print("\n📈 Monthly cash flow overview:")
    monthly_flow = df.groupby("Month")["Betrag"].agg([
        ("Inflow", lambda x: x[x > 0].sum()),
        ("Outflow", lambda x: x[x < 0].sum())
    ])
    monthly_flow["Difference"] = monthly_flow["Outflow"] + monthly_flow["Inflow"]
    print(monthly_flow)

    # Transactions without a category
    no_category = df[df["Category"].isna() | (df["Category"].str.strip() == "")]
    print(f"\n⚠️ Transactions without category: {len(no_category)}")
    no_category = no_category.reindex(no_category["Betrag"].abs().sort_values(ascending=False).index).head(25)
    print("\n⚠️ Top 25 transactions without a category:")
    print(no_category[["Name Zahlungsbeteiligter", "Verwendungszweck", "Betrag"]])

    print("------------------------------")

    # List of all categories
    categories = [
        "Lebensmittel", "Drogerie", "Tanken", "Bargeldabholung", "Mieteinnahme", "Versicherung",
        "Gas", "Studium", "Telekommunikation", "Streaming", "Auto", "Strom", "Kindergeld",
        "Medikamente", "Hauskredit", "Gehalt", "Essen gehen", "eBay", "Wasser", "Freizeit",
        "Bank", "Schreibwaren und Porto", "Clara", "Amazon", "Kleidung/Schuhe", "Baumarkt",
        "Rundfunkgebühr", "Nebenkosten Haus", "Möbel", "Urlaub", "Elterngeld"
    ]

    print("\n📊 Category-wise summary:\n")
    for cat in categories:
        cat_df = df[df["Category"] == cat]
        if cat_df.empty:
            continue
        total = cat_df["Betrag"].sum()
        avg_monthly = cat_df.groupby("Month")["Betrag"].sum().mean()
        max_tx = cat_df["Betrag"].abs().max()
        count_tx = len(cat_df)
        print(f"Category: {cat}")
        print(f"  Total spent: {total:.2f}")
        print(f"  Average monthly spend: {avg_monthly:.2f}")
        print(f"  Largest transaction (absolute): {max_tx:.2f}")
        print(f"  Number of transactions: {count_tx}\n")


if __name__ == "__main__":
    main()
