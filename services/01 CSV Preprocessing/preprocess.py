import os
import pandas as pd

# INPUT_DIR = "/app/input"
# OUTPUT_DIR = "/app/output"
INPUT_DIR = "../../data/input"
OUTPUT_DIR = "../../data/processed/01-csv-preprocessing"
MAPPINGS_DIR = "../../mappings/"  # Keep trailing "/" for appending file name.

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Columns to keep
COLUMNS = [
    "Buchungstag",
    "Name Zahlungsbeteiligter",
    "Buchungstext",
    "Verwendungszweck",
    "Betrag",
    "Saldo nach Buchung",
    "Mandatsreferenz",
    "Waehrung"
]


def process_csv(file_path):
    try:
        df = pd.read_csv(file_path, sep=";", encoding="utf-8")

        # Check for required columns
        if "Buchungstag" not in df.columns:
            print(f"Skipping {file_path}: Missing column 'Buchungstag'")
            return

        # Keep only desired columns
        existing_cols = [col for col in COLUMNS if col in df.columns]
        df = df[existing_cols]

        # Convert date format (DD.MM.YYYY → YYYY-MM-DD)
        df["Buchungstag"] = pd.to_datetime(df["Buchungstag"], format="%d.%m.%Y", errors="coerce").dt.strftime(
            "%Y-%m-%d")

        # Add empty "Category" column
        df["Category"] = None

        # 1) Apply mapping from reference-text.config.csv
        ref_map = pd.read_csv(MAPPINGS_DIR + "reference-text.config.csv", sep=";", encoding="utf-8")
        for _, row in ref_map.iterrows():
            match_str = str(row["Verwendungszweck"]).strip()
            category = str(row["Category"]).strip()
            mask = df["Verwendungszweck"].astype(str).str.contains(match_str, case=False, na=False, regex=False)
            df.loc[mask, "Category"] = category

        # 2) Apply mapping from payment-party.config.csv (overrides previous)
        party_map = pd.read_csv(MAPPINGS_DIR + "payment-party.config.csv", sep=";", encoding="utf-8")
        for _, row in party_map.iterrows():
            match_str = str(row["Name Zahlungsbeteiligter"]).strip()
            category = str(row["Category"]).strip()
            mask = df["Name Zahlungsbeteiligter"].astype(str).str.contains(match_str, case=False, na=False, regex=False)
            df.loc[mask, "Category"] = category

        # Save output CSV
        output_path = os.path.join(OUTPUT_DIR, os.path.basename(file_path))
        df.to_csv(output_path, index=False, sep=";", encoding="utf-8")
        print(f"Processed: {file_path} → {output_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".csv"):
            process_csv(os.path.join(INPUT_DIR, filename))


if __name__ == "__main__":
    main()
