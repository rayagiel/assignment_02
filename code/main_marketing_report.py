"""
main_marketing_report.py — the Marketing department's report.

Marketing does not care about individual transactions. They care about *products*:
which one earns the most money, and which one moves the most units. Those are
frequently not the same product, and the gap between them is the interesting part.

This is the payoff for building a package instead of a script. Marketing needs a
roll-up that Finance never asked for, so `summarize_by_item` and `find_top_entry`
were **added** to `sales_pipeline.transform` — and `main_finance_report.py` did
not change by a single character. That is what modular means: the package grows
by addition, not by editing everyone who already depends on it.

Before running:  pip install -r requirements.txt

    python code/main_marketing_report.py        # the fixed sample data
    python code/main_marketing_report.py 42     # the generated data for seed 42
"""

import sys
from sales_pipeline import get_raw_sales_data, clean_sales_data, print_item_table, summarize_by_item, find_top_entry

# --- The report ------------------------------------------------------------------
#
# Less scaffolding this time. The steps are described, but which function does each
# job — and what to call the result — is now yours to work out. Everything you need
# is in the package's public API; if a step sounds like arithmetic, the function
# already exists in transform.py.
#
# `main_finance_report.py` is your worked example for anything structural.

seed = None
if len(sys.argv) > 1 and sys.argv[1].strip() != "":
    seed = int(sys.argv[1])

print('   === MARKETING: Revenue by Item ===')
print()

raw_data = get_raw_sales_data(seed)


clean_data = clean_sales_data(raw_data)
summarized_data = summarize_by_item(clean_data)
sales_winner = find_top_entry(summarized_data, "units_sold")
revenue_winner = find_top_entry(summarized_data)

revenue_winner_total = revenue_winner['revenue']
print_item_table(summarized_data)
print(f'Top seller by revenue: {revenue_winner["item"]} (${revenue_winner_total:,.2f})')
print(f'Top seller by units:   {sales_winner["item"]} ({sales_winner["units_sold"]} units)')
