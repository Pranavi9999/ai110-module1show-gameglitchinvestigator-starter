# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  - I noticed that the hint was incorrect. I started with guessing the number 50, and it told me to go lower each time until I reached 1. Turns out the secret number was 57!
  - The difficulty levels are not set up properly. When I click the easy level, it allows a lesser number of guesses than the normal mode.
  - Clicking the new game button doesn't successfully start the new game

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
- I used Claude for this project. The suggestion that was corect was how to fix the refresh error. It gave the correct solution and it worked when I implemented it. One incorrect solution AI gave was for the test cases. It provided two test cases and one of them was overly complicated and tested things that did not need to be tested.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
- I decided that the first bug was fixed when I checked the website and found that the new game button allowed me to restart the game without having to refresh the window. I decided that the second bug was fixed when I played the game again and the hints were correct, and I was also able to win! I utilized Claude to help me write a pytest to ensure that the fixes that Claude provided were correct. AI helped me design the tests since I've never created them before.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?


- There were two bugs working together. First, on every even-numbered attempt, the code was converting the secret number to a string before comparing it, so instead of doing math like 7 < 67, it was doing alphabetical comparison like "7" vs "67". Alphabetically, "7" comes after "6", so it would say 7 is too high when it's actually too low. Second, the hint messages were swapped. "Too High" was telling me to go higher and "Too Low" was telling me to go lower. So between the wrong comparisons and the wrong directions, the hints flipped every turn.

- Imagine Streamlit re-reads and re-runs your entire Python script from top to bottom every single time you click a button or type anything. It's like refreshing the page, all your local variables get thrown away and start fresh. Session state is like a small notebook that Streamlit holds onto between those reruns. Anything you write into st.session_state survives the re-run, so the game can remember your score, your guess history, and the secret number across interactions.

-The secret was already stable. It was stored in st.session_state.secret so it survived reruns. The problem was the comparison logic casting it to a string on even attempts. Removing the if attempts % 2 == 0 block and always passing st.session_state.secret as an integer to check_guess meant every comparison used real number math, so the hints became consistent and the secret appeared to stay the same.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- I usually commit to Git using the terminal. This time I did it directly from VS Code. I think that I will resuse this in my future projects.

- I think I relied pretty heavily on using AI, and I think in the future I want to not utilize AI as heavily.

- AI makes working with code very easy. I noticed that with Claude built in it's very easy to integrate the code without thinking too much about it, which can potentially be a hinderance in learning.