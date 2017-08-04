string1 = raw_input("enter your message: ")
string2 = "kitty"
for i,c in enumerate(string1):
    if string1[i:i+5] == string2:
        print "found match at %d" %i
