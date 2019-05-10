dataset = [[float(x) for x in s.strip().split(',')] for s in open('bifurcationFromSharelatex.csv').readlines()]

output = []

current = dataset[0][0]
uniquevals = []
threshold = 0.0005

for point in dataset:
    x,y = point[0],point[1]
    if x != current:
        output.append((current, len(uniquevals)))
        uniquevals = []
        current = x
    if len(uniquevals) == 0 or min(abs(z-y) for z in uniquevals) > threshold:
        uniquevals.append(y)

last = 1
changeVals = []
for point in output:
    x,y = point[0],point[1]
    if last != y:
        last = y
        changeVals.append(x)

x,y,z,w=changeVals[0],changeVals[1],changeVals[2],changeVals[3]
δ1 = (y-x)/(z-y)
δ2 = (z-y)/(w-z)
err = math.sqrt(2)*0.0001
pm1 = math.sqrt( (1/(z-y) * err)**2 + ((y-x)/((z-y)**2) * err)**2 )
pm2 = math.sqrt( (1/(w-z) * err)**2 + ((z-y)/((w-z)**2) * err)**2 )


print("Combined:")
δ = (δ1*pm1**-2 + δ2*pm2**-2)/(pm1**-2 + pm2**-2)
pm = (pm1**-2 + pm2**-2)**-.5
print(δ)
print("pm")
print(pm)
