for i in ./bank/*.tt; do
	base=${i%.*}
 	touch $base".mack"
 	iconv -f ISO-8859-9 $i -t UTF-8 > $base".mack"
 	#cat $base".txt" | tr A-Z a-z | tr -c '[:alnum:]' '\n' | sort | uniq | fmt\
 	#> $base".mack"
 	rm $base".txt"
 	mkdir ./bank/originals
 	#mv i originals
done;