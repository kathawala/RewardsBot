#!/bin/bash

DICT= 
DIR=$(cd "$(dirname "$BASH_SOURCE[0]]")" && pwd)

function setup_dict() {
    if [[ -n "${DICT}" ]]; then
	echo "Setting up dictionary file copied from: ${DICT}"
    elif [[ -f "/usr/dict/words" ]]; then
	DICT="/usr/dict/words"
	echo "Setting up dictionary file copied from UNIX built-in dictionary"
    elif [[ -f "/usr/share/dict/words" ]]; then
	DICT="/usr/share/dict/words"
	echo "Setting up dictionary file copied from UNIX built-in dictionary"
    elif [[ -d "/usr/share/dict" ]] && [[ $(ls "/usr/share/dict" | wc -l) -ne "0" ]]; then
	DICT="/usr/share/dict/"
	DICT="$DICT$(ls "${DICT}" | head -n 1)"
	echo "Setting up dictionary file copied from: ${DICT}"
    else
	echo "Please input path to dictionary file in the script's DICT variable"
	exit 1
    fi
    
    cp "${DICT}" "${DIR}/words"
}

if [[ ! -f "${DIR}/words" ]]; then
    setup_dict
fi
