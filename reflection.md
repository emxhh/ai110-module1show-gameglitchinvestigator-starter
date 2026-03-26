# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The hint is incorrect. It says the opposite direction.
- The history skips logging some attempts.
- Clicking New Game only changes the secret number. It doesn't clear the history or score and does not track attempts or score for the new game.
- Submitting an incorrect guess doesn't update the attempt, score, or history right away.
- Changing the difficulty doesn't appear to affect the secret number.
- The user is allowed to submit numbers outside of the range.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used Claude Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - I told AI that there is a bug with the history. It skips logging some guesses. It correctly identified that the number of attempts was being initialized to 1 instead of 0, which was leading to some errors.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - However, fixing the number of attempts to initialize at 0 fixed a different bug. It didn't fix the error that the history was not logging some guesses. When I prompted AI again, I gave it more details explaining that when clicking `Submit Guess`, I need to click it twice before the guess is submitted into the history. That may have been why some guesses were not being logged in the history. Claude identified that this is a known Streamlit behavior. The fix was to wrap the input and the button in a `st.form` to batch them both into a single submission.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - To check if a bug was really fixed, I ran the game and did a test manually.
  - Also, I ran the `pytest` test cases.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - I ran `test_guess_too_high`. Initially, the test failed even though I knew the bug was fixed. The test failed b/c the test result was asserted to just be "Win". However, the actual result was a tuple ("Too High", "📉 Go LOWER!"). I opted to update the test.
- Did AI help you design or understand any tests? How?
  - I used Claude to design the tests for the history to log attempts. It came up with 3 edge cases, which were relevant.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - The secret number was not changing in the app version that I forked. But from my understanding, if `st.session_state.secret = random.randint(low, high)` was set without a session state guard i.e. `if "secret" not in st.session_state:`, then a new secret would be set/overwritten on every user interaction. In Streamlit, the entire `app.py` script reruns every time a user interacts with the app. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Every time a user interacts with the app, i.e. clicks a button, types something, toggles the difficulty, etc., then the page would essentially refresh since Streamlit reruns the script. When this happens, the code is essentially re-run from scratch and each variable is recreated. Only things stored in the `st.session_state` would persist.
- What change did you make that finally gave the game a stable secret number?
  - Adding the conditional for the session state gives the game a stable secret number.
  ```
  if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)
  ```


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    - A habit that I will continue to reuse in the future is to create new chat sessions for each bug to keep the AI focused on one problem at a time. 
- What is one thing you would do differently next time you work with AI on a coding task?
  - Next time I work with AI on a coding task,  I would fine tune my asks. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - Overall, AI generated code for something like this has been mostly good. But it can be unfocused if not given the specific guidelines. 
