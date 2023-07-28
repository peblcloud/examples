import pebl

print("fetching key: foo")
print(pebl.kv.get("foo"))

print("setting new value for \"foo\"")
pebl.kv.set("foo", "bar")

print("checking new value for \"foo\"")
print(pebl.kv.get("foo"))
