import json


def parse_firm(s: str) -> dict:
    parts = s.strip().rstrip('.').split(' ')
    firm = None
    if len(parts) == 4:
        firm = {
            'name': parts[0],
            'legal_type': parts[1],
            'income': int(parts[2]),
            'expenses': int(parts[3]),
        }
    return firm


def make_result(firms):
    total_profit = 0
    profitable_firms = 0
    result_dict = {}
    for firm in firms:
        profit = firm['income'] - firm['expenses']
        result_dict[firm['name']] = profit
        if profit > 0:
            profitable_firms += 1
            total_profit += profit

    return [result_dict, {'average_profit': total_profit / profitable_firms if profitable_firms > 0 else 0}]


firms = []
with open('data/task7-input.txt') as infile:
    for line in infile:
        firm = parse_firm(line)
        if firm:
            firms.append(firm)

with open('data/task7-out.json', 'w') as outfile:
    result = make_result(firms)
    json.dump(result, outfile)
