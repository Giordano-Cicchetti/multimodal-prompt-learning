#!/bin/bash

#cd ../..

# custom config
DATA="G:\Giordano"
TRAINER="MaPLe"

DATASET="imagenet"
SEED=1
CFG="vit_b16_c2_ep5_batch4_2ctx"

SHOTS=16
LOADEP=5
SUB="new"


COMMON_DIR=f"{DATASET}/shots_{SHOTS}/{TRAINER}/{CFG}/seed{SEED}"
MODEL_DIR=f"output/base2new/train_base/{COMMON_DIR}"
DIR=f"output/base2new/test_{SUB}/{COMMON_DIR}"

import os

if os.path.exists(os.path.join(os.getcwd(), DIR)):
    print("Evaluating model")
    print(f"Results are available in ${DIR}. Resuming...")
    os.system(f"python train.py \
    --root {DATA} \
    --seed {SEED} \
    --trainer {TRAINER} \
    --dataset-config-file configs/datasets/{DATASET}.yaml \
    --config-file configs/trainers/{TRAINER}/{CFG}.yaml \
    --output-dir {DIR} \
    --model-dir {MODEL_DIR} \
    --load-epoch {LOADEP} \
    --eval-only \
    DATASET.NUM_SHOTS {SHOTS} \
    DATASET.SUBSAMPLE_CLASSES {SUB}")  
    
else:
    print(f"Run this job and save the output to ${DIR}")
    os.system(f"python train.py \
    --root {DATA} \
    --seed {SEED} \
    --trainer {TRAINER} \
    --dataset-config-file configs/datasets/{DATASET}.yaml \
    --config-file configs/trainers/{TRAINER}/{CFG}.yaml \
    --output-dir {DIR} \
    --model-dir {MODEL_DIR} \
    --load-epoch {LOADEP} \
    --eval-only \
    DATASET.NUM_SHOTS {SHOTS} \
    DATASET.SUBSAMPLE_CLASSES {SUB}")  
'''
if [ -d "$DIR" ]; then
    echo "Evaluating model"
    echo "Results are available in ${DIR}. Resuming..."

    python train.py \
    --root ${DATA} \
    --seed ${SEED} \
    --trainer ${TRAINER} \
    --dataset-config-file configs/datasets/${DATASET}.yaml \
    --config-file configs/trainers/${TRAINER}/${CFG}.yaml \
    --output-dir ${DIR} \
    --model-dir ${MODEL_DIR} \
    --load-epoch ${LOADEP} \
    --eval-only \
    DATASET.NUM_SHOTS ${SHOTS} \
    DATASET.SUBSAMPLE_CLASSES ${SUB}

else
    echo "Evaluating model"
    echo "Runing the first phase job and save the output to ${DIR}"

    python train.py \
    --root ${DATA} \
    --seed ${SEED} \
    --trainer ${TRAINER} \
    --dataset-config-file configs/datasets/${DATASET}.yaml \
    --config-file configs/trainers/${TRAINER}/${CFG}.yaml \
    --output-dir ${DIR} \
    --model-dir ${MODEL_DIR} \
    --load-epoch ${LOADEP} \
    --eval-only \
    DATASET.NUM_SHOTS ${SHOTS} \
    DATASET.SUBSAMPLE_CLASSES ${SUB}
fi
'''