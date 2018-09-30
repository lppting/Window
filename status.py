import json

def Write():
    d = {}
    local = {"location":{"lat":"0","lng":"0"}}
    d.update(local)
    sun = {"Sun":{"Azi":"0","Ele":"0","Where":"0"}}
    d.update(sun)
    s = {"status":{"inside":" ","outside":" "}}
    d.update(s)
    data =  json.dumps(d,indent=4)
    f = open("status.json","w+")
    f.write(data)
    f.close()
    print "ok"    

if __name__ == "__main__":
    Write()
