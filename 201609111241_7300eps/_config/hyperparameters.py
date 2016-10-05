from collections import namedtuple


class GenericHyperparameters(object):
    NUM_EPISODES_TO_TRAIN = 75000
    EPISODE_SAVE_STEP = 150
    EPISODE_TRAINED_PLAY_METRICS_GATHER_STEP = 20
    MAX_REPLAY_MEMORIES_IN_RAM = 142080
    MAX_REPLAY_MEMORIES_PER_FILE = 5000

    AGENT_HISTORY_LENGTH = 4

    REACTION_TIME_MILISECONDS = 450
    GAME_FRAMES_PER_SECOND = 30
    FRAMES_SKIPPED_UNTIL_NEXT_ACTION = int(round((REACTION_TIME_MILISECONDS * GAME_FRAMES_PER_SECOND) / 1000))

    REPLAY_MEMORIES_MINIMUM_SIZE_FOR_LEARNING = int(round(50000 / AGENT_HISTORY_LENGTH))
    REPLAY_MEMORIES_RECENT_SAMPLE_SPAN = int(round(1000000 / AGENT_HISTORY_LENGTH))
    REPLAY_MEMORIES_TRAIN_SAMPLE_SIZE = 32

    EXPLORATION_INITIAL_EPSILON = 1.0
    EXPLORATION_FINAL_EPSILON = 0.1
    EXPLORATION_EPSILON_FULL_DEGRADATION_AT_STEP = int(round(1000000 / AGENT_HISTORY_LENGTH))

    Q_UPDATE_DISCOUNT_FACTOR = 0.99

    MAXIMUM_NO_ACTIONS_BEGGINING_EPISODE = 30

class ModelHyperparameters(object):
    METRICS_SAVE_STEP = 1000
    SGD_BATCH_SIZE = 32
    LEARNING_RATE_INITIAL = 0.00025
    LEARNING_RATE_FINAL = 0.00001
    LEARNING_RATE_DECAY_STEP = 150
    LEARNING_RATE_FINAL_AT_STEP = 4100 * 192
    RMS_DECAY = 0.9
    RMS_MOMENTUM = 0.95
    RMS_EPSILON = 0.01
    NUM_STEPS_ASSIGN_TRAIN_TO_FORWARD_PROP_GRAPH = 10000

ImageDescription = namedtuple("ImageDescription", ["num_channels"])
class ImageType(object):
    RGB = ImageDescription(num_channels=3)  # Red + Green + Blue channels (color image)
    Y = ImageDescription(num_channels=1)    # Luminance channel (greyscale image)
    RGBY = ImageDescription(num_channels=4) # RGB + Luminance

class PreprocessorHyperparameters(object):
    OUTPUT_WIDTH = 80
    OUTPUT_HEIGHT = 80
    OUTPUT_TYPE = ImageType.Y
    OUTPUT_NUM_CHANNELS = OUTPUT_TYPE.num_channels
