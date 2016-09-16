from CE import *
from Reset_databases import *


i=1
BW=200000
T=1000
epsilon=0.1
DiscountFactor=0.9
maxReward=0
RESET_Tables(BW)
for i in range(100):
	Conf=EGreedy(i,epsilon,BW)

print "EGreedy"
print "conf1 ",Conf[1].modulation, Conf[1].innercode, Conf[1].outercode
print "conf0 ",Conf[0].modulation, Conf[0].innercode, Conf[0].outercode
print "\n##################### \n##################### \n"


##for i in xrange(0,11):
##    print i
