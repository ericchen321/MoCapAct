from mocapact import observables
from mocapact.sb3 import utils
# expert_path = "data/experts/CMU_083_33-0-194/eval_rsi/model"
expert_path = "data/experts/CMU_015_04-0-181/eval_rsi/model"
expert = utils.load_policy(expert_path, observables.TIME_INDEX_OBSERVABLES)

from mocapact.envs import tracking
from dm_control.locomotion.tasks.reference_pose import types
# dataset = types.ClipCollection(ids=['CMU_083_33'], start_steps=[0], end_steps=[194])
dataset = types.ClipCollection(ids=['CMU_015_04'], start_steps=[0], end_steps=[181])
env = tracking.MocapTrackingGymEnv(dataset)
obs, done = env.reset(), False
while not done:
    action, _ = expert.predict(obs, deterministic=True)
    obs, rew, done, _ = env.step(action)
    print(rew)