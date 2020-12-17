

class MyEnv:

    def __init__(self):
        pass

    def library_path(self):
        from os import path
        pth = path.abspath(__file__)
        return pth

    def bundle_dir(self):
        from os import path
        import sys
        result = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
        return result

    def executable(self):
        import sys
        result = sys.executable
        return result

    def exec(self):
        import sys, os
        frozen = 'not'
        if getattr(sys, 'frozen', False):
            # we are running in a bundle
            frozen = 'ever so'
            bundle_dir = sys._MEIPASS
        else:
            # we are running in a normal Python environment
            bundle_dir = os.path.dirname(os.path.abspath(__file__))

        args = sys.argv
        classpath = os.path.abspath(__file__)
        print('we are', frozen, 'frozen')
        print('class file path = ', classpath)
        print('bundle dir is', bundle_dir)
        print('sys.argv[0] is', sys.argv[0])
        print('sys.executable is', sys.executable)
        print('os.getcwd is', os.getcwd())
        for i in range(args):
            print('arg[', i, '] = ', args[i])

