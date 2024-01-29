from functools import reduce


def mean(values):
    return sum(values) / len(values)


def peerson_correlation(x, y):
    n = len(x)
    mean_x, mean_y = mean(x), mean(y)
    numerator = reduce(lambda acc, xy: acc + (xy[0] - mean_x) * (xy[1] - mean_y), zip(x, y), 0)
    denominator_x = reduce(lambda acc, xi: acc + (xi - mean_x) ** 2, x, 0)
    denominator_y = reduce(lambda acc, yi: acc + (yi - mean_y) ** 2, y, 0)
    correlation = numerator / (pow(denominator_x, 0.5) * pow(denominator_y, 0.5))
    return correlation


array1 = [1,2,3,4,5]
array2 = [2,4,5,5,7]

res = peerson_correlation(array1, array2)
print(res)