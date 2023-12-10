#!/usr/bin/env python

"""
Consolidate rows in a "supported markets" JSON
"""

# usage: ./consolidate-coverage-data.py -s <path-to-source>

# Merge datatype and markettype

# Transform:
# { "datatype": "OHLCV", "markettype": "spot", "market_venue": "bibox", "symbol": "ada", "base": "usdt" },
# { "datatype": "raw_trades", "markettype": "spot", "market_venue": "bibox", "symbol": "algo", "base": "usdt" },
# { "datatype": "OHLCV", "markettype": "futures", "market_venue": "bibox", "symbol": "algo", "base": "usdt" }

# Into:
# { "datatype": "[OHLCV]", "markettype": "[spot, futures]", "market_venue": "bibox", "symbol": "ada", "base": "usdt" },
# { "datatype": "[OHLCV, raw_trades]", "markettype": "[spot]", "market_venue": "bibox", "symbol": "ada", "base": "usdt" },

__author__  = "Daniel Souza <me@posix.dev.br>"

import argparse, os
import pandas as pd
import json

def _consolidate(src_json):
    raw = pd.read_json(src_json)

    grouped = raw.groupby(["market_venue", "symbol", "base"])

    aggregated = grouped.agg({
        "datatype": lambda x: ", ".join(set(x)),
        "markettype": lambda x: ", ".join(set(x))
    }).reset_index()

    output = aggregated.to_dict("records")

    dst_name, dst_extension = os.path.splitext(src_json)

    with open(dst_name + "-consolidated" + dst_extension , "w") as f:
        json.dump(output, f)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', dest='src_path', help="Path to source JSON object")
    args = parser.parse_args()

    if os.path.isfile(args.src_path):
        _consolidate(args.src_path)

    else:
        print("Source file not found!")

main()
