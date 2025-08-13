def is_palindrome(s):
    normalized = s.lower().replace(" ", "")
    reversed_str = normalized[::-1]
    return normalized == reversed_str