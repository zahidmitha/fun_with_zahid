from numpy import *
from scipy.optimize import fixed_point
from scipy.optimize import fmin
import math ,sys
print "loading finished"

#===================
#
#This code is Final Project of Numerical Analysis
#
#Class of Prof.Andrew
#
#===================

#new outline
#1.settings
#2.reading data
#3.maximize likelihood

print "preparation start"

#==============
#settings
#==============

c = 1 #employment income
b = 0.4 #unemployment insurance
maxt = 20 #maximum period
T = 2.00 #duration of insurance
dt = 10**(-3) #finfo(single).eps * 100 #length of small time
r = 0.1 #discount factor
w = (c**(1-sigma) / (1-sigma)) / r #value of employed

#generate sequence of dt from 0 to T
smalls = arange(0,T+dt,dt)
dts = len(smalls)
maxsmalls = arange(0,maxt+dt,dt)
maxdts = len(maxsmalls)
durs = [] #container of data.txt

#count
counts = 0

#==============
#reading data.txt
#==============

def picknum(txt):
    if txt[10] == " ":
        return txt[11:17]
    else:
        return txt[10:17]

f = open("data.txt", "r")
for line in f:
    durs.append(float(picknum(line)))
f.close()

#compute locations of each agent
loc = zeros(len(durs))

#compute time t just before getting job
def locate(d):
    for i in xrange(maxdts):
        if d < maxsmalls[i]:
            return i

for i in xrange(len(durs)):
    loc[i] = locate(durs[i])

print "Preparation finished"

#==============
#likelihood function
#==============

#let parameter vector theta = [sigma, alpha, lamda]

def likelihood(theta):

    sigma = theta[0]
    alpha = theta[1]
    lamda = theta[2]

    global counts
    counts = counts+1
    print counts, "times likelihood"
    print "sigma = ",sigma, "alpha = ", alpha, "lamda = ", lamda

    #outline
    #2.compute V1
    #3.shooting method
    #4.derive likelihood
    
    #"=== 2 ==="
    #derive value and search cost of no insurance
    
    def value_noins(x):
        s = (alpha*lamda*(w-x))**(1/(1-lamda))
        v = (-s + alpha*(s**lamda) * (w-x)) / r
        return 0.9 * x + 0.1 * v

    print w, w-10
    v0 = fixed_point(value_noins, w-10)
    s0 = (alpha*lamda*(w-v0))**(1/(1-lamda))

    #"=== 3 ==="

    #shooting method

    #container of value and search cost during getting insurance
    value_ins = zeros(dts)
    scosts = zeros(dts)

    #substitute the value when t = T
    value_ins[dts-1] = v0
    scosts[dts-1] = s0

    #deribe previous value from current value and dt
    def value_prev(x,v_next):
        s = (alpha*lamda*(w-x))**(1/(1-lamda))
        v = ((b**(1-sigma))/(1-sigma) - s + alpha*(s**lamda) * (w-x) + (v_next - x) / dt) / r
        return 0.9 * x + 0.1 * v

    for i in range(dts-1):
        value_ins[dts-2-i] = fixed_point(value_prev, value_ins[dts-1-i] + 5 * dt, args=([value_ins[dts-1-i]]))
        scosts[dts-2-i] = (alpha*lamda*(w-value_ins[dts-2-i]))**(1/(1-lamda))
    #"=== 4 ==="

    #obtain likelihood when parameter and value of duration is given
    #by derive cumulative distribution function of search cost

    #compute hazard ratio (getting job rate)
    jrate = zeros(maxdts)
    for i in xrange(dts):
        jrate[i] = alpha * (scosts[i]**lamda)
    jrate[dts:maxdts] = alpha * (s0 ** lamda)
    
    #generate cumulative function
    cdf = zeros(maxdts-1)
    for i in xrange(maxdts-1):
        cdf[i] = 1 - exp(0 - (dt/2) * (sum(jrate[0:i]) + sum(jrate[0:i+1])))

    #deribe cumulative likelihood
    llh = 0
    for i in xrange(len(durs)):
        llh = llh + log(cdf[loc[i]])
    print "-likelihood = ", -llh
    print "========================="
    return -llh

print "Optimization start"

#initial value
g_sigma = 1.056
g_alpha = 0.3465
g_lamda = 0.19

initheta = array([g_sigma, g_alpha, g_lamda])

print fmin(likelihood, initheta)