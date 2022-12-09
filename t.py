import random


class RandomPickWithWeight:

    def __init__(self, w):
      # Write your code here
      # The integer's weight array is passed to the constructor
      self.sums = [0] * len(w)
      for i, elem in enumerate(w):
        if i == 0:
          self.sums[i] = elem
        else:
          self.sums[i] = self.sums[i-1] + elem
      # print("SUMS", self.sums)
      self.last_elem = self.sums[len(self.sums)-1]

    def pick_index(self):
        # Write your code here
        # Currently returning the first index
        # Your function should implement the required solution to this problem
      pick = random.randint(0, self.last_elem)
      # print("Picked running sum: ", pick)

      lo, hi = 0, len(self.sums)
      while lo < hi:
        mid = int(lo + ((hi-lo)/2))
        prev_mid = max(0, mid-1)
        if mid > 0:
          if pick <= self.sums[mid]:
            if pick > self.sums[mid - 1]:
              return mid
            else:
              hi = mid
          elif pick > self.sums[mid]:
            lo = mid
        else:
          if pick <= self.sums[mid]:
            return mid
          else:
            lo = mid
        
      return -1

# Driver code


def main():
    counter = 900
    weights1 = [1, 2, 3, 4, 5] # [1, 3, 6, 10, 15]
    # [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]
    #   
    weights2 = [1, 12, 23, 34, 45, 56, 67, 78, 89, 90]
    weights3 = [10, 20, 30, 40, 50]
    weights4 = [1, 10, 23, 32, 41, 56, 62, 75, 87, 90]
    weights5 = [12, 20, 35, 42, 55]
    weights6 = [10, 10, 10, 10, 10]
    weights7 = [10, 10, 20, 20, 20, 30]
    weights8 = [1, 2, 3]
    weights9 = [10, 20, 30, 40]
    weights10 = [5, 10, 15, 20, 25, 30]
    weights = [weights1, weights2, weights3, weights4, weights5,
               weights6, weights7, weights8, weights9, weights10]
    dict = {}
    for i in range(len(weights)):
        print(i + 1, ".\tInput: ", weights[i], ", pick_index() called ", counter, " times", "\n", sep="")
        [dict.setdefault(l, 0) for l in range(len(weights[i]))]
        for j in range(counter):
            sol = RandomPickWithWeight(weights[i])
            index = sol.pick_index()
            dict[index] += 1
        print("-"*95)
        print("{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<15}{:<5}{:<15}".format( \
            "Indexes", "|", "Weights", "|", "Occurences", "|", "Frequency", "|", "Expected Frequency"))
        print("-"*95)
        for key, value in dict.items():

            print("{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<15}{:<5}{:<15}".format(key, "|", weights[i][key], "|", value, "|", \
                str(round((value/counter)*100, 2)) + "%", "|", str(round(weights[i][key]/sum(weights[i])*100, 2))+"%"))
        dict = {}
        print("\n", "-"*100, "\n", sep="")


if __name__ == '__main__':
    main()
