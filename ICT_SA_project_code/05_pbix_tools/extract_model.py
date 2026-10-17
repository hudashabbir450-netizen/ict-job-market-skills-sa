"""Read measures, columns, relationships, Power Query and tables out of a .pbix data model.
Usage: pip install pbixray pandas ; python3 extract_model.py report.pbix outdir
"""
import sys, os
from pbixray import PBIXRay

pbix, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
m = PBIXRay(pbix)

print(m.dax_measures[["TableName", "Name", "Expression"]].to_string())   # DAX measures
print(m.dax_columns.to_string())                                         # calculated columns
print(m.relationships.to_string())                                       # model relationships
for _, r in m.power_query.iterrows():                                    # Power Query (M)
    open(os.path.join(out, r["TableName"] + ".m"), "w").write(r["Expression"])
for t in ["JobPostings", "JobSkills", "Skills"]:                         # table data -> CSV
    m.get_table(t).to_csv(os.path.join(out, t + ".csv"), index=False)
