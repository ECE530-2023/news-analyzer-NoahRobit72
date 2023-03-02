## Here I am building a 3 APIs for:
* Secure File Uploader/Ingester
* Text NLP Analysis
* News feed Ingester

## Why Mongo DB?
1.  The document-oriented approach allows non-defined attributes to be modified on the fly. This is a key contrast between MongoDB and other relational databases. 
2.  JSON is widely used across for frontend and API communication. It only makes sense for the database to use the same protocol. 

Structure:
<img width="645" alt="Structure" src="https://user-images.githubusercontent.com/64294283/222464606-903732cb-db5e-4458-b021-8642afec1a98.png">


## Database Structure

The mongoDB will have 4 containers:

* User:
	* User ID: 
	* Username:
	* Password:

* Files:
	* File ID:
	* File Name:
	* File Type:
	* Favorite Status:

* UserFiles:
	* User ID:
	* File ID:

* Text Analysis:
	* File ID:
	* Sentiment Analysis
	* Summary Analysis 
	


