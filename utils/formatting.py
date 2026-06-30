def format_currency(value, currency_symbol="$"):
    """
    Formats a value as currency.
    """
    if value is None:
        return "N/A"
    return f"{currency_symbol} {value:,.2f}"

def format_percentage(value):
    """
    Formats a value as a percentage.
    """
    if value is None:
        return "N/A"
    return f"{value:.2f}%"
