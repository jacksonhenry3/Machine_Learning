curl 'http://imgur.com/r/ConfessionBear' -o '1.html'
grep -oh 'i.imgur.com/.........jpg' 1.html >urls.txt
sort -u urls.txt | wget -i-
# rm ./ConfessionBear/*
mv *.jpg ./ConfessionBear

curl 'http://imgur.com/' -o '2.html'
grep -oh 'i.imgur.com/.........jpg' 2.html >urls.txt
sort -u urls.txt | wget -i-
# rm ./FP/*
mv *.jpg ./FP


curl 'http://imgur.com/new/time' -o '3.html'
grep -oh 'i.imgur.com/.........jpg' 3.html >urls.txt
sort -u urls.txt | wget -i-
# rm ./test/*
mv *.jpg ./FP
mv *.jpg ./test
