# FamPay-Assignment

Backend Assignment (Intern)

<h4> TechStack Used</h4>
1. Python (Programming Language)<br>
2. Django (Web Framework)<br>
3. PostgreSQL (Database)<br>

<br>
<h3> How to setup and run locally </h3>
<br>
<h4>
  1. Clone the Repository <br>
  2. <a href="https://www.geeksforgeeks.org/python-virtual-environment/"> Create a Activate Python Virtual Environment </a></h5>
  3. Run the below command for installing the dependencies<br>
</h4>

    $ pip3 install -r requirements.txt

<br>
  5. Now redirect to FamPay-Assignment folder .

    $ cd FamPay-Assignment

<br>
  6. Now before running the server, Set up the database.
    
    $ python3 manage.py makemigrations
 
    $ python3 manage.py migrate

<br>
  7. Now run the following command for starting the server

    $ python3 manage.py runserver

<br>
  8. To View the list of the Videos, type the below command
  
    $ http://localhost:3000/index

<br>
  9. To Search for the Videos based on the title and description, type the following command
        
    $ http://localhost:3000/search/<str:title>/<str:description>

Now run the following apis described in the Postman collection for testing the project.
<br>

<h2> OverView</h2><br>

<h3><a href="https://www.getpostman.com/collections/610f88abd398de431fca"> Postman Collection</a></h3>

<br>

<h3> 1. Get Videos (GET Request)</h3>
Returns all the videos  sorted in descending order by latest published date. If you get an error of <b> API Quota Completed</b> , then add a new API key (refer to Step 2)
<img src="https://user-images.githubusercontent.com/69706506/129439215-04aff496-e084-4457-abc5-770a327c230c.png">
<br>
<img src="https://user-images.githubusercontent.com/69706506/129439830-6f796b3d-3601-4cef-9ee7-8b6001680e7f.png">

| Status |
| ------ |
| 200 OK |

<h3> 2. Add Key (POST Request)</h3>
When you get an error <b>All APIKey's Quota is over, Add a new APIKey</b>, then use this api, for adding a new YouTube Data API Key in the database.
<img src="https://user-images.githubusercontent.com/69706506/129439271-80aa6654-05bd-4814-93d7-5fabd1bb5fe9.png">
<br>
<img src="https://user-images.githubusercontent.com/69706506/129439795-64e21405-1e03-4358-9eaf-b2d3b9622bf1.png">

| Status |
| ------ |
| 200 OK |

<h3> 3. Search for Videos based on the <b> Title </b> and <b> Description</b>
To search for the Videos based on the <b> Title </b> and <b> Description </b> and then display the results on the webpage
<img src="https://user-images.githubusercontent.com/69706506/129439333-b98e7064-0080-4e4a-a5b6-78a78c6ff447.png">

| Status |
| ------ |
| 200 OK |
