# coding: utf-8
# Author: Zhongyang Zhang
# Email : mirakuruyoo@gmail.com

import torch
from z_functions import *


class Config(object):
    def __init__(self):
        self.USE_CUDA            = torch.cuda.is_available()
        self.LOAD_SAVED_MOD      = True
        self.SAVE_TEMP_MODEL     = True
        self.SAVE_BEST_MODEL     = True
        self.MASS_TESTING        = False
        self.NET_SAVE_PATH       = "./source/trained_net/"
        self.MODEL               = 'PolicyConvNet'
        self.PROCESS_ID          = 'xxyy_300_B.C.'
        self.SUMMARY_PATH        = "./source/summary/"+self.MODEL+'_'+self.PROCESS_ID
        self.NUM_VARIABLE        = 2
        self.NUM_EPOCHS          = 2000
        self.MOST_BEAR_STEP      = 300
        self.QUEUE_LENGTH        = 100
        self.TEST_EPOCH          = 100
        self.CRITERION           = 0
        self.GAMMA               = 0.95
        self.LEARNING_RATE       = 1e-4
        self.STEP_DECAY          = 0.8
        self.PRINT_EVERY         = 50

        self.BATCH_SIZE          = 512
        self.TEST_BATCH_SIZE     = 512
        self.NUM_WORKERS         = 0
        self.ZC                  = X2Y2()
        self.BOUNDARY            = [[-20, 20], [-20, 20]]
