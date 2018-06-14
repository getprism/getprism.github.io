#!/bin/bash
rm *.png

mkdir -p silver black

./generate.py

# Silver frames
cd silver
fastlane frameit silver
mv *_framed.png ../

# Black frames
cd ../black
fastlane frameit
mv *_framed.png ../

rm -rf silver black
