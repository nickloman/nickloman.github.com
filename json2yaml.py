import yaml
import sys
import json

s = json.load(open(sys.argv[1]))
print yaml.safe_dump(s, allow_unicode=True)

