# Approach:
#  put the list of lists into a dictionary where key = id and value = list of scores
#  ex: d = {1:[92, 93, 100, 87], 2: [77, 65, 49, 20]}
#  then manipulate the list values to get top five high scores


def highFive(items):
    d = {}
    # {1: [ 91, 94, 77...]}

    # take the first index of each list in the list, use as key
    # then for the dictionary's values =  we'll use a list to store all of the scores
    for i in items:
        # use a try to try to append
        try:
            d[i[0]].append(i[1])
        # otherwise except will create a list as dictionary's value
        except:
            d[i[0]] = [i[1]]

    for j in d:
        # sort the list of scores
        d[j].sort()
        # reverse the list to ascending order. And take the top 5 scores
        d[j] = d[j][::-1][:5]
        # then iterate through to take the average of the list of values
        return [[i, sum(d[i]) // len(d[i])] for i in d]





items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],
                            [1,87],[1,100],[2,100],[2,76]]

print(highFive(items))