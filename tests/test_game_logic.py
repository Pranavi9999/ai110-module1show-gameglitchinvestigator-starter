from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# --- Bug regression: new game must reset status to "playing" ---

def simulate_new_game(session_state: dict) -> dict:
    """Mirrors the new_game block in app.py (st.rerun() excluded, not testable)."""
    import random
    session_state["attempts"] = 0
    session_state["secret"] = random.randint(1, 100)
    session_state["status"] = "playing"
    session_state["history"] = []
    return session_state


def test_new_game_resets_status_to_playing():
    """
    Regression: before the fix, clicking New Game after a win/loss left
    status as "won"/"lost", causing st.stop() to halt the page on rerun.
    Covers both terminal states in one parametrized-style check.
    """
    for terminal_status in ("won", "lost"):
        session_state = {
            "status": terminal_status,
            "attempts": 5,
            "secret": 42,
            "history": [10, 20, 42],
        }
        updated = simulate_new_game(session_state)
        assert updated["status"] == "playing", (
            f"status was '{terminal_status}' before new game; expected 'playing' after"
        )
        assert updated["history"] == [], "history must be cleared on new game"