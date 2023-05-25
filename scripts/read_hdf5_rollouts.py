import h5py

dset = h5py.File("data/dataset/small/CMU_015_04.hdf5", "r")
print("Expert actions from first rollout episode:")
print(dset["CMU_015_04-0-181/0/actions"][...])