def nonLocalFunc():
   a = 10
   def nonLocalFunc_internal():
       nonlocal a
       print('nonLocalFunc_internal \t', a)
   nonLocalFunc_internal()
   print('nonLocalFunc \t\t', a)

def localFunc():
   a = 10
   def localFunc_internal():
       a = 20
       print('localFunc_internal \t', a)
   localFunc_internal()
   print('localFunc \t\t', a)

nonLocalFunc()
localFunc()