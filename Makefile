default:
	@cat Makefile

# Ten E.A. Poe works
get_texts:
	wget https://www.gutenberg.org/cache/epub/2147/pg2147.txt  # 1. The Fall of the House of Usher
	wget https://www.gutenberg.org/cache/epub/17192/pg17192.txt # 2. The Raven
	wget https://www.gutenberg.org/cache/epub/2148/pg2148.txt  # 3. The Raven VOL 2 and Other Works
	wget https://www.gutenberg.org/cache/epub/1063/pg1063.txt  # 4. The Masque of the Red Death
	wget https://www.gutenberg.org/cache/epub/2149/pg2149.txt  # The Pit and the Pendulum
	wget https://www.gutenberg.org/cache/epub/2150/pg2150.txt  # 6. The Tell-Tale Heart
	wget https://www.gutenberg.org/cache/epub/2151/pg2151.txt  # The Cask of Amontillado
	wget https://www.gutenberg.org/cache/epub/1064/pg1064.txt  # 8. The Murders in the Rue Morgue
	wget https://www.gutenberg.org/cache/epub/2152/pg2152.txt  # The Black Cat
	wget https://www.gutenberg.org/cache/epub/2154/pg2154.txt  # 10. The Purloined Letter

raven_line_count:
	@echo "Raven line count:"
	@wc -l pg2148.txt | cut -d' ' -f1

raven_word_count:
	@echo "Raven word count:"
	@wc -w pg2148.txt | cut -d' ' -f1


raven_counts:
	@echo "Lines with 'raven' [lc]:"
	@grep -c 'raven' pg2148.txt
	@echo "Lines with 'raven' [uc]:"
	@grep -c 'Raven' pg2148.txt
	@echo "Lines with 'raven' [lc,uc]"
	@grep -ci 'raven' pg2148.txt

total_lines:
	@echo "Total line count, all downloaded text files:"
	@wc -l pg*.txt | awk 'END {print $1}'

total_words:
	@echo "Total word count, all downloaded text files:"
	@wc -w pg*.txt | awk 'END {print $1}'


setup_env:
	python3 -m venv env
	./env/bin/pip install --upgrade pip
	./env/bin/pip install -r requirements.txt




.PHONY: default get_texts raven_line_count ravent_word_count raven_counts total_lines total_words setup_env
