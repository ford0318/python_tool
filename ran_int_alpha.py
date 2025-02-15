import random, string
import math

### generate a random string including letters and digits
def randnormalstring(lengths):
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(lengths))

### generate a random string including letters & digits & punc
def randpuncstring(lengths):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(lengths))


def writereport(documentname,):
    documentname = documentname +".text"
    with open(documentname,'a') as f :
            f.write("===================================================================================")
            #test_items_name = "TEST LENGTH:" + str(j) +"\n"
            f.write("TEST LENGTH:")
            for i in range(1000):
                a = randnormalstring(j)
                f.write(a)
                f.write("\n")
                
if __name__=="__main__":

    normllist=[1,5,100,300,500,1000,1500,2000]

    for j in normllist:
        with open('randnormalletter.txt','a') as f :
            # f.write("===================================================================================")
            # test_items_name = "\nTEST LENGTH:" + str(j) +"\n"
            # f.write(test_items_name)
            if (j>=300):
                for i in range(math.ceil(j/3)):
                    a = randnormalstring(j)
                    f.write(a)
                    f.write("\n")
            else:
                for i in range(100):
                    a = randnormalstring(j)
                    f.write(a)
                    f.write("\n")

    for j in normllist:
        with open('randspecialletter.txt','a') as f :
            # f.write("===================================================================================")
            # test_items_name = "\nTEST LENGTH:" + str(j) +"\n"
            # f.write(test_items_name)
            if (j>=300):
                for i in range(math.ceil(j/3)):
                    a = randpuncstring(j)
                    f.write(a)
                    f.write("\n")
            else:
                for i in range(100):
                    a = randpuncstring(j)
                    f.write(a)
                    f.write("\n")

    #lenlist = [k for k in range(4098) if (k%16==1) or (k%16==15)]
    lenlist =[1,15,16,17,31,32,33,1023,1024,1025,2047,2048,2049,4095,4096,4097]
    for j in lenlist:
        with open('sens_randnormalletter.txt','a') as f :
            # f.write("===================================================================================")
            # test_items_name = "\nTEST LENGTH:" + str(j) +"\n"
            # f.write(test_items_name)
            if (j>=300):
                for i in range(math.ceil(j/3)):
                    a = randnormalstring(j)
                    f.write(a)
                    f.write("\n")
            else:
                for i in range(100):
                    a = randnormalstring(j)
                    f.write(a)
                    f.write("\n")
    
    for k in lenlist:
        with open('sens_randspecialletter.txt','a') as f :
            # f.write("===================================================================================")
            # test_items_name = "\nTEST LENGTH:" + str(j) +"\n"
            # f.write(test_items_name)
            if (k>=300):
                for i in range(math.ceil(k/3)):
                    a = randpuncstring(k)
                    f.write(a)
                    f.write("\n")
            else:
                for i in range(100):
                    a = randpuncstring(k)
                    f.write(a)
                    f.write("\n")