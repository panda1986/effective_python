#!python

import eventlet, time

pool = eventlet.GreenPool()


def do_cycle():
    while True:
        eventlet.green.time.sleep(1)
        print "do cycle"

th = pool.spawn(do_cycle)
print "spawn a thread"

eventlet.green.time.sleep(5)
th.kill()

