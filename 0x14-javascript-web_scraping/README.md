<h1> Web Scraping</h1>
Web scraping in JavaScript refers to the process of extracting data from websites using JavaScript code.
 It involves making HTTP requests to a website, fetching the HTML content, and then parsing and extracting the desired information from the HTML. 
JavaScript is commonly used for web scraping because it can run in web browsers, making it easy to interact with and manipulate the Document Object Model (DOM) of a web page.

Here is a basic outline of how web scraping in JavaScript typically works:

1. **Make an HTTP Request:**
   - Use JavaScript's XMLHttpRequest or the more modern Fetch API to make a request to the website's server.

2. **Retrieve HTML Content:**
   - Once the request is successful, you'll get the HTML content of the web page.

3. **Parse HTML:**
   - Use a parsing library or built-in DOM manipulation methods to parse the HTML and extract the relevant data.

4. **Extract Data:**
   - Identify the specific elements in the HTML that contain the data you want to scrape and extract that information using JavaScript.

5. **Handle Asynchronous Requests:**
   - If the webpage uses asynchronous requests to load data dynamically (e.g., AJAX), you might need to handle these requests to ensure you retrieve all the necessary data.

It's important to note that web scraping might be against the terms of service of some websites, and it's crucial to respect the website's policies and guidelines. Additionally, some websites implement measures to prevent or limit scraping, so you should be aware of legal and ethical considerations when engaging in web scraping activities.

There are also various JavaScript libraries and tools specifically designed for web scraping, such as Puppeteer, Cheerio, and Nightmare.js, which can simplify the process and provide additional features for handling complex scenarios.

<h2>More Info</h2>
Install Node 14
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
Install semi-standard
Documentation

$ sudo npm install semistandard --global
Install request module and use it
Documentation

$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules

Notes: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).
