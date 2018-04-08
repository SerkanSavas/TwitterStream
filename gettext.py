import json
inp = open('input.txt', 'r')
out = open('output.txt', 'w')
for line in inp:
    if not line.strip():
        out.write(line)
        continue
    in_as_obj = json.loads(line)
    veri= in_as_obj.get('text')
    json.dump(veri, out, ensure_ascii=False)
    out.write('\n')
