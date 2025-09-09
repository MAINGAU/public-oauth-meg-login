# MAINGAU Energie Login Page - Static Content

This directory contains the downloaded static content from the MAINGAU Energie login page at https://auth.maingau-kraken.systems/login/

## Files

### Main Content
- `index.html` - Main login page with Django i18n support
- `static/clients/maingau/theme.css` - MAINGAU design system theme
- `static/common/layout.css` - Common layout styles
- `static/clients/maingau/favicon.ico` - Authentic MAINGAU favicon

### Features
- **Django i18n integration** with `{% trans %}` template tags
- **Modern MAINGAU design** with updated colors and typography
- **Responsive layout** that works on all devices
- **Authentic branding** with real favicon from maingau-energie.de

## Usage

Open `index.html` in a web browser to view the login page locally.

### Environment-Specific URLs

The password reset link in `index.html` needs to be updated based on the deployment environment:

- **Production**: `https://app.maingau-energie.de/passwort-vergessen`
- **Staging/Test**: `https://app-staging.maingau-energie.de/passwort-vergessen`

Update line 93 in `index.html` with the appropriate URL before deployment.

### For Django Projects
1. Copy `index.html` to your Django templates directory
2. Update the password reset URL (line 93) for your target environment
3. Run `python manage.py makemessages -l de` to extract translations
4. Edit `locale/de/LC_MESSAGES/django.po` with German translations
5. Run `python manage.py compilemessages` to compile

## Translation Example

The page uses direct English text for Django translations:

```django
{% trans "Email address" %}        → "E-Mail-Adresse" (German)
{% trans "Password" %}             → "Passwort" (German)
{% trans "Forgot your password?" %} → "Passwort vergessen?" (German)
```

See `locale_example.py` for complete translation mappings.

## File Structure

```
login-view/
├── index.html
├── static/
│   ├── common/layout.css
│   └── clients/maingau/
│       ├── favicon.ico
│       └── theme.css
└── locale_example.py
```