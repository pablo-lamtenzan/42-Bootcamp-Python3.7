
def log(function):
    def timed(*args, **kargs):
        start = time.time()
        res = function(*args, **kargs)
        end = time.time()
        user_name = getpass.getuser()
        with open("machine.log", 'a+') as f:
            print("(%s)Runnng: %r [%2.2f ms]" % (user_name, function.__name__,
                 (end - start) * 1000), file=f)
        f.close()
        return res
    return timed
