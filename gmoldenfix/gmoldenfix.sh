#!/bin/bash

# MR, Oct 2013
# This is a quick fix for making gmolden5.0.6.macosX work on a Mac.
# Alleviates the "mach-o but wrong architecture" problem.

# The script switches between i386 and x86_64 libraries in /usr/local/lib
# i386 libraries are needed for gmolden5.0.6.macosX, while x86_64 are for
# the previous version.

cd /usr/local/lib/

LIBS=( libgfortran.3.dylib libquadmath.0.dylib )

for ITEM in ${LIBS[@]};
    do
        if [ -f $ITEM ] && [ -f i386/$ITEM ]; then
            ARCH=$(file $ITEM | awk '{print $NF}')
            if [ $ARCH == 'x86_64' ] && [ -f ./i386/$ITEM ]; then
                sudo cp $ITEM $ITEM.backup.x86_64.script
                sudo cp ./i386/$ITEM .
                echo "i386 version of $ITEM succesfully installed."

            elif [ $ARCH == 'i386' ] && [ -f $ITEM.backup.x86_64.script ]; then
                sudo cp $ITEM.backup.x86_64.script $ITEM
                echo "x86_64 version of $ITEM succesfully restored."

            elif [ $ARCH == 'i386' ] && [ ! -f $ITEM.backup.x86_64.script ]; then
                echo "Nothing to do. The $ITEM is of the right architecture $ARCH."
            fi
        else
        echo "No gfortran libraries found. Please install gfortran first."
        fi
    done


