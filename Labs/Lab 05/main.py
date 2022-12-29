file = open('data.txt', 'r')
outfile = open("output.txt", "w")
#print(file.readline().strip() + '  BMI')
print(file.readline().strip() + '  BMI         ')
avg_ht = 0
avg_wt = 0
avg_bmi = 0
heights = []
weights = []
bmis = []
for i in file.readlines():
    name = i[:12].strip()
    height = float(i[12:16].strip())
    weight = float(i[24:29].strip())
    bmi = weight / height ** 2
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(name, height, weight,
+bmi))
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(name, height, weight,
    +bmi), file=outfile)
    avg_ht = avg_ht + height
    avg_wt = avg_wt + weight
    avg_bmi = avg_bmi + bmi
    heights.append(height)
    weights.append(weight)
    bmis.append(bmi)
file.close()
print()
print('', file=outfile)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Average', avg_ht / 8,
                                                  avg_wt / 8,
                                                  +avg_bmi / 8), file=outfile)

print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Average', avg_ht / 8,
                                                  avg_wt / 8,
                                                  +avg_bmi / 8))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Max', max(heights),
                                                  max(weights),
                                                  +max(bmis)))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Max', max(heights),
                                                  max(weights),
                                                  +max(bmis)), file=outfile)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Min', min(heights),
                                                  min(weights),
                                                  +min(bmis)))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Min', min(heights),
                                                  min(weights),
                                                  +min(bmis)), file=outfile)
outfile.close()
