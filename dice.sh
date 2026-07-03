today=$(date +%F)

cd /home/sliu0702/life-dices

python3 dice.py

git add .
git commit -m "dice: $today"
git push origin main