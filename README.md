# Agent Trainer Results

Collection of [agent trainer](https://github.com/lopespm/agent-trainer) training sessions, each containing their resulting network, metrics and visualizations. More details in this [blogpost](http://lopespm.github.io/machine_learning/2016/10/06/deep-reinforcement-learning-racing-game.html).

## Setup

Since GitHub has a limit of 100MB per file, the tensorflow's network metric files were zipped and split to smaller files. To uncompress and place them in the correct folder:

```bash
# On agent-trainer-results´ root folder, execute these commands:
$ chmod u+x decompress_metrics.sh
$ ./decompress_metrics.sh
```

## Usage

Use [tensorboard](https://www.tensorflow.org/versions/r0.10/how_tos/summaries_and_tensorboard/index.html)<sup>1</sup> to explore the network's metrics:

```bash
# To see the metrics for a specific run:
$ tensorboard --logdir=/folder/where/repo/cloned/201609040550_5010eps/metrics-q-network

# To see the metrics for all runs: 
# (be aware that tensorboard takes some time to show all the runs after it is started, so you may have to wait some seconds until they are all ready for viewing)
$ tensorboard --logdir=/folder/where/repo/cloned
```

Use [agent-trainer](https://github.com/lopespm/agent-trainer) to play the game using the trained network, build the session's metrics or build a t-SNE visualization. For example:

```bash
$ cd /your/agent/trainer/folder/
$ python -m agent play -s 201609171218_175eps --resultspath /folder/where/repo/cloned/
```
    


## Contents Description


| Session | Machine | Training<br/>game mode  |  Learning rate decay                                                           |
| -------------------- | :---: | --- |---------------------------------------------------------------------- |
| 201609040550_5010eps | a) | timed; easy  | without learning rate decay          |
| 201609111241_2700eps | b) | timed; easy  |  unclipped learning rate decay   |
| 201609111241_7300eps | b) | timed; easy  |  unclipped learning rate decay   |
| 201609160922_54eps | b)   | unlimited time  | without learning rate decay        |
| 201609171218_175eps | b)  | unlimited time  | unclipped learning rate decay |

*Machines used for training:*

- (a) - AMD Athlon(tm) II X2 250 Processor @ 3GHz; 2GB RAM DDR3-1333 SDRAM; SSD 500 GB: Samsung 850 EVO (CPU only training)

- (b) - AWS EC2 g2.2xlarge (GPU enabled instance) with 200 GB General Purpose SSD (GP2)<sup>2</sup>

<br/>
---

<sup>1</sup> As of Tensorboard 16 (tested on OSX El Capitan), using tilde (~) to represent the home folder on *--logdir* will not work properly and tensorboard wont be able to detect the metrics files (for example, `tensorboard --logdir=~/temp/agent-trainer-results`)

<sup>2</sup> Each training run can reach up to 25GB worth of replay memories, which need to be accessed randomly during the training process. Since these cannot fit into the instance's 16GB of RAM, about 600 IOPS are required to keep the training performance acceptable. GP2 volumes provide more IOPS as you increase their size, hence the allocation of a 200 GB General Purpose SSD (GP2, 600 IOPS), which turns out to be more cost effective than a smaller 30GB, 600 IOPS Provisioned SSD (IO1).