# LHManip
This repository contains the python script to parse the **_LHManip_** dataset presented in the paper _**LHManip: A Dataset for Long-Horizon Language-Grounded Manipulation Tasks in Cluttered Tabletop Environments**_.

![example_seq](https://github.com/fedeceola/LHManip/assets/32268209/6f52231d-7750-40a2-b92c-20086b93c19d)

To parse the data, you need to download the dataset from [here](https://huggingface.co/datasets/fedeceola/LHManip). Then, after extracting the dataset from the downloaded _.zip_ files, run the _parse_dataset.py_ script in the _long\_horizon\_manipulation\_dataset_ folder.

For conciseness, in the provided snippet, we consider the state of the robot as a 23-dimensional array of values comprising all the *proprioceptive* observation in the order reported in Tab. 3 in the paper. Similarly, we provide the robot action as a 8-dimensional array comprising end-effector position and orientation displacements and the desired gripper opening displacement.



## Citing the papers

If you find this dataset useful, please consider citing the associated papers:

```bibtex
@INPROCEEDINGS{lhmanip,
  author={F. {Ceola} and L. {Natale} and N. {S}\"underhauf and K. {Rana}},
  booktitle={2024 Robotics: Science and Systems (RSS) Workshop on Data Generation for Robotics},
  title={{LHManip: A Dataset for Long-Horizon Language-Grounded Manipulation Tasks in Cluttered Tabletop Environments}},
  year={2024},
  volume={},
  number={},
  pages={},
  doi={}}

@INPROCEEDINGS{lhmanip,
  author={F. {Ceola} and L. {Natale} and N. {S}\"underhauf and K. {Rana}},
  booktitle={2024 Robotics: Science and Systems (RSS) Workshop on Mechanisms for Mapping Human Input to Robots},
  title={{LHManip: A Dataset for Long-Horizon Language-Grounded Manipulation Tasks in Cluttered Tabletop Environments}},
  year={2024},
  volume={},
  number={},
  pages={},
  doi={}}
```
