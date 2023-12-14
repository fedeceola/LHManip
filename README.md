# LHManip
This repository contains the python script to parse the **_LHManip_** dataset presented in the paper _**LHManip: A Dataset for Long-Horizon Language-Grounded Manipulation Tasks in Cluttered Tabletop Environments**_.

![example_seq](https://github.com/fedeceola/LHManip/assets/32268209/6f52231d-7750-40a2-b92c-20086b93c19d)

To parse the data, you need to download the dataset from [here](https://www.dropbox.com/scl/fi/6t717h5mo5kyhq521qavb/long_horizon_manipulation_dataset.zip?rlkey=rk4wsxp464x5bt4a8tgz563ne&dl=0). Then, after extracting the dataset from the downloaded _.zip_ file, run the _parse_dataset.py_ script in the _long\_horizon\_manipulation\_dataset_ folder.

For conciseness, in the provided snippet, we consider the state of the robot as a 23-dimensional array of values comprising all the *proprioceptive* observation in the order reported in Tab. 3 in the paper. Similarly, we provide the robot action as a 8-dimensional array comprising end-effector position and orientation displacements and the desired gripper opening displacement.
