# Insights

## CookieCutter or CookieMonster
I used cookiecutter template to make the initial project template. I believe I used ```https://github.com/arthurhenrique/cookiecutter-fastapi``` for this project.

I just wanted to get started so I did not give this much thought. Turns out I should have. For a simple project you should try to keep the setupsimple too. It seemed this extra bloated template (for this simple tictactoe app anyways) took me a long time to get things figured out and going. I had to delete quite a lot of folders and changed so many files that I beleve it would have been way faster to set it up from scratch.

I think templates save a lot of time; when you know exactly what you need and what you're about to do. Otherwise it can be a pain in the a-spiring mind and soul of this fragile computer geek.

## Life is a **test**
I never before thought of writing tests and then making the app. I tried this the first time when writing code for fastapi. This was magic to me. I wrote tests first and then the app making me consider many things, that I would generally miss and would have to write later, on the first go itself.

I also did not have to rush back and forth between postman and django files to test a feature out. The tests would do it for me. Maybe it was because I was not actually using django this time but FastAPI hehe. But I would like to try this method out again.

## D*cker
Docker is a very impoortant tool for deployment. I get it. But man I couldn't get my head around why you need a dockerfile and then a docker-compose.yaml and again the cookiecutter template made it more complicated to understand whatever I was supposed to do to get a docker file ready.

But yeah I got it done despite some issues with docker due to there being NUL character in requirements.txt as it was UTF 16 encoded for some reason and I just couldn't get rid of it due to pre-commit hook adding end-of-file fixes forcibly to that UTF 16 file and docker telling me it didn't understand a byte in the requirement file and making docker even frustrati-- *sigh* you get the idea right.

This was a rant more than a insight but yes, I got docker down.

## 12 Factors

## 1. **Codebase**

> *One codebase tracked in revision control, many deploys.*

* Got it. One project, many versions, one repo. **DONE**

---

## 2. **Dependencies**

> *Explicitly declare and isolate dependencies.*

* `venv` active.
* Tried `pyproject.toml` but found it too time-consuming.
* Used `pip freeze > requirements.txt` instead.

---

## 3. **Config**

> *Store config in the environment.*

* Minimal setup.
* *"What secret key does tictactoe in localhost even need?"*

---

## 4. **Backing Services**

> *Treat backing services as attached resources.*

* Got it. Models and Databases kept separate.

---

## 5. **Build, Release, Run**

> *Strictly separate build and run stages.*

* Dockerized.
* CI/CD pipeline in progress.

---

## 6. **Processes**

> *Execute the app as one or more stateless processes.*

* Still not very clear.
* Will explore with future projects.

---

## 7. **Port Binding**

> *Export services via port binding.*

* Docker on port `8080`, FastAPI on port `8000`.

---

## 8. **Concurrency**

> *Scale out via the process model.*

* Couldn’t scale `tictactoe`.
* Will choose a more appropriate project for this.

---

## 9. **Disposability**

> *Maximize robustness with fast startup and graceful shutdown.*

* Cleaning up models when used.

---

## 10. **Dev/Prod Parity**

> *Keep development, staging, and production as similar as possible.*

*  Avoiding tech stack drift.
* Not using MongoDB in dev and MySQL in prod.

---

## 11. **Logs**

> *Treat logs as event streams.*

* Set up logging.
* Haven’t actively used it yet.
* Still figuring out effective logging practices.

---

## 12. **Admin Processes**

> *Run admin/management tasks as one-off processes.*

* Yet to explore this.
* Will dive deeper through complex projects.

---

## **Summary:**
Solid progress made. Some factors (like scaling, admin processes, and logs) need more real-world projects to explore fully.
