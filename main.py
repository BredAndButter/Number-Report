from collections import Counter
import math

# Count
amtofnum = input("How many number would you like to process: ")
amtofnum = int(amtofnum)

print()

nums = []
sums = 0
varnums = []
variance = 0

for x in range(amtofnum):
	numtoadd = input("What number: ")
	numtoadd = float(numtoadd)
	nums.append(numtoadd)

nums.sort()

# Minimum and Maximum
mins = nums[0]
maxs = nums[-1]

# Range
ranges = maxs - mins

# Sum
for x in range(len(nums)):
	sums += nums[x]

# Mean
mean = sums / amtofnum

# Variation
for x in range(len(nums)):
	varnums.append((nums[x] - mean) ** 2)

for x in range(len(varnums)):
	variance += varnums[x]

variance /= amtofnum

# Standard Deviation
deviation = math.sqrt(variance)

# Median
if len(nums) % 2 == 0: 
    median1 = nums[len(nums)//2] 
    median2 = nums[len(nums)//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = nums[len(nums)//2] 

# Mode
data = Counter(nums) 
get_mode = dict(data) 
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
  
if len(mode) == len(nums): 
    get_mode = "No mode found"
else: 
    get_mode = "Mode: " + ', '.join(map(str, mode))

# Histograph
print()

histo = dict(Counter(nums))
for x in range(len(histo)):
	print(str(list(histo)[x]) + "  |  " + '*' * list(histo.values())[x])



# Show the user the data
print()
print("Count: " + str(amtofnum))
print("Sum: " + str(sums))
print("Min: " + str(mins))
print("Max: " + str(maxs))
print("Range: " + str(ranges))
print("Median: " + str(median))
print(get_mode)
print("Mean: " + str(mean))
print("Variance: " + str(variance))
print("Standard Deviation: " + str(deviation))
print()

outchoice = input("Would you like to output the report [y/n]: ")

if outchoice.lower() == "y":
	outfile = input("Enter the name of the file: ")
	f = open(outfile, "w")
	f.write("Count: " + str(amtofnum) + "\nSum: " + str(sums) + "\nMin: " + str(mins) + "\nMax: " + str(maxs) + "\nRange: " + str(ranges) + "\nMedian: " + str(median) + "\n" + get_mode + "\nMean: " + str(mean) + "\nVariance: " + str(variance) + "\nStandard Deviation: " + str(deviation))
	f.close()
	print("Outputted to: " + outfile)
elif outchoice.lower() == "n":
	print()
	print("Did not output.")
else:
	print()
	print("Invalid.")