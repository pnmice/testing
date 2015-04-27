#!/bin/bash

set -o verbose
set -o xtrace

rm -rf ~/test/a
mkdir -p ~/test/a

code=$(echo "obase=2; ibase=10; $1" | bc | xargs printf "%04d\n")

bit1=$(echo ${code:0:1})
bit2=$(echo ${code:1:1})
bit3=$(echo ${code:2:1})
bit4=$(echo ${code:3:1})



if [ ! -d "~/test/a/$bit1" ];then
	mkdir ~/test/a/$bit1
	if [ ! -d "~/test/a/$bit1/$bit2" ];then
		mkdir ~/test/a/$bit1/$bit2
		if [ ! -d "~/test/a/$bit1/$bit2/$bit3" ];then
			mkdir ~/test/a/$bit1/$bit2/$bit3
			if [ ! -d "~/test/a/$bit1/$bit2/$bit3/$bit4" ];then
				mkdir ~/test/a/$bit1/$bit2/$bit3/$bit4
			fi	
		fi			
	fi	
fi


rm -rf ~/test/b
mkdir -p ~/test/b

code_b=$(echo "obase=2; ibase=10; $2" | bc | xargs printf "%04d\n")

bit1=$(echo ${code_b:0:1})
bit2=$(echo ${code_b:1:1})
bit3=$(echo ${code_b:2:1})
bit4=$(echo ${code_b:3:1})



if [ ! -d "~/test/b/$bit1" ];then
	mkdir ~/test/b/$bit1
	if [ ! -d "~/test/b/$bit1/$bit2" ];then
		mkdir ~/test/b/$bit1/$bit2
		if [ ! -d "~/test/b/$bit1/$bit2/$bit3" ];then
			mkdir ~/test/b/$bit1/$bit2/$bit3
			if [ ! -d "~/test/b/$bit1/$bit2/$bit3/$bit4" ];then
				mkdir ~/test/b/$bit1/$bit2/$bit3/$bit4
			fi	
		fi			
	fi	
fi