import numpy as np

### Start
def main_task(start_choice):

  ### Input Process

  print('\nInput an m x n matrix below as an array as shown in the template below: \n\n Input: [[3, -9, 12, -9, 0, -9], [0, 2, -4, 4, 0, -14], [0, 0, 0, 0, 1, 4]]')
  print('\n Interpreted Matrix: \n', np.array([[3, -9, 12, -9, 0, -9], [0, 2, -4, 4, 0, -14], [0, 0, 0, 0, 1, 4]]))
  print('\nNote: Each entry must be greater than 10^-15')
  inp_mat = input()
  list_form =[[float(q) for q in u] for u in [v.split(',') for v in inp_mat.replace(' ', '').strip('[]').split('],[')]]

  ### Cleaning of Input
  def clean(input):
    mod_inp = []
    stor=[]

    for obj in input:
      if len((np.nonzero(obj))[0]) > 0:
        stor.append([(np.nonzero(obj))[0][0], obj])
      else:
        stor.append([10^99, obj])

    stor = np.array(stor, dtype='object')
    indexes = list([stor[:, 0]][0])

    for a in range(len(list(np.array(stor)[:, 0]))):
      ind = indexes.index(min(indexes))
      mod_inp.append(stor[ind, 1])
      indexes.remove(min(indexes))
      stor=np.delete(stor, (ind), axis=0)
    
    return mod_inp

  mod_inp = clean(list_form)
  t = np.array(mod_inp)
  r, c = t.shape
  print('\nOriginal Matrix: \n', np.array(list_form))

  ### Reduction
  correction = []
  if r <= c:
    for i in range(r):
      for j in range(i+1, r):
        if (t[i, i] != 0):
          t[j, :] = t[j, :] - (t[j, i]/t[i, i])*t[i, :]
        elif len(np.nonzero(t[i, :])[0]) > 0:
          t[j, :] = t[j, :] - (t[j, np.nonzero(t[i, :])[0][0]]/t[i, np.nonzero(t[i, :])[0][0]])*t[i, :]
      for j in range(i):
        if (t[i, i] != 0):
          t[j, :] = t[j, :] - (t[j, i]/t[i, i])*t[i, :]
        elif len(np.nonzero(t[i, :])[0]) > 0:
          t[j, :] = t[j, :] - (t[j, np.nonzero(t[i, :])[0][0]]/t[i, np.nonzero(t[i, :])[0][0]])*t[i, :]
    for j in range(r):
      if (t[j,j] != 0):
        t[j, :] = (1/t[j, j]) * t[j, :]
      elif len(np.nonzero(t[j, :])[0]) > 0:
        t[j, :] = (1/t[j, np.nonzero(t[j, :])[0][0]]) * t[j, :]

    t = np.array(clean(t))

  elif r > c:
    for a in range(r):
      correction.append([0])
    correction = np.array(correction)

    for a in range(r-c):
      t = np.append(t, correction, axis=1)
    for i in range(r):
      for j in range(i+1, r):
        if (t[i, i] != 0):
          t[j, :] = t[j, :] - (t[j, i]/t[i, i])*t[i, :]
      for j in range(i):
        if (t[i, i] != 0):
          t[j, :] = t[j, :] - (t[j, i]/t[i, i])*t[i, :]
    for j in range(r):
      if (t[j,j] != 0):
        t[j, :] = (1/t[j, j])*t[j, :]

    t = np.delete(t, slice(c, r), axis = 1)
    mod_t = list(t)
    mod_t = [[float(a) for a in b] for b in mod_t]
    t = np.array(clean(mod_t))

  for a in range(r):
    for b in range(c):
      if abs(t[a, b]) <= 10**(-15):
        val = +0.0
        t[a, b] = val
      t[a, b] = round(t[a, b], 4)
    
  print('\nRREF Matrix: \n', t)
  
#Interface
while True:
  start_choice_1 = input('Welcome! Select one of the choices (1 or 2) below to proceed: \n 1. Row Reduction Calculator \n 2. Help \n')
  if start_choice_1 not in ['1', '2']:
    print('Please enter either "1" or "2" to proceed\n')
    continue
  elif start_choice_1 == '1':
    main_task(start_choice_1)
    continue_op = input('\n Would you like to continue? \n 1. Yes\n 2. No\n')
    print('')
    if continue_op not in ['1', '2']:
      print('Please enter either "1" or "2" to proceed\n')
    elif continue_op == '1':
      continue
    elif continue_op == '2':
      break
  elif start_choice_1 == '2':
    print('\nMatrices are sets of numbers arranged in rows and columns so as to form a rectangular array. \nThey are widely used for specifying and representing geometric transformations (for example \nrotations) and coordinate changes. Row reduction is especially important for solving linear \nsystems. Restart the program to use the row reduction calculator!')
    print('\nHere is an example of an input for the calculator: ')
    print('\nInput: [[3, -9, 12, -9, 0, -9], [0, 2, -4, 4, 0, -14], [0, 0, 0, 0, 1, 4]]')
    print('\nOriginal Matrix: \n', np.array([[3, -9, 12, -9, 0, -9], [0, 2, -4, 4, 0, -14], [0, 0, 0, 0, 1, 4]]))
    print('\nRREF Matrix: \n', np.array([[1.0, 0.0, -2.0, 3.0, 0.0, -24.0], [0.0, 1.0, -2.0, 2.0, 0.0, -7.0], [0.0, 0.0, 0.0, 0.0, 1.0, 4.0]]))
    help_choice_1 = input('\n Would you like to return to the start page? \n 1. Yes\n 2. No\n')
    print('')
    if help_choice_1 not in ['1', '2']:
      print('Please enter either "1" or "2" to proceed\n')
    elif help_choice_1 == '1':
      continue
    elif help_choice_1 == '2':
      break
