#! bash
function display() {
  YEL='\e[1;33m'
  YELB='\e[5;1;33m'
  NC='\033[25;15;0m' # No Color
  printf "${YELB}============================================================${NC}\n"
  printf "${YEL}\t ${1} ${NC}\n"
  printf "${YELB}============================================================${NC}\n"

}

display "Training START"

for SEED in 1 2 3; do
  display "Seed= $SEED"
  python train.py --seed $SEED
done

display "Training End"
