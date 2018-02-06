def grades():
    for x in range(59,101,10):
        if x < 70 and x > 59:
            print "Score: 60 - 69; Grade - D"
        elif x < 80:
            print "Score: 70 - 79; Grade - C"
        elif x < 90:
            print "Score: 80 - 89; Grade - B"
        else:
            print "Score: 90 - 100; Grade - A"
grades()