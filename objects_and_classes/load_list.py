import pickle
load_file = open('d:\\composers.dat', 'rb')
loaded_data = pickle.load(load_file)
print(loaded_data)