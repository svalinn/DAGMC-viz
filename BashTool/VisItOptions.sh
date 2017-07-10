#!/bin/bash
PythonScripts=../PythonTool
cd "${PythonScripts}"

printf "Options include the following: \n"
printf "'-i' for plots and possible operators \n"
printf "'-d' for default views with multiple windows \n"
printf "'-w' for multiple windows with plots and operators \n"
printf "'-m' for multiple slices \n"
printf "'-o' for orbital views \n"

echo "Enter choice: "

read InputOption

python MakeImagesTerminal.py $InputOption