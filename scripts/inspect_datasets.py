import h5py


# dset = h5py.File("data/dataset/small/CMU_015_04.hdf5", "r")
dset = h5py.File("/home/eric/anaconda3/envs/MoCapAct/lib/python3.8/site-packages/dm_control/locomotion/mocap/cmu_2020_dfe3e9e0.h5", "r")
print(dset.keys())