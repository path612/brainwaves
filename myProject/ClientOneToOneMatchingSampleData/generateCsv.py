import csv

mycsv = csv.writer(open('cp.csv', 'w'))
mycsv.writerow([":20", ":22A", ":22C", ":30T", ":52A", ":82A", ":87A", ":77H",
                ":30V", ":36", ":32B", ":57A", ":33B", ":53A", ":56", ":57D", ":58A", ":24D"])
for i in range(1, 501):
    text_file = open("{}_message.txt".format(i), "r")
    lines = text_file.readlines()
    if(len(lines) == 19):
        a = lines[1].split(':')[2]
        b = lines[2].split(':')[2]
        c = lines[3].split(':')[2]
        d = lines[4].split(':')[2]
        e = lines[5].split(':')[2]
        f = lines[6].split(':')[2]
        g = lines[7].split(':')[2]
        h = lines[8].split(':')[2]
        i = lines[9].split(':')[2]
        j = lines[10].split(':')[2]
        k = lines[11].split(':')[2]
        l = lines[12].split(':')[2]
        m = lines[13].split(':')[2]
        n = lines[14].split(':')[2]
        o = 0
        p = lines[15].split(':')[2]
        q = lines[16].split(':')[2]
    if(len(lines) == 20):
        a = lines[1].split(':')[2]
        b = lines[2].split(':')[2]
        c = lines[3].split(':')[2]
        d = lines[4].split(':')[2]
        e = lines[5].split(':')[2]
        f = lines[6].split(':')[2]
        g = lines[7].split(':')[2]
        h = lines[8].split(':')[2]
        i = lines[9].split(':')[2]
        j = lines[10].split(':')[2]
        k = lines[11].split(':')[2]
        l = lines[12].split(':')[2]
        m = lines[13].split(':')[2]
        n = lines[14].split(':')[2]
        o = lines[15].split(':')[2]
        p = lines[16].split(':')[2]
        q = lines[17].split(':')[2]
    mycsv.writerow([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q])
