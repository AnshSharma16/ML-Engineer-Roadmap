%%writefile src/validate_data.py

import sys
import os
sys.path.append(os.path.dirname(__file__))

import pandas as pd
from validation_schema import sales_schema

df = pd.read_csv("data/sample.csv")

sales_schema.validate(df)
print("✅ Data validation passed") 
