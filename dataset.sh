#!/bin/bash

DATASET_URL="http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz"
DATASET_DIR="food-101"
TAR_PATH="$DATASET_DIR/food-101.tar.gz"

download_dataset() {
    echo "Downloading Food-101 dataset"
    curl -L -o "$TAR_PATH" "$DATASET_URL"
}

extract_dataset() {
    echo "Extracting Food-101 dataset"
    tar -xzf "$TAR_PATH" -C "$DATASET_DIR"
}

delete_file() {
    echo "Cleaning up"
    rm "$TAR_PATH"
}


if [ ! -d "$DATASET_DIR" ]; then
    echo "Creating directory: $DATASET_DIR"
    mkdir -p "$DATASET_DIR"
fi

if [ -f "$TAR_PATH" ] || [ "$(ls -A $DATASET_DIR)" ]; then
    echo "Food-101 dataset already exists. No action needed."
else
    download_dataset
    extract_dataset
    delete_file
    echo "Food-101 dataset downloaded and extracted successfully."
fi
