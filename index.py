def grades(x):
    if x < 70 and x > 59:
        print "Score:", x , ";Grade - D"
    elif x < 80:
        print "Score:", x , ";Grade - C"
    elif x < 90:
        print "Score:", x , ";Grade - B"
    else:
        print "Score:",x , ";Grade - A"


for i in range(1,11,1):
    import random
    random_num = random.randint(60,100)
    grades(random_num)