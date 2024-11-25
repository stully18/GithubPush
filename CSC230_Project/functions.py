import pandas as pd

df = pd.read_csv("CSC230.csv")
x_values = df['X'].values
y_values = df['Y'].values
probabilities = df['Probability'].values

marginal_x = df.groupby('X')['Probability'].sum()
marginal_y = df.groupby('Y')['Probability'].sum()

def getMargX():
    return marginal_x

def getMargY():
    return marginal_y

def find_expectedX():
    eOfX = 0
    for x,prob in marginal_x.items():
        eOfX += x * prob
    return round(eOfX,4)

def find_expectedY():
    eOfY = 0
    for y,prob in marginal_y.items():
        eOfY += y * prob
    return round(eOfY,4)

expectedX = find_expectedX()
expectedY = find_expectedY()

def find_VarX():
    eOfXsqr = 0
    for x,prob in marginal_x.items():
        eOfXsqr += x**2 * prob
    varX = eOfXsqr - expectedX**2
    return round(varX,4)

def find_VarY():
    eOfYsqr = 0
    for y,prob in marginal_y.items():
        eOfYsqr += y**2 * prob
    varY = eOfYsqr - expectedY**2
    return round(varY,4)

varX = find_VarX()
varY = find_VarY()

def findCov():
    EofXY = 0
    for index,row in df.iterrows():
        EofXY += row.product()
    tempCov = EofXY-expectedY*expectedX
    return round(tempCov,4)
cov = findCov()

def correlation():
    cor = cov/((varX**0.5)*(varY**0.5))
    return round(cor,4)
cor = correlation()
