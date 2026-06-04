# Remediation Notes

Author: chandu

## Security improvements

- Add Flask-Talisman or explicit secure headers for XSS and content security.
- Enable CSRF protection before adding forms.
- Replace any insecure library usage with safe alternatives.
- Keep debug mode disabled outside local development.
- Validate and encode user-controlled input before rendering.

## Pipeline improvements

- Add output gating so the CI job fails on high-risk findings.
- Store scan reports as pipeline artifacts.
- Use a dedicated security testing environment in CI.
- Tune scanner rules to reduce false positives.
- Track remediation status in pull requests.
