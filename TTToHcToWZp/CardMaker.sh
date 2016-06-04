#!/bin/bash

#Author: Jihwan Bhyun, 30 May 2016
#Usage : 1) in TTToHcToWA dir. put seed card dir e.g. TTToHcToWA_3mu_MHc130_MA30_LO
#        2) Then in the TTToHcToWA Dir, make TTToHcTOWA_3mu && TTToHcToWA_1e2mu, 
#        3) Change Input Mass pt variable,e.g. InputMhc=130, InputMA=30, And change the process and corresponding variable names
#        4) Set the Mass point you want
#        5) then run ./shell ${SeedDirName}

##Variable Definitions

InputMhc="130"
InputMA="5"
Var1="MHc"
Var2="MZp"
CardVar1="mhc"
CardVar2="mzp"
Process="TTToHcToWZp_3mu"
declare -a MhcList=("90" "100" "110" "120" "130" "140" "150" "160")
declare -a MAList=("2" "5" "8")


##Main Code

InputSample=${Process}_${Var1}${InputMhc}_${Var2}${InputMA}_LO
for Mhc in "${MhcList[@]}"
do
  for MA in "${MAList[@]}"
  do
    DeltaM=$(( ${Mhc} - ${MA} ))
    if [ ${DeltaM} -lt 80 ] 
    then 
      continue
    fi

    DirName=${Process}_${Var1}${Mhc}_${Var2}${MA}_LO
    echo ${DirName}
    cp -r ${InputSample} ${Process}/${DirName}

    if [ ${InputMhc} -eq ${Mhc} ]
    then
       if [ ${InputMA} -eq ${MA} ]
       then
          continue
       fi
    fi

    mv ${Process}/${DirName}/${InputSample}_run_card.dat ${Process}/${DirName}/${DirName}_run_card.dat
    mv ${Process}/${DirName}/${InputSample}_proc_card.dat ${Process}/${DirName}/${DirName}_proc_card.dat
    mv ${Process}/${DirName}/${InputSample}_customizecards.dat ${Process}/${DirName}/${DirName}_customizecards.dat
    
    sed -i "s/${InputSample}/${DirName}/g" ${Process}/${DirName}/${DirName}_proc_card.dat
    sed -i -e "s/${CardVar1}\ ${InputMhc}/${CardVar1}\ ${Mhc}/g" -e "s/${CardVar2}\ ${InputMA}/${CardVar2}\ ${MA}/g" ${Process}/${DirName}/${DirName}_customizecards.dat
  done
done
