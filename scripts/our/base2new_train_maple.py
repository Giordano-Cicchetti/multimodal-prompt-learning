#!/bin/bash

#cd ../..

# custom config
DATA="G:\Giordano"
TRAINER="MaPLe"

DATASET="imagenet"
SEED=1

CFG="vit_b16_c2_ep5_batch4_2ctx"
SHOTS=16


DIR=f"output/base2new/train_base/{DATASET}/shots_{SHOTS}/{TRAINER}/{CFG}/seed{SEED}"

import os

if os.path.exists(os.path.join(os.getcwd(), DIR)):
    print(f"Results are available in ${DIR}. Resuming...")
    os.system(f"python train.py \
    --root {DATA} \
    --seed {SEED} \
    --trainer {TRAINER} \
    --dataset-config-file configs/datasets/{DATASET}.yaml \
    --config-file configs/trainers/{TRAINER}/{CFG}.yaml \
    --output-dir {DIR} \
    DATASET.NUM_SHOTS {SHOTS} \
    DATASET.SUBSAMPLE_CLASSES base")  
    
else:
    print(f"Run this job and save the output to ${DIR}")
    os.system(f"python train.py \
    --root {DATA} \
    --seed {SEED} \
    --trainer {TRAINER} \
    --dataset-config-file configs/datasets/{DATASET}.yaml \
    --config-file configs/trainers/{TRAINER}/{CFG}.yaml \
    --output-dir {DIR} \
    DATASET.NUM_SHOTS {SHOTS} \
    DATASET.SUBSAMPLE_CLASSES base")  
