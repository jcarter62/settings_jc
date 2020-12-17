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

        def print_settings(items):
            for i in range(len(items)):
                print(f"{i}: {items[i]['name']} = {items[i]['value']}")
            return

        def print_one(n, items):
            for i in range(len(items)):
                if i == n:
                    print(f"{i}: {items[i]['name']} = {items[i]['value']}")
            return


        def update_item(n, nvalue, items):
            for i in range(len(items)):
                if i == n:
                    items[i]['value'] = nvalue
            return

        while not done:
            print('Current Settings:')
            print_settings(settings.items)
            print('')
            inp = input('(s)ave, (a)dd, (e)dit, (d)elete, (q)uit\n')
            inp = inp.lower()
            if inp == 's':
                settings.save_config()
            elif inp == 'e':
                item_num = input('Item # to Edit')
                print_one(item_num, settings.items)
                item_val = input('New Value for item')
                i = int(item_num)
                settings.items[i]['value'] = item_val
                settings.save_config()
            elif inp == 'd':
                item_num = input('Item # to Delete')
                i = int(item_num)
                print_one(i, settings.items)
                confirm_delete = input('Confirm deletion(y/n)').lower()
                if confirm_delete == 'y':
                    settings.items.pop(i)
                    settings.save_config()
            elif inp == 'a':
                item_name = input('Name')
                item_val = input('Value')
                settings.items.append({'name': item_name, 'value': item_val})
                settings.save_config()
            elif inp == 'q':
                done = True
