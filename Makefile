help: # Print this help dialogue
	@grep -E '^#?[a-zA-Z_-]+:.*?# .*$$' Makefile \
		| column -t -s'#'

open: # Open slides in firefox
	firefox 'http://127.0.0.1:5052/slides/vtcc.html#1'

.PHONY: open
