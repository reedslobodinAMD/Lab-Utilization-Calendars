#!/bin/bash


cd images
for dir in *.dcgpu/ ; do
	mv $dir/*.png $dir/archive
done
