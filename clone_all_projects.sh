#!/bin/bash

# Run from a non-git directory in which to clone all student projects
# listed in the repositories.
#
# TODO: the repositories filename should be an argument.

for line in $(cat ../2016-2017/repositories); do
    name=$(echo $line | sed -e 's|https://github.com/||; s|/.*$||;';)
    git clone $line $name
done
