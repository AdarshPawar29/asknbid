**To Run the Script in command line**
*It's a R Script*
```
Adarshs-MacBook-Air:Problem6 adarshpawar$ ls
Problem6.R	sample.csv
Adarshs-MacBook-Air:Problem6 adarshpawar$ RScript Problem6.R sample.csv 3
Adarshs-MacBook-Air:Problem6 adarshpawar$ ls
Output_0	Problem6.R	sample.csv
Adarshs-MacBook-Air:Problem6 adarshpawar$ cat Output_0 	
"type"	"symbol"		"price"	"quantity"		"expirydate"		"strikeprice"	"amendtime"			  "id"		"parentid"
"P"		  "ICICIBANK"	1100		100			      20121210			   120			    "20121209103030		1237		1234
"P"	  	"ICICIBANK"	1100		100			      20121210			   120			    "20121209103030		1241		1234
"T"	  	"ICICIBANK"	1000		100			      20121210		     120		    	"20121209103030		1234		0
Adarshs-MacBook-Air:Problem6 adarshpawar$ 
```
**In Output0.txt file**<br />
*Tab separated variables*<br />
"type"	"symbol"		"price"	"quantity"		"expirydate"		"strikeprice"	"amendtime"			  "id"		"parentid"<br />
"P"		  "ICICIBANK"	1100		100			      20121210			   120			    "20121209103030		1237		1234<br />
"P"	  	"ICICIBANK"	1100		100			      20121210			   120			    "20121209103030		1241		1234<br />
"T"	  	"ICICIBANK"	1000		100			      20121210		     120		    	"20121209103030		1234		0<br />
