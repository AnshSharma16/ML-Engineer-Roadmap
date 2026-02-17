import pandas as pd
from validation_schema import sales_schema

def run_validation():
    df = pd.read_csv("data/sample.csv")
    sales_schema.validate(df)
    print("✅ Data validation passed")

if __name__ == "__main__":
    run_validation()
