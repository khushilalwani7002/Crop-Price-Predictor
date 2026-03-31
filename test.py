import pickle
le = pickle.load(open('le_state.pkl', 'rb'))
print("The AI knows these states:", le.classes_)