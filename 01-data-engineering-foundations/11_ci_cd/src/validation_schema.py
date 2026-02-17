import pandera as pa
from pandera import Column, Check

sales_schema = pa.DataFrameSchema({
    "Units Sold": Column(int, Check.ge(0)),
    "Unit Price": Column(float, Check.ge(0)),
    "Sales Channel": Column(str, Check.isin(["Online", "Offline"]))
})
