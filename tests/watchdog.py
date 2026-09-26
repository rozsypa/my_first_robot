#tohle ma udelat prvni koncept watchdog.
#nejprve to bude prijimat vstupy jako argumenty, potom uz primo pres
#toppic

def Watchdog(t_now,t_last,t_timeout):
    if t_now is None or t_last is None or t_timeout is None:
        return False

    elif t_now - t_last>t_timeout:
        return False
    else:
        return True


print(Watchdog(None,None,0.1))
assert(Watchdog(None,None,0.2)==False)