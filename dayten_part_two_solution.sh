# This is not a solution from me (posted by handlestorm on Reddit). Just like ThePrimeagen's solution, I'm not taking credit for something I did not make.
echo "0" >> dayten_input.txt; sort -g dayten_input.txt | awk 'BEGIN{RS=""}{k=0;for(i=2;i<=NF;i++){if($i-$(i-1)==1)k++;else{print k*k/2-k/2+1"*";k=0;}}print k*k/2-k/2+1}' | tr -d '\n' | echo $(cat) | bc; sed -i '$ d' dayten_input.txt