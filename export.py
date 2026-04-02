# export.py — Generates daily index report as CSV

import pandas as pd
from datetime import date
from index_calculator import build_dataframe, calculate_index_level, apply_split
from data import stocks, split_event

def export_report():
    today = date.today().strftime("%Y-%m-%d")

    # Before split
    df_before, cap_before = build_dataframe(stocks)
    index_before = calculate_index_level(cap_before)
    df_before["event"]       = "None"
    df_before["index_level"] = index_before
    df_before["snapshot"]    = "Before Split"

    # After split
    updated_stocks = apply_split(stocks, split_event)
    df_after, cap_after = build_dataframe(updated_stocks)
    index_after = calculate_index_level(cap_after)
    df_after["event"]       = split_event["description"]
    df_after["index_level"] = index_after
    df_after["snapshot"]    = "After Split"

    # Combine both snapshots into one report
    report = pd.concat([df_before, df_after], ignore_index=True)
    report["date"] = today
    report["weight_%"] = report["weight_%"].astype(str) + "%"

    # Save to CSV
    filename = f"index_report_{today}.csv"
    report.to_csv(filename, index=False)

    print(f"\n  Report saved: {filename}")
    print(f"  Rows exported: {len(report)}")
    print(f"\n  Preview:")
    print(report[["date","snapshot","symbol","price","shares","market_cap","weight_%","index_level"]].to_string(index=False))

if __name__ == "__main__":
    export_report()