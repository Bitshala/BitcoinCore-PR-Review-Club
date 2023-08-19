#! /bin/bash

# Step 1: Clone the bitcoin/bitcoin github repo and install dependencies. You'd need to do it only the very first time.

git clone git@github.com:bitcoin/bitcoin.git
# Change directory into the cloned repository
cd bitcoin
# Install basic dependencies
sudo apt-get install build-essential libtool autotools-dev automake pkg-config bsdmainutils python3
# Install libboost tools
sudo apt-get install libevent-dev libboost-dev
# Install sqlite for wallet
sudo apt install libsqlite3-dev

# Step 2: Get the PR branch you want to test

# Add the PR author's fork of bitcoin as a remote. here https://github.com/bitcoin/bitcoin/pull/26533.
git remote add andrewtoth git@github.com:andrewtoth/bitcoin.git
# Fetch everything from the PR author
git fetch andrewtoth
# Checkout to the branch used in the PR.
git checkout andrewtoth/scan-and-unlink-pruned-files

# See the PR diff in your difftool editor. You can set your custom IDE too.
# For setting up VSCode as `difftool`, follow instructions here : https://www.roboleary.net/vscode/2020/09/15/vscode-git.html
git difftool HEAD~1 HEAD

# Step 3: Run autogen script, configure your build and compile

# Run autogen.sh
./autogen.sh
# Specify compilation configuration. Checkout `--help`` and productivity doc
./configure --without-miniupnpc --disable-bench --without-gui
# Compile. This will store `bitcoind`, `bitcoin-cli`, etc in `/src` directory
make -j2

# Step 4: Run the tests

# Run all the unit tests
./src/test/test_bitcoin
# Run all the functional tests
./test/functional/test_runner.py

# Step 5: Go mess around. You might like this too: https://jonatack.github.io/articles/how-to-review-pull-requests-in-bitcoin-core
