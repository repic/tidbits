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


