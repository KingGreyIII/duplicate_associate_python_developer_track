# first note

def wait_until_done():
    def check_is_done():
        # Add a keyword so that wait_until_done()
        # doesn't run forever
        global done
        if random.random() < 0.1:
            done = True

    while not done:
        check_is_done()


done = False
wait_until_done()

print('Work done? {}'.format(done))

# Second note

import random

def wait_until_done():
    done = False

    def check_is_done():
        nonlocal done
        if random.random() < 0.1:
            done = True

    while not done:
        check_is_done()

    return done

print('Work done? {}'.format(wait_until_done()))
