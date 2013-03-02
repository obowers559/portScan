import optparse
import socket
import threading
screenLock = threading.Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    connSktopen = 'FALSE'
    try:
        connSkt = socket(socket.AF_INET, socket.SOCK_STREAM)
        connSktopen = 'TRUE'
        socket.connSkt.connect((tgtHost, tgtPort))
        socket.connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print '[+]%d/tcp open'% tgtPort
    except:
        screenLock.acquire()
        print '[-]%d/tcp closed'% tgtPort
    finally:
        screenLock.release()
        if connSktopen=='TRUE':
            connSkt.close()

def portScan(tgtHost, tgtPort):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknown host"%tgtHost
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan results for: ' + tgtName[0] 
    except:
        print '\n[+] Scan Results fo: ' + tgtIP
    
    for tgtPort in tgtPort:
        t = threading.Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()
        
"""
Initialize the variables of the minimum and maximum ports
"""
tgt1 = 1
tgt2 = 65535

def main():

    parser = optparse.OptionParser('usage%prog  ' +\
        '-H <target host (either name or IP address)> -pst <target port start> -pnd <target port end>')

    parser.add_option('--H', dest='tgtHost', type='string', \
        help = 'specify target host')

    parser.add_option('--pst', dest='tgt1', type='int', \
        help = 'speicfy target port')

    parser.add_option('--pnd', dest='tgt2', type='int', \
        help = 'speicfy target port')

    (options, args) = parser.parse_args()


"""
A for loop that iteratest through all of the ports between the start port (tgtPortstart) and
the end port (tgtPortend), and concatenates them into a single string of CSVs.
"""
    tgtPortcon = str(options.tgt1)
    y = ''
    for x in range (options.tgt1, options.tgt2):
        x+=1
        y=str(x)
        tgtPortcon+=','+y 

    tgtHost = options.tgtHost


"""
Handle the exception if no Host or Port is entered
"""

    if (tgtHost == None) | (tgtPort == None):
                                   print parser.usage
                                   exit(0)



"""
An expression that splits the string along the commas...
Then feeds the sting (List??) to the function portScan.
"""
    tgtPort = str(tgtPortcon).split(',')
    portScan(tgtHost, tgtPort)

  
if __name__ == "__main__":
    main()
    
