import json, os, sys

root = sys.argv[1]
defn = os.path.join(root, "Report", "definition")
pages_meta = json.load(open(os.path.join(defn, "pages", "pages.json")))
order = pages_meta["pageOrder"]

def field_name(proj):
    return proj.get("nativeQueryRef") or proj.get("queryRef") or "?"

def get_title(objs):
    try:
        t = objs["title"][0]["properties"]
        if "text" in t:
            return t["text"]["expr"]["Literal"]["Value"].strip("'")
        return "(title object, no text)"
    except Exception:
        return None

def textbox_text(v):
    try:
        paras = v["objects"]["general"][0]["properties"]["paragraphs"]
        return " | ".join(r.get("value", "") for p in paras for r in p.get("textRuns", []))
    except Exception:
        return ""

for pid in order:
    page = json.load(open(os.path.join(defn, "pages", pid, "page.json")))
    print(f"\n########## PAGE: {page.get('displayName')}  ({page.get('width')}x{page.get('height')}) ##########")
    vdir = os.path.join(defn, "pages", pid, "visuals")
    if not os.path.exists(vdir):
        print("  (no visuals)")
        continue
    rows = []
    for vname in os.listdir(vdir):
        vj = json.load(open(os.path.join(vdir, vname, "visual.json")))
        v = vj.get("visual", {})
        vtype = v.get("visualType")
        pos = vj.get("position", {})
        qs = v.get("query", {}).get("queryState", {})
        fields = {role: [field_name(p) for p in blk.get("projections", [])] for role, blk in qs.items()}
        objs = v.get("objects", {}) or {}
        title = get_title(v.get("visualContainerObjects", {}) or {}) or get_title(objs)
        vco = v.get("visualContainerObjects", {}) or {}
        rows.append((pos.get("y", 0), pos.get("x", 0), vname, vtype, title, fields, objs, vco, pos, v, vj))
    rows.sort()
    for y, x, vname, vtype, title, fields, objs, vco, pos, v, vj in rows:
        print(f"  [{vtype}] x={pos.get('x',0):.0f} y={pos.get('y',0):.0f} w={pos.get('width',0):.0f} h={pos.get('height',0):.0f} z={pos.get('z')}")
        if title:
            print(f"      title: {title}")
        if fields:
            print(f"      fields: {fields}")
        if vtype == "textbox":
            print(f"      text: {textbox_text(v)[:300]}")
        if objs:
            print(f"      objects: {list(objs.keys())}")
        if vco:
            print(f"      containerObjects: {list(vco.keys())}")
        sg = v.get("syncGroup")
        if sg:
            print(f"      syncGroup: {sg.get('groupName')}")
        fc = vj.get("filterConfig")
        if fc:
            print(f"      filterConfig: {json.dumps(fc)[:300]}")
