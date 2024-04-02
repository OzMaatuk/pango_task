# Pre-Interview Assigment - Pango QA Automation position.

https://www.linkedin.com/jobs/view/3812358995

Use the `requierments.txt` file to install dependacies with `pip install requierments.txt`.

The project based on `pytest` and should be executed with `pytest -s`

The code in `automation_framework\utilities` was provided, need to implement the tests following the cases described in the `task.md` file.

The Bonus section output file will be in `report.txt` file on the top directory.

### Note to the reviewer:

Wish that i did get the purpose of the task, when dynamicly adding and calculating the avarage temp.

But it's actually not testing the API, but more like testing the DB operations, so i'm not sure.

Additionally, about the "Identify a relevant API to acquire city names for testing", thought you wanted to use the `https://api.openweathermap.org/geo/1.0/direct?q={}&limit={}`, but didn't managed to get 100 countried in efficient way.

So just used json file for countries list.
