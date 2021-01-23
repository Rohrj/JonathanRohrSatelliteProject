class Error(Exception):
    def __init___(self,args):
        Exception.__init__(self,"an exception was raised with arguments {0}".format(args))
        self.args = args