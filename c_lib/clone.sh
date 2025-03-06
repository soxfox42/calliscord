#!/bin/bash

# git submodules are evil
# fun fact: even git itself doesn't fully support its own submodule feature
# for instance, try making a worktree if you have submodules
# lol

cd "$(dirname "$0")"
[ -d ed25519 ] || git clone https://github.com/orlp/ed25519.git
[ -d json.h ]  || git clone https://github.com/sheredom/json.h.git
