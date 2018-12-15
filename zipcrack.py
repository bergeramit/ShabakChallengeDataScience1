import optparse
import zipfile
from threading import Thread


#run from cmd!!
def extract_zip(zfile,password):
    try:
        zfile.extractall(pwd=password)
        print('Found pass word: ',password)
    except Exception as e:
        return
        pass

def Main():
    #made dynamic and via arguments in comand line
    Parser = optparse.OptionParser("usage prog "+\
                                   "-f <zipfile> -d <dictionary>")
    Parser.add_option("-f", dest= "zname",type='string',\
                      help='specify zip file')
    Parser.add_option("-d", dest= "dname",type='string',\
                      help='specify dictionary main')
    (options,args) = Parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(Parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
        # here we start the hacking
    zfile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        print("Trying: {}".format(password))
        t = Thread(target=extract_zip,args=(zfile,"262626"))
        t.start()

if __name__ == "__main__":
    Main()
