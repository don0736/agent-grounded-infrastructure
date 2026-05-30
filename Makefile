.PHONY: validate sanitize dry-run-install

validate:
	./scripts/validate.sh

sanitize:
	./scripts/sanitize-check.sh

dry-run-install:
	./scripts/install.sh --dry-run

