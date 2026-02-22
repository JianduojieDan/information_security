#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 [directory]"
    exit 1
fi

TARGET_DIR=$1

echo "Deleting empty files in $TARGET_DIR..."
find "$TARGET_DIR" -type f -empty -print -delete
