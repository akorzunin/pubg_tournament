from functools import wraps
from flask import session, redirect, url_for, flash, request
from cryptography.fernet import Fernet
from flask import current_app
from models import User
from urllib.parse import urlparse, urljoin

# Получение данных авторизованного пользователя
def get_current_user():
    user_id = session.get('user_logged')
    return User.query.get(user_id) if user_id else None

def is_safe_url(target):
    """Проверяет, что URL безопасен для перенаправления (чтобы избежать Open Redirect)."""
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

# Проверка авторизации пользователя
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not get_current_user():
            flash('Для доступа к данной странице необходимо авторизоваться', 'error')
            # Сохраняем URL, на который пытался зайти пользователь
            next_url = request.url
            return redirect(url_for('user.login', next=next_url))
        return f(*args, **kwargs)
    return decorated_function

# Проверка роли текущего пользователя (теперь включает проверку авторизации)
def role_required(required_roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user = get_current_user()
            if not user:
                flash('Для доступа к данной странице необходимо авторизоваться', 'warning')
                return redirect(request.referrer or url_for('public.home'))
            if user.role not in required_roles:
                flash('Недостаточно прав доступа', 'error')
                return redirect(request.referrer or url_for('public.home'))
            return f(*args, **kwargs)
        return wrapper
    return decorator

def get_cipher():
    """Инициализирует шифровальщик в контексте приложения"""
    return Fernet(current_app.config['FERNET_KEY'].encode())