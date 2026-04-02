# data.py — Our stock data (simulated market data)

stocks = [
    {"symbol": "RELIANCE", "company": "Reliance Industries",     "price": 2850.00, "shares": 500},
    {"symbol": "TCS",      "company": "Tata Consultancy Svcs",   "price": 3920.00, "shares": 300},
    {"symbol": "HDFCBANK", "company": "HDFC Bank",               "price": 1640.00, "shares": 700},
    {"symbol": "INFY",     "company": "Infosys",                 "price": 1480.00, "shares": 400},
    {"symbol": "ITC",      "company": "ITC Limited",             "price":  450.00, "shares": 900},
]

# A corporate event: RELIANCE did a 2-for-1 stock split
# This means: shares double, price halves
split_event = {
    "symbol": "RELIANCE",
    "split_ratio": 2,   # 2 new shares for every 1 old share
    "description": "Reliance 2-for-1 stock split"
}