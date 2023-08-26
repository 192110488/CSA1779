print("       192110488--subhash")
print("       13.min max algorithm.")
import math

def minimax (curDepth, nodeIndex,
maxTurn, scores,
targetDepth):

  # base case : targetDepth reached
  if (curDepth == targetDepth):
      return scores[nodeIndex]
  
  if (maxTurn):
      return max(minimax(curDepth + 1, nodeIndex * 2,
      False, scores, targetDepth),
      minimax(curDepth + 1, nodeIndex * 2 + 1,
      False, scores, targetDepth))
  
  else:
      return min(minimax(curDepth + 1, nodeIndex * 2,
      True, scores, targetDepth),
      minimax(curDepth + 1, nodeIndex * 2 + 1,
      True, scores, targetDepth))
  
  # Driver code
scores = []
n=int(eval(input("enter the noof numbers::")))
print("enter values::")
for i in range(n):
    no=eval(input())
    scores.append(no)
treeDepth = math.log(len(scores), 2)
print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))
