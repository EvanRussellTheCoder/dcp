#question: make array return an array of all the products of all the items of a list except itself (ex: [1, 2, 3] would be [6, 3, 2])
#best python solution is in this video: https://www.youtube.com/watch?v=bNvIQI2wAjk&t=607s
def productArray(arr):
    #new array, set it all to ones at first
    res = [1] * len(arr)
    #prefix variable to set items in result array equal to i
    prefix = 1
    #loop that sets every item in res equal to prefix's value at the time it's iterated (the last item in the list won't convert to the biggest number)
    for i in range(len(arr)):
        res[i] = prefix
        prefix *= arr[i]
    #postfix does the same thing as prefix, but sets the values in reverse order
    postfix = 1
    #loop that sets every item in res array equal to postfix's value at the time it's iterated
    for i in range(len(arr) - 1, -1, -1):
        res[i] *= postfix
        postfix *= arr[i]
    return res