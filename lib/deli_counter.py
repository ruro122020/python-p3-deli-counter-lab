katz_deli = []

def line(queue):
  if len(queue) < 1:
    print("The line is currently empty.")
  else:
    new_list = []
    for i, person in enumerate(queue):
      new_list.append(f"{i + 1}. {person}")
    print("The line is currently: " + ' '.join(new_list))

def take_a_number():
  pass

def now_serving():
  pass