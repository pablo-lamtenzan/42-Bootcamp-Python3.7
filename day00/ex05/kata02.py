z = "0"
t = (3, 30, 2019, 9, 25)
for x in t:
    if len(str(x)) == 1:
        x = "0" + str(x)

print("%s/%s/%d %s:%s" % (t[3] if len(str(t[3])) == 2 else "0" + str(t[3]),
      t[4] if len(str(t[4])) == 2 else "0" + str(t[4]),
      t[2], t[0] if len(str(t[0])) == 2 else "0" + str(t[0]),
      t[1] if len(str(t[1])) == 2 else "0" + str(t[1])))
