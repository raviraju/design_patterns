from factory import Factory

someclass_obj = Factory.create_object('some_class')
someclass_obj.do_something('something')

defaultclass_obj = Factory.create_object('i dont know')
defaultclass_obj.do_something('something')

# if someclass_obj is not None:
#     myobj.do_something('something')
# else:
#     print('Not doing anything.')
