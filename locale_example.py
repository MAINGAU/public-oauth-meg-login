# Django Translation Best Practices for MAINGAU Login Page
# This demonstrates the CORRECT way to structure Django translations

# ✅ BEST PRACTICE: Use direct, meaningful English text as translation keys
# ❌ AVOID: Abstract keys like "login.email_label" or "msg_001"

# Example German translation file (locale/de/LC_MESSAGES/django.po):
GERMAN_TRANSLATIONS = """
# LANGUAGE: German (de)
# CHARSET: UTF-8

#: templates/login.html:19 templates/login.html:77 templates/login.html:145
msgid "Login"
msgstr "Anmelden"

#: templates/login.html:105 templates/login.html:107
msgid "Email address"
msgstr "E-Mail-Adresse"

#: templates/login.html:119 templates/login.html:121
msgid "Password"
msgstr "Passwort"

#: templates/login.html:123 templates/login.html:124
msgid "Click to show your password"
msgstr "Klicken Sie, um Ihr Passwort anzuzeigen"

#: templates/login.html:155
msgid "Forgot your password?"
msgstr "Passwort vergessen?"

#: templates/login.html:160
msgid "New to MAINGAU?"
msgstr "Neu bei MAINGAU?"

#: templates/login.html:162
msgid "Sign up for a tariff"
msgstr "Tarif abschließen"
"""

# Example English translation file (locale/en/LC_MESSAGES/django.po):
ENGLISH_TRANSLATIONS = """
# LANGUAGE: English (en)
# CHARSET: UTF-8
# NOTE: English is typically the source language, so most strings remain unchanged

#: templates/login.html:19 templates/login.html:77 templates/login.html:145
msgid "Login"
msgstr "Login"

#: templates/login.html:105 templates/login.html:107
msgid "Email address"
msgstr "Email address"

#: templates/login.html:119 templates/login.html:121
msgid "Password"
msgstr "Password"

#: templates/login.html:123 templates/login.html:124
msgid "Click to show your password"
msgstr "Click to show your password"

#: templates/login.html:155
msgid "Forgot your password?"
msgstr "Forgot your password?"

#: templates/login.html:160
msgid "New to MAINGAU?"
msgstr "New to MAINGAU?"

#: templates/login.html:162
msgid "Sign up for a tariff"
msgstr "Sign up for a tariff"
"""

# Django Translation Best Practices Summary:
BEST_PRACTICES = {
    "✅ DO": [
        "Use meaningful English text as translation keys",
        "Write clear, complete sentences",
        "Use consistent terminology across the app",
        "Provide context with comments when needed",
        "Use {% blocktrans %} for complex strings with variables",
        "Mark strings for translation close to where they're used",
        "Use lazy translations (_) in forms and models",
        "Test translations in all supported languages"
    ],
    
    "❌ DON'T": [
        "Use abstract keys like 'login.email' or 'msg_001'",
        "Break sentences into multiple translation strings",
        "Hardcode text that should be translatable",
        "Forget to run makemessages after adding new strings",
        "Mix languages in the same translation file",
        "Use technical jargon as translation keys",
        "Forget to compile messages with compilemessages"
    ]
}

# Advanced Django Translation Features:
ADVANCED_FEATURES = """
1. **Pluralization Support:**
   {% blocktrans count counter=items|length %}
   There is {{ counter }} item.
   {% plural %}
   There are {{ counter }} items.
   {% endblocktrans %}

2. **Context-specific Translations:**
   {% trans "May" context "month name" %}
   {% trans "May" context "modal verb" %}

3. **Lazy Translations (for forms/models):**
   from django.utils.translation import gettext_lazy as _
   
   class LoginForm(forms.Form):
       email = forms.EmailField(label=_("Email address"))
       password = forms.CharField(label=_("Password"))

4. **Format Localization:**
   {% load l10n %}
   {{ value|localize }}  # Formats numbers/dates per locale

5. **Language Detection Order:**
   1. URL language prefix (/en/, /de/)
   2. Session language (if user changed it)
   3. Cookie language
   4. Accept-Language header from browser
   5. LANGUAGE_CODE setting (fallback)
"""

# Django Settings for Internationalization:
DJANGO_SETTINGS_EXAMPLE = """
# settings.py
LANGUAGE_CODE = 'en'  # Default/fallback language
TIME_ZONE = 'UTC'

USE_I18N = True       # Enable internationalization
USE_L10N = True       # Enable localization (number/date formatting)
USE_TZ = True         # Enable timezone support

LANGUAGES = [
    ('en', 'English'),
    ('de', 'Deutsch'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Optional: Language detection from URL
MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    # ... other middleware
]
"""

# Command Line Workflow:
CLI_WORKFLOW = """
# 1. Extract translatable strings from templates/code
python manage.py makemessages -l de
python manage.py makemessages -l en

# 2. Translate the strings in .po files
# Edit locale/de/LC_MESSAGES/django.po
# Edit locale/en/LC_MESSAGES/django.po

# 3. Compile translations to binary .mo files
python manage.py compilemessages

# 4. Test translations
python manage.py runserver
# Change browser language or use URL prefixes to test
"""