import pandas as pd

dataVal = [(10,20,30,40,50,60,70),
           (10,10,40,40,50,60,70),
           (10,20,30,50,50,60,80)]

df = pd.DataFrame(dataVal)

skewValue = df.skew(axis=1)

print(df, "\n", "A data frame using the array function")

print(skewValue, "\n", "The skewness of the data frame")


kurtValue = df.kurt(axis=1)

print(kurtValue, "\n", "The kurtosis of the data frame")

