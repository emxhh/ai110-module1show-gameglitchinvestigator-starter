from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_hint_message_correct():
    _, message = check_guess(50, 50)
    assert message == "🎉 Correct!"

def test_hint_message_go_higher():
    # guess < secret → player should go higher
    _, message = check_guess(30, 50)
    assert message == "📈 Go HIGHER!"

def test_hint_message_go_lower():
    # guess > secret → player should go lower
    _, message = check_guess(70, 50)
    assert message == "📉 Go LOWER!"

def test_history_records_valid_guess():
    # A valid guess is parsed and appended to history
    history = []
    ok, value, _ = parse_guess("42")
    if ok:
        history.append(value)
    assert history == [42]

def test_history_accumulates_multiple_guesses():
    # Each valid guess is added in order
    history = []
    for raw in ["10", "50", "99"]:
        ok, value, _ = parse_guess(raw)
        if ok:
            history.append(value)
    assert history == [10, 50, 99]

def test_history_ignores_invalid_guess():
    # An invalid input is not appended to history
    history = []
    ok, value, _ = parse_guess("abc")
    if ok:
        history.append(value)
    assert history == []
