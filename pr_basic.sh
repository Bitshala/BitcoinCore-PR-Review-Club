#! /bin/bash

# Clone the bitcoin/bitcoin github repo
git clone git@github.com:bitcoin/bitcoin.git


# Check into the cloned repository
cd bitcoin

# Add the PR author's fork of bitcoin as a remote
git add andrewtoth git@github.com:andrewtoth/bitcoin.git

# Fetch the PR author
git fetch andrewtoth

# Checkout the particular PR. In this case https://github.com/bitcoin/bitcoin/pull/26533
git checkout andrewtoth/scan-and-unlink-pruned-files


# See the PR diff in your difttool editor. You can set your custom IDE too.
git difftool HEAD~1 HEAD


# Run autogen.sh
./autogen.sh


# Specify compilation configuration. Checkout `--help`` and productivity doc
./configure --without-miniupnpc --disable-bench --without-gui

# Compile. This will store `bitcoind`, `bitcoin-cli`, etc in `/src` directory
make -j -2

# Run all the unit tests
./src/test/test_bitcoin

# Run all the functional tests
./test/functional/test_runner.py