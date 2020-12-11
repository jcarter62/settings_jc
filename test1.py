from settings_jc import Settings, Export

s = Settings()
s.set('appname', 'mytestapp')
s.set('mysetting', '12345')
s.set('anotherSetting', 'abcdefg12345')
s.save_config()

print(s.items)
e = Export(settings=s)

e.export_to_file('e:\\projects\\py\\temp\\exportfile.txt')

