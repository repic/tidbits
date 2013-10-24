#!/usr/bin/env awk -f

# MR, Oct 2013
# Script for computing an average and standard deviation of the sample
# for each column in a file containing an arbitrary number of columns.

# Empty lines and lines that contain alphabetic characters are ignored
# completely. Lines that do not have the same number of columns as the
# first line are also ignored from the calculations.


{
    # Get the number of columns in the first line
    if ( NR == 1 ) {
        nf = NF
    }

    # Skip lines matching the regex and incomplete lines
    if ( ! ( /[[:alpha:]]|^$/ || NF != nf ) ) {
        for (i = 1; i <= nf; i++) {
            sum[i] += $i        # column sum
            sumsq[i]+= $i * $i  # column sum of squares
            nr[i] += 1          # column records
        }
    }
}

# Calculate the averages and sample standard deviations (N-1)
END\
{
    # Print averages in one line
    for (i = 1; i <= nf; i++) {
        avg = sum[i] / nr[i]
        printf "%6.2f", avg
    }
    printf "  AV \n"

    # Print deviations in one line
    for (i = 1; i <= nf; i++) {
        stdev = sqrt( ( sumsq[i] - sum[i]^2 / nr[i] ) / (nr[i] - 1) )
        printf "%6.2f", stdev
    }
    printf "  SD \n"

    # Print number of records in one line
    for (i = 1; i <= nf; i++) {
        printf "%6i", nr[i]
    }
    printf "  NR \n"
}
