# QuizletScraper

Scrapes data from https://quizlet.com/stats/log and dumps it into JSON files  

I recommend setting up a cron job to `*/3 * * * * python /path/to/scraper.py` with a `"repeat": 4` and `"delay": 45` in scraper.cfg. This calls the script every 3 minutes, with a repeat of 4 and a delay of 45 seconds, which matches the web client built by Quizlet. This is done because cron does not support faster-than-every-minute jobs.