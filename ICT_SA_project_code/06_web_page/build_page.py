"""Build the single-file web page.
Inputs (same folder):  template.html  (contains the placeholder /*DATA*/)
                       data.json      (jobs, pairs, skillCat, bandOrder, levelOrder, sectorOrder, basisOrder)
Chart.js 4.4.4 is embedded so the page needs no external files:  npm i chart.js@4.4.4
Usage: python3 build_page.py path/to/chart.umd.js  ->  sa_ict_skills_analytics.html
"""
import sys, json, re
chart_js = open(sys.argv[1]).read()
tpl = open("template.html").read()
data = open("data.json").read()
page = tpl.replace("/*DATA*/", data, 1)
tag = '<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.4/chart.umd.min.js"></script>'
assert tag in page
page = page.replace(tag, "<script>/* Chart.js 4.4.4 (MIT), embedded so the page has no external dependency */\n" + chart_js + "\n</script>", 1)
open("sa_ict_skills_analytics.html", "w").write(page)
print("wrote", len(page), "bytes")
