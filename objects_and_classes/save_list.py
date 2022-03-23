import pickle
composers = ['Mozart', 'Beethoven', 'Haydn', 'Chopin']
save_file = open('d:\\composers.dat', 'wb')
pickle.dump(composers, save_file)
save_file.close()
