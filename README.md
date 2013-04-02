# Overview

Search for data that hashes to the correct goal output hash. This script will randomly Skein1024 hash data and check the digest output to determine how many bits are different from the goal output. If the goal is below a certain threshold (MIT's current score), it will print out "Yay!!" and the data which you should copy-paste into the XKCD input page for mit.edu.

# Quickstart

	sudo apt-get install build-essential
	sudo apt-get install python3.2    # Installed by default on Ubunutu 12.04
	sudo apt-get install python3-dev

    virtualenv venv --python=python3.2
    source venv/bin/activate
    pip install pyskein

    python3.2 xkcd-hashing.py

Wait and hope you see Yay!! and the random data that produces a hash that is close to the goal hash.

TODO list
+ Scrape the current MIT score
+ Automatically POST the data when found
+ Use the random bytes, right now the bit differences calculated for these are not the same as those calculated on the xkcd website for some reason.
+ Autodeployment on Amazon EC2
+ multithreading?

I might do some of these eventually, if psets magically get done...








