def verify_user(sender, user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    user.isVerified = True
    user.save(update_fields=['isVerified'])