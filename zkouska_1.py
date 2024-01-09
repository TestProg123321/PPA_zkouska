def shortwire(redwire,bluewire):
  if redwire>2:
    longwire(bluewire-1,redwire-2)
  print(redwire)
    

def longwire(greenwire,yellowwire):
  if greenwire>2:
    shortwire(greenwire-1,yellowwire-2) 
  print(greenwire)

shortwire(5,5)

