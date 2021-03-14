

def extract_info(tr):
    return {
        "short_name": tr.select('td:nth-child(2) > a.tooltip > div')[0].text.strip(),
        "full_name": tr.select("td:nth-child(2) > a.tooltip")[0].get('data-tooltip'),
        "country": tr.select('td:nth-child(2) > a.tooltip > div > img')[0].get('title'),
        "age": tr.select('td.col.col-ae')[0].text.strip(),
        "overall_rating": tr.select('td.col.col-oa')[0].text.strip(),
        "potential": tr.select('td.col.col-pt')[0].text.strip(),
        "club": tr.select('td:nth-child(6) > div > a')[0].text,
        "height": tr.select('td.col.col-hi')[0].text.strip(),
        "weight": tr.select('td.col.col-wi')[0].text.strip(),
        "foot": tr.select('td.col.col-pf')[0].text.strip(),
        "best_postion": tr.select('td.col.col-bp')[0].text.strip(),
        "value": tr.select('td.col.col-vl')[0].text.strip(),
        "wage": tr.select('td.col.col-wg')[0].text.strip(),
        "VIT": tr.select('td.col.col-pac')[0].text.strip(),
        "TIR": tr.select('td.col.col-sho')[0].text.strip(),
        "PAS": tr.select('td.col.col-pas')[0].text.strip(),
        "DRI": tr.select('td.col.col-dri')[0].text.strip(),
        "DEF": tr.select('td.col.col-def')[0].text.strip(),
        "PHY": tr.select('td.col.col-phy')[0].text.strip()
        }