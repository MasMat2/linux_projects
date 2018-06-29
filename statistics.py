import scipy.stats as st

def proportion(n, sample, z):
    p = sample/n
    zet = st.norm.ppf((1+z)/2)
    det = zet*(((p*(1-p))/n)**(1/2))
    return ((p+det),(p-det))

def main():

    count = 0
    problems = {}
    while True:
        print()
        try:
            count += 1
            print("Sample size: ", end = "")
            n = float(input())
            print("Events: ", end = "")
            sample = float(input())
            print("Percentage: ", end = "")
            z = float(input())/100
            problems[count] = proportion(n, sample, z)
        except ValueError:
            break
    print()
    for problem in problems.keys():
        print("Problem %i Upper: %f, Lower: %f" % (problem, problems[problem][0], problems[problem][1]))

main()
