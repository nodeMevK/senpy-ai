1. PACKAGES
    1. `pip install anthropic`
    2. `pip install tweepy`
    3. `pip install ollama`
    4. `pip install twitter-api-client`
    5. `pip install pandas`
    6. `pip install Flask-SQLAlchemy`
    7. `pip install psycopg2`
    8. `pip install psycopg2-binary`

2. Download Ollama for your machine `https://ollama.com/download`
    - `ollama run {model}` to download and run model

    - make sure ollama version is >=0.5.7

3. Psql Version: 16.4
    - `psql -U postgres`

4. Llama Version:

5. Docker:
    - setup docker soon

6. **TODO** 

    1. ~~will try again with playwright~~

    2. ~~need to figure out ratelimit for twitter~~

    3. ~~with ollama implementation, not sure if i still have to download the llama model as well~~

    4. ~~ollama already installed~~

    5. have to create prompts next and templates

    6. ~~get cookies from a new a account~~ 

    7. ~~need to sort thru response~~

    8. ~~got to inner part of tweet  had to change approach slightly because dictionaries were nested with arrays~~

    9. ~~CLEAN UP, check for specific entry types to avoid error~~ 

    10. ~~Cleaned up a little but need to sort error and try, except statement~~

    11. ~~need to relax with requets being made, getting data ready for pandas df~~

    12. ~~Need to make models for db and finish setting up, postgres is already downloaded on the PC~~

    13. ~~Need to get back asap~~

    14. Want to look into voice capabilities and things of that nature
    
    15. ~~Need to check setup db and work on peresonality, will do that later tonight~~ 

    16. Need to come up with more specific reason for ai, was thinking an ai with a sole purpose to get a response from elon musk

    lo mismo 

    17. update psql on mac 

    18. ~~need to start implementing db and install psycopg2~~

    19. ~~Finish Models and then start seeding DB~~

    20. Try twitter.accounts alongside scraper to get more tweets, pretty sure scraper just isnt that good

    21. Ehh yk why im here fr 

    22. Adding some very important things here seriously 

    23. Added some more files for database and memory, need to make sure i can connect to db next time around (connect as in can create the initial db programmitcally)

    24. ~~need to clean up some files (or delete)~~

    25. start updating character files as well

    26. Updating character files now 

    Take my shirt off now the hoes stop breathing 

    27. Get db versions in place

    28. Having issues getting into db on mac 

    29. Use this link for ref
        - `https://stackoverflow.com/questions/69754628/psql-error-connection-to-server-on-socket-tmp-s-pgsql-5432-failed-no-such`
        - `brew services start postgresql@version`
        - `brew services stop postgresql@version`
    
    30. Data is successfully being pushed to db and db is setup

    31. Need to start messing with the prompts

    32. ~~Work on characters asap~~

    35. Begin pushing data constantly to db

    36. get docker going as well

    37. Getting docker ready to go 

    38. Make sure model handles responses well in next update

    39.  Need to test llama with new characters and prompts

    40. Swarm tech J(AI)NE ST

    41. Got llama working with prompts
        - need to organize data before going any further tbh

    44. J(AI)NE or Senp(ai)

    45. Tbh have more ideas for this but thinking of different things to integrate

    46. Thinking of integrating token scanner to get data and things of that nature

    47. Need to clean up other parts of repo

    48. Look into hallucination yeild

    49. Need to set up pipeline now tbh and organize db - look into vector dbs

    50. Also check back to creating custom models on `https://ollama.com/blog/python-javascript-libraries`

    51. important link: `https://github.com/ollama/ollama-python/tree/main/examples`

    52. Trying to update communication with ollama

    53. Something is up with ollama.create() - others on github are having the same issue
        - `https://github.com/ollama/ollama-python/issues/371`

    54. Going to start turning some files into classes to clean up and get ready for prod { scraper, agent, etc }

    55. Just some more links `https://www.geeksforgeeks.org/python-yield-keyword/`

    56. ML Learning link (really start studying these) `https://www.geeksforgeeks.org/machine-learning/?ref=outind`

    57. Going to add more in a few just needed a commit

    58. Mans on COD taking a little break innit

    59. have to update prompts for new class structure

    60. Classes and tests are working properly as of now - have to update cookies and clean up scraper class more still

    61. Start diagramming agent architecture

    62. Looking into formatting responses: length, format, things of that nature

    63. Going to set up deepseek tomorrow should be fire

    64. Still need to look into response formatting