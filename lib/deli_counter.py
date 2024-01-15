def line(queue):
  if len(queue) < 1:
    print("The line is currently empty.")
  else:
    new_list = []
    for i, person in enumerate(queue):
      new_list.append(f"{i + 1}. {person}")
    print("The line is currently: " + ' '.join(new_list))

def take_a_number(queue, new_person):
  queue.append(new_person)
  print(f"Welcome, {new_person}. You are number {len(queue)} in line.")

def now_serving(queue):
  if len(queue) < 1:
    print("There is nobody waiting to be served!")
  else:
    print(f"Currently serving {queue[0]}.")
    del queue[0]