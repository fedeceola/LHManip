import os
import glob
import pickle
from PIL import Image
import numpy as np

# Create list of paths to all episodes
tasks_paths = glob.glob(f"{os.getcwd()}/*")
episode_paths = []
for task in tasks_paths:
    for i in range(10):
        episode_paths.append(f"{task}/{str(i)}")

# Read data for each episode
episodes = []
for episode_path in episode_paths:
    with open(f"{episode_path}/data.pkl", "rb") as f:
        data = pickle.load(f)
    episode = []
    num_steps = len(glob.glob(f"{episode_path}/images/*.png"))
    for i in range(num_steps):
        episode.append({
            'observation': {
                'image': np.asarray(Image.open(f"{episode_path}/images/{i}.png")),
                'secondary_image': np.asarray(Image.open(f"{episode_path}/images_left/{i}.png")),
                'wrist_image': np.asarray(Image.open(f"{episode_path}/images_wrist/{i}.png")),
                'depth': np.asarray(Image.open(f"{episode_path}/depth/{i}.png"))*data['depth_scales'][i*3],
                'secondary_depth': np.asarray(Image.open(f"{episode_path}/depth_left/{i}.png"))*data['depth_scales'][i*3+1],
                'wrist_depth': np.asarray(Image.open(f"{episode_path}/depth_wrist/{i}.png"))*data['depth_scales'][i*3+2],
                'state': data['observations']['states'][i][:23],
            },
            'action': data['actions'][i],
            'language_instruction': data['language_instruction'][i],
        })
    episodes.append(episode)
