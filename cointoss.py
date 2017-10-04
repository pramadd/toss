import random
head =0
tail=0
x = .23945593
y = .798839238

for i in range(1,5001):
    x_rounded = round(x)
    y_rounded = round(y)
    score = random.randint(x_rounded,y_rounded)  
    #print score
    #print i
    if score == 0   :
        head += 1
        print "Attempt #{}: It's a head! ... Got {} head(s) so far  and {} tails so far " .format(i,head,tail)
         
    else:
        score == 1
        tail += 1
        print "Attempt #{}: It's a tail! ... Got {} head(s) so far  and {} tails so far " .format(i,head,tail)
       