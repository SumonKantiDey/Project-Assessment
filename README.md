# Project-Assessment
**Used framework : Django REST framework**
## Api end point
```
GET/ http://127.0.0.1:8000/api/v1/values
GET/ http://127.0.0.1:8000/api/v1/values?keys=key1,key2...
POST/ http://127.0.0.1:8000/api/v1/values
PATCH/ http://127.0.0.1:8000/api/v1/values
```
## Done Task
```
> Use appropriate status codes
> Remove all values stored over more than 5 minutes. Used Advanced Python Scheduler 
  which will run autometically every one minutes from background if server is on. 
> SET TTL on every POST Request.
> Reset TTL on every PATCH and GET Request.
> Write unit test case to see the API is working perfectly or not.
```
For TTL automatically stored the posting date time when key value will send in POST request.
When user will send GET or PATCH request previous date time will replaced by present date time  of those key 
value and BackgroundScheduler will check the time of key value exceed five minutes or not.
