# index_calculator.py — Calculates index levels and handles corporate events

import pandas as pd
from data import stocks, split_event

def build_dataframe(stock_list):
    df = pd.DataFrame(stock_list)
    df["market_cap"] = df["price"] * df["shares"]
    total_market_cap = df["market_cap"].sum()
    df["weight_%"] = (df["market_cap"] / total_market_cap * 100).round(2)
    return df, total_market_cap

def calculate_index_level(total_market_cap, divisor=1000):
    return round(total_market_cap / divisor, 2)

def apply_split(stock_list, event):
    updated = []
    for stock in stock_list:
        s = stock.copy()
        if s["symbol"] == event["symbol"]:
            s["shares"] = s["shares"] * event["split_ratio"]
            s["price"]  = s["price"]  / event["split_ratio"]
            print(f"\n  EVENT APPLIED: {event['description']}")
            print(f"  {s['symbol']} → New Price: ₹{s['price']:.2f} | New Shares: {s['shares']}")
        updated.append(s)
    return updated

def display_table(df, label):
    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"{'='*60}")
    print(df[["symbol", "company", "price", "shares", "market_cap", "weight_%"]].to_string(index=False))

def run():
    print("\n>>> BEFORE CORPORATE EVENT <<<")
    df_before, cap_before = build_dataframe(stocks)
    display_table(df_before, "Index Constituents — Before Split")
    index_before = calculate_index_level(cap_before)
    print(f"\n  Total Market Cap : ₹{cap_before:,.2f}")
    print(f"  Index Level      : {index_before}")

    print("\n\n>>> APPLYING CORPORATE EVENT <<<")
    updated_stocks = apply_split(stocks, split_event)

    print("\n\n>>> AFTER CORPORATE EVENT <<<")
    df_after, cap_after = build_dataframe(updated_stocks)
    display_table(df_after, "Index Constituents — After Split")
    index_after = calculate_index_level(cap_after)
    print(f"\n  Total Market Cap : ₹{cap_after:,.2f}")
    print(f"  Index Level      : {index_after}")

    print(f"\n  Index Change     : {round(index_after - index_before, 2)}")
    print(f"  (Should be 0.0 — a stock split must NOT change the index level)")

    return df_before, df_after

if __name__ == "__main__":
    run()