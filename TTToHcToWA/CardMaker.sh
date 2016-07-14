#!/bin/bash

#Author: Jihwan Bhyun, 30 May 2016
#Usage : in TTToHcToWA dir. put seed card dir e.g. TTToHcToWA_3mu
#        Then in the TTToHcToWA Dir, make TTToHcTOWA_3mu && TTToHcToWA_1e2mu, then run ./shell ${LepDecayMode}
#        May change Process name and Mass list

##Variable Definitions

InputMhc="130"
InputMA="30"
LepDec=$1
Var1="MHc"
Var2="MA"
CardVar1="mhc"
CardVar2="mh3"
if [[ ${LepDec} == '1e2mu' ]]; then Process="TTToHcToWA_1e2mu";
elif [[ ${LepDec} == '3mu' ]]; then Process="TTToHcToWA_3mu";
else echo "Lepton Decay mode wrong, Type again"; exit 1;
fi

declare -a MhcList=("90" "100" "110" "120" "130" "140" "150" "160")
declare -a MAList=("10" "15" "20" "25" "30" "35")


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
