# AppSec Threat Model

Author: chandu

## Application summary

The demo application exposes basic JSON endpoints and a profile lookup route. It is intentionally small so security controls can be reviewed clearly.

## Assets

- Application source code
- User-supplied route input
- CI/CD pipeline configuration
- Scan reports

## Threats considered

| Threat | Risk | Control |
| --- | --- | --- |
| Reflected script input | Browser-side abuse | Validate route input and return JSON |
| Clickjacking | UI abuse | `X-Frame-Options: DENY` |
| MIME sniffing | Content interpretation issue | `X-Content-Type-Options: nosniff` |
| Weak pipeline visibility | Vulnerabilities missed before deployment | Bandit and ZAP scan steps |
| Insecure debug mode | Sensitive runtime exposure | Debug disabled in app entrypoint |

## Next improvements

- Add authentication and authorization checks.
- Add CSRF protection before adding forms.
- Add dependency scanning.
- Store scan outputs as CI artifacts.
