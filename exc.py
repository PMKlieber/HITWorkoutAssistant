
import time
import pyttsx3

from argparse import ArgumentParser
	  
clparser    =ArgumentParser()

clparser.add_argument('exercise', type=str, help="Name of exercise")
clparser.add_argument('-s', '--sets',type=int, help='number of sets',default=3)
clparser.add_argument('-r', '--reps',type=int, help='rep count per set',default=15)
clparser.add_argument('-p', '--pause',type=int, help='pause between sets',default=60)
clparser.add_argument('-i', '--initdelay',type=int, help='inital delay',default=60)
clparser.add_argument('-uc', '--upcount',type=int, help='length of up count',default=5)
clparser.add_argument('-dc', '--downcount',type=int, help='length of down count',default=5)
clparser.add_argument('-hc', '--holdcount',type=int, help='length of hold count',default=5)
clparser.add_argument('--countone', type=int, help='begin count at 1')
args=clparser.parse_args()



engine = pyttsx3.init() # object creation
engine.setProperty('rate', 60)

def js(i,rate=60):
  engine.setProperty('rate', rate)
  engine.say(i)
  engine.runAndWait()



def pset(n,pace=120,upcnt=5,holdcnt=5,downcnt=5,uphrase='up',dphrase='down',nofirstcnt=True):
  upstr=uphrase + ", " +  ", ".join([str(i) for i in range(1+nofirstcnt,upcnt+1)])
  holdstr='hold' + ", " +  ", ".join([str(i) for i in range(1+nofirstcnt,holdcnt+1)])	
  downstr=dphrase + ", " +  ", ".join([str(i) for i in range(1+nofirstcnt,downcnt+1)])
  for i in range(1,n+1):
    #js("up, 1, 2, 3, 4, 5. hold, 1, 2, 3, 4, 5. down, 1, 2, 3, 4, 5. {}".format(i),pace)
    #js("up, 2, 3, 4, 5, hold, 2, 3, 4, 5, down, 2, 3, 4, 5. {}".format(i),pace)
    js(upstr +", " + holdstr + ", " +downstr + ". {}".format(i),pace)
    time.sleep(.1)


			
def srest(s,i=15):
  print(time.time(),120)
  for j in range(0,int(s/i)):
    st=time.time()
    js("{} minute {} second".format(*divmod(s-i*j,60)),120)
    time.sleep(i-(time.time()-st))
    print(time.time())
  engine.setProperty('rate', 60)


def delap(st):
  print("{}:{:02d}".format(*divmod(int(time.time()-st),60)))

 
st=time.time()

def pexc(name, reps=15, sets=3, dsec=90,idel=30,upcnt=5,holdcnt=5,downcnt=5,uphrase='up',dphrase='down',nofirstcnt=True):
  js("Begin in {} seconds {}, {} sets of {} reps".format(idel,name,sets,reps),120)
  if idel>0: srest(idel)
  for j in range(0,sets):  	
    if j>0: srest(dsec)
    js("{} set #{}".format(name,j+1),120)
    pset(reps,120,upcnt,holdcnt,downcnt,uphrase,dphrase,nofirstcnt)
    delap(st)

print(args)

pexc(args.exercise, reps=args .reps,sets=args.sets,dsec=args.pause, idel=args.initdelay)