from .settings import Settings


class Setup:

    def __init__(self):
        pass

    def clear(self):
        from os import name, getenv, system
        _term = getenv('TERM')
        if getenv('TERM') is None:
            pass
        else:
            if name == 'nt':    # for windows
                _ = system('cls')
            else:   # for mac and linux(here, os.name is 'posix')
                _ = system('clear')

    def display(self, s: Settings = None):
        if s is None:
            return
        self.clear()
        for item in s.items:
            msg = '%s=%s' % (item['name'], item['value'])
            print(msg)
        return

    def user_input(self, msg, def_val) -> str:
        result = def_val
        s = '%s (%s):' % (msg, def_val)
        inp = input(s)
        if inp != '':
            result = inp
        return result

    def execute(self):
        done = False
        self.clear()
        settings = Settings()

        while done == False:
            for item in settings.items:
                msg = 'Provide %s' % item['name']
                defval = item['value']
                newval = self.user_input(msg=msg, def_val=defval)
                item['value'] = newval

        if self.user_input(msg='Update config file ? ', def_val='yes') == 'yes':
            settings.save_config()

        print(str(settings))