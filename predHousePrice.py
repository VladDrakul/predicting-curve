#!/usr/bin/python
import itertools
from numpy import *
from scipy.optimize import curve_fit
import scipy

#this is how the data should fit. t is the x (independent) variables, and a, b, and c are the coefficients
def fitFunc(t, a, b, c):
    return a + b*t[0] + c*t[1]

#same fitfunction but with lists for both the independent values, and the coefficients
def fitFuncL(t, l):
    #import pdb; pdb.set_trace()
    y = l[-1]
    for x,m in itertools.izip(t, l):
        y += x*m

    return y

#same fitfunction but with variable amount of parameters. On second thought, this is just like a list except not really
def fitFunc2(t, *args):
    leng = len(args)
    total = args[-1]
    leng = leng-1
    for argh in args[:-1]:
        total += t[leng-1] * argh

    return total
        
def fitFunc3(t, args):
    leng = len(args)
    total = args[-1]
    leng = leng-1
    for argh in args[:-1]:
        total += t[leng-1] * argh

    return total
        
def leastSquares(yVals, xVals):
    #yVals is all the yVals we know
    #xVals is a list of lists of the x-vals for each independent variable. "by column"
    yAvg = sum(yVals)/len(yVals)
    print yAvg
    xAvgs = []
    for xVar in xVals:
        print sum(xVar)/len(xVar)
        xAvgs.append(sum(xVar)/len(xVar))

    top=0
    bottom = 0
    m = []
    for xAvg,xCol in itertools.izip(xAvgs,xVals):
        for x,y in itertools.izip(xCol,yVals):
            top += (x-xAvg)*(y-yAvg)
            bottom += (x-xAvg)**2

        m.append(top/bottom) #LOLing at this line oh my goodness
        top = bottom = 0


    b = yAvg
    for anM, xAvg in itertools.izip(m,xAvgs):
        b - anM * xAvg

    m.append(b)
    return m


        #diffSum = reduce(lambda a,b: a+b, map(lambda a: a-xAvg,xVal)
    #for xAvg,xVal,yVal in xAvgs,xVals,yVals:
        #top.append

#main main it's so plain, blah blah whatever
def main():
    #F is how many independent variables there are
    #N is the number of training data sets there are
    F,N = map(int, raw_input().split())
    xData = []
    yData = []
    for _ in range(N):
        tmp = map(float, raw_input().split())
        #the first F are the independent variables, and the last one is the KNOWLEDGE (answer) from which we learn
        row = tmp[:F]
        ydat = tmp[-1]
        xData.append(row)
        yData.append(ydat)

    #turn into the lovely numpy data array things because that's what we need
    yDat = array(yData)
    xDat = array(xData)

    #oops I had the x data as rows, I need them as columns. because that's how the thing works
    tmp = []
    for i in range(F):
        tmp.append(xDat[:,i])

    print "what?"
    #import pdb; pdb.set_trace()
    squares = leastSquares(yData,tmp)
    print squares
    print "that was squares"
    #now I have the columns
    x = scipy.array(tmp)
    print "in row format: "
    print xDat
    print "in column format: "
    print x
    print

    print "the answers look like this!"
    print yDat

    #I need a function with F+1 number of parameters.
    #fuck this I'm tired here's the mess I'm thinking

    #import pdb; pdb.set_trace()
    
    def retFunc(f):
        return {
                1 : lambda t, a, b: fitFunc2(t, a, b),
                2 : lambda t, a, b, c: fitFunc2(t, a, b, c),
                3 : lambda t, a, b, c, d: fitFunc2(t, a, b, c, d),
                4 : lambda t, a, b, c, d, e: fitFunc2(t, a, b, c, d, e),
                5 : lambda t, a, b, c, d, e, f: fitFunc2(t, a, b, c, d, e, f),
                6 : lambda t, a, b, c, d, e, f, g: fitFunc2(t, a, b, c, d, e, f, g),
                7 : lambda t, a, b, c, d, e, f, g, h: fitFunc2(t, a, b, c, d, e, f, g, h),
                8 : lambda t, a, b, c, d, e, f, g, h, i: fitFunc2(t, a, b, c, d, e, f, g, h, i),
                9 : lambda t, a, b, c, d, e, f, g, h, i, j: fitFunc2(t, a, b, c, d, e, f, g, h, i, j),
                10 : lambda t, a, b, c, d, e, f, g, h, i, j, k: fitFunc2(t, a, b, c, d, e, f, g, h, i, j, k),
                }[f]

    testFunc = retFunc(F)
    print "F is: " + str(F)
    print testFunc(xDat, 1, 2, 3)
    print "was that testFuncy enough?"
    print testFunc(xDat, 2, 3, 4)
    print "bloop bleep fuck"
    #OH MY FUCKING GOD THERE HAS TO BE AN EASIER WAY TO DO THAT
    #computer do it for me somehow please oh god please oh please oh please
    #takes in a function to model the data (linear, parabolic? etc.), takes in independent variables, and takes in dependent variables. 

    #fitParams, fitCovariances = curve_fit(testFunc, x, yDat)
    #fitFunc2

    guess = []
    for i in range(F+1):
        guess.append(1)
    fitPars, fitCovs = curve_fit(fitFunc2, x, yDat, guess)



    
    #now we have to do the predictions
    N2 = int(raw_input())
    for _ in range(N2):
        xVals = map(float, raw_input().split())
        #print "new func: "
        #print fitFuncL(xVals, squares)
        #print testFunc(xVals, fitParams[0], fitParams[1], fitParams[2])
        import pdb; pdb.set_trace()
        print fitFunc3(xVals, fitPars)






main()

