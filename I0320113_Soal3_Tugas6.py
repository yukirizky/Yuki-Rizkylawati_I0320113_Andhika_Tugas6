# Program mengecek bilangan prima dalam rentang nilai tertentu
for bil in range(10,25):
    if bil % 2 == 0 or bil % 3 == 0:
        print("%d bukan prima"% bil)
    else:
        print("%d adalah bilangan prima" % bil)