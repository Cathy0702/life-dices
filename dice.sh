today=$(date +%F)

python3 dice.py

git add .
git commit -m "dice: $today"
git push origin main