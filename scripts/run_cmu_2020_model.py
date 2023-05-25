import mujoco
import mujoco.viewer

m = mujoco.MjModel.from_xml_path("data/mjcfs/humanoid_CMU_V2020.xml")
d = mujoco.MjData(m)

qpos = d.qpos
print(f"qpos.shape: {qpos.shape}")

qvel = d.qvel
print(f"qvel.shape: {qvel.shape}")