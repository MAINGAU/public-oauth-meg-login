# MAINGAU Energie Login Page - Static Content

This directory contains the downloaded static content from the MAINGAU Energie login page at https://auth.maingau-kraken.systems/login/

## Downloaded Files

### Main Content
- `index.html` - Main login page HTML (5.1KB)

### CSS Files
- `static/common/layout.css` - Common layout styles (5.4KB)
- `static/clients/maingau/theme.css` - MAINGAU client-specific theme (6.8KB)
- `static/brands/maingau/theme.css` - MAINGAU brand theme (146B - likely empty/error)

### JavaScript Files
- `static/clients/maingau/ui.js` - MAINGAU client UI scripts (146B - likely empty/error)
- `static/brands/maingau/ui.js` - MAINGAU brand UI scripts (146B - likely empty/error)

### Assets
- `static/clients/maingau/favicon.ico` - Favicon (146B - likely empty/error)
- `static/brands/maingau/favicon.ico` - Favicon (146B - likely empty/error)
- `static/brands/maingau/logo.svg` - Logo SVG (returns 404 error)
- `static/clients/maingau/logo.svg` - Logo SVG (146B - likely empty/error)

## Notes

- The main HTML file and common layout CSS downloaded successfully
- The MAINGAU client theme CSS appears to have downloaded correctly (6.8KB)
- Several assets returned 404 errors or appear to be empty (146B files)
- Some resources may be protected or have different access patterns when accessed directly vs. through the browser

## Structure

The directory structure mirrors the original website's static file organization:
```
login-view/
├── index.html
└── static/
    ├── common/
    │   └── layout.css
    ├── clients/
    │   └── maingau/
    │       ├── favicon.ico
    │       ├── logo.svg
    │       ├── theme.css
    │       └── ui.js
    └── brands/
        └── maingau/
            ├── favicon.ico
            ├── logo.svg
            ├── theme.css
            └── ui.js
```

## Usage

To view the login page locally, open `index.html` in a web browser. The HTML file contains both the original absolute paths (commented out) and relative paths for local testing.

Note that some functionality may not work due to missing server-side components and authentication systems.

## Features

### Django i18n Integration
The login page is now fully integrated with Django's internationalization system:
- **Automatic language detection** based on Django's i18n framework
- **Translation tags** ({% trans %}) for all user-facing text
- **Compatible with Django's locale system** for German (DE) and English (EN)
- **No manual language switching** - handled by Django middleware

### Updated Design
- **New MAINGAU theme** based on Figma design specifications
- **Modern design system** with CSS custom properties
- **Improved typography** with RT Rondelle font family
- **Enhanced form styling** with better accessibility
- **Responsive design** that works on all devices

### File Structure Notes

The `index.html` file has been modified to include:
- **Original paths** (commented out): `/static/...` - these are the original absolute paths from the live website
- **Local testing paths** (active): `static/...` - these relative paths work when viewing the file locally
- **Django i18n template tags** ({% trans %}) for all translatable content
- **Authentic MAINGAU favicon** downloaded from [maingau-energie.de](https://www.maingau-energie.de/)

This approach allows you to:
1. See exactly how the original website was structured
2. View the page locally with working CSS and assets
3. Use Django's built-in internationalization system
4. Experience the updated MAINGAU design system with authentic branding

### Translation Files & Best Practices
The `locale_example.py` file demonstrates Django translation best practices:

#### ✅ **Recommended Approach: Direct Text**
```django
{% trans "Email address" %}
{% trans "Password" %}
{% trans "Forgot your password?" %}
```

#### ❌ **Avoid: Abstract Keys**
```django
{% trans "login.email_label" %}      # Don't do this
{% trans "form.password_field" %}    # Don't do this
```

#### **Why Direct Text is Better:**
- **Self-documenting**: Developers immediately understand the content
- **Translator-friendly**: Context is clear without looking up keys
- **Fallback safety**: Missing translations show meaningful English text
- **Django convention**: Follows Django's own patterns

#### **Complete Workflow:**
1. `python manage.py makemessages -l de` - Extract translatable strings
2. Edit `locale/de/LC_MESSAGES/django.po` - Add German translations
3. `python manage.py compilemessages` - Compile to binary format
4. Django automatically detects user language via browser/settings
