default:
	@cat Makefile

# Ten E.A. Poe works
get_texts:
	wget https://www.gutenberg.org/cache/epub/10947/pg10947.txt  	# 1. Best AMR Shorties
	wget https://www.gutenberg.org/cache/epub/17192/pg17192.txt 	# 2. The Raven 
	wget https://www.gutenberg.org/cache/epub/932/pg932.txt  	# 3. Fall, House of Usher
	wget https://www.gutenberg.org/cache/epub/1063/pg1063.txt  	# 4. Cask Amontillado
	wget https://www.gutenberg.org/cache/epub/10031/pg10031.txt  	# 5. Poems
	wget https://www.gutenberg.org/cache/epub/14082/pg14082.txt  	# 6. French raven
	wget https://www.gutenberg.org/cache/epub/50852/pg50852.txt  	# 7. Bells, Poems
	wget https://www.gutenberg.org/cache/epub/1064/pg1064.txt  	# 8. Masque Red Death
	wget https://www.gutenberg.org/cache/epub/32037/pg32037.txt  	# 9. Eureka Poems 
	wget https://www.gutenberg.org/cache/epub/51060/pg51060.txt  	# 10. Arthur G. Pym

raven_line_count:
	@echo "Raven line count:"
	@wc -l pg17192.txt | cut -d' ' -f1

raven_word_count:
	@echo "Raven word count:"
	@wc -w pg17192.txt | cut -d' ' -f1


raven_counts:
	@echo "Lines with 'raven' [lc]:"
	@grep -c 'raven' pg17192.txt
	@echo "Lines with 'raven' [uc]:"
	@grep -c 'Raven' pg17192.txt
	@echo "Lines with 'raven' [lc,uc]"
	@grep -ci 'raven' pg17192.txt

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

tests:
	@echo "Running PyTest for non-integration test cases in 'tests/' subdirectory.'"
	@bash -c "source env/bin/activate && pytest -vvx -m 'not integration' tests/"

integration_tests:
	@echo "Running PyTest for integration test cases in 'tests/' subdirectory.'"
	@bash -c "source env/bin/activate && pytest -vvx -m integration tests/"

cleanup_dir:
	@echo "Cleaning up directory..."
	@rm -f pg*.txt

all: setup_env get_texts
	@echo "---- Begin statistics about downloaded texts ----"
	@$(MAKE) --no-print-directory raven_line_count
	@$(MAKE) --no-print-directory raven_word_count
	@$(MAKE) --no-print-directory raven_counts
	@$(MAKE) --no-print-directory total_lines
	@$(MAKE) --no-print-directory total_words
	@echo "-------------------------------------------------"
	@$(MAKE) --no-print-directory tests
	@$(MAKE) --no-print-directory cleanup_dir


.PHONY: default get_texts raven_line_count cleanup_dir ravent_word_count raven_counts total_lines total_words setup_env tests all
