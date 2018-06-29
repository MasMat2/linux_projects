import scipy.stats as st


def conf_interval(mean, deviation, percentage, population, cnt):
  zvalue = st.norm.ppf((1 + percentage/100)/2)
  plusminus = (zvalue*(deviation)/((population)**(1/2)))
  solved[cnt] = (mean,plusminus)

solved = {}
count = 0
finish = False
while True:
  count += 1
  problem = [0,0,0,0]
  print("Problem {}".format(count))
  q = 'Mean: Deviation: Percentage: Poplation:'.split()
  for val in range(len(q)):
    print("\t" + q[val], end = "")
    try:
      problem[val] = float(input())
    except:
      finish = True
      break
  if finish:
    break
  conf_interval(problem[0], problem[1], problem[2], problem[3], count)

for answer in solved.keys():
  print("Problem %s  Lower %f    Upper %f" % (answer, solved[answer][0] - solved[answer][1], solved[answer][0] + solved[answer][1]))
