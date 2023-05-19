# App Title

## Summary 
* This is a simulation trading app for both stocks and cryptocurrencies, targeted towards mobile users. It allows users to register, view near real-time market data, manage a virtual portfolio, execute trades, and gain an understanding and experience without any real-world financial risk.

## Team Members
* Brian Rogers
* Garrett Heiner

## Technologies we plan on using
* Backend: python, django, postresql
* Frontend: React, javascript
* Beautiful Soup -> this will be used for our DIY API. Scraping the stock prices off of MarketWatch will give us real time data for the user.
* TradingView Plugin -> this allows us to show historical graph data to the user of a specific stock without us having to 


---
## RESTful Routing Chart

| HTTP Verb | URL Pattern | CRUD Action | Description |
| --- | --- | --- | --- |
| POST | /register | CREATE | Register a new user |
| POST | /login | READ | Log in an existing user |
| GET | /logout | READ | Log out the current user |
| GET | /portfolio | READ | Show the current user's portfolio |
| POST | /portfolio/<ticker> | CREATE | Add a new asset to the portfolio |
| PUT | /portfolio/<ticker> | UPDATE | Update an asset in the portfolio |
| DELETE | /portfolio/<ticker> | DELETE | Remove an asset from the portfolio |
| POST | /trades | CREATE | Execute a trade |
| GET | /assets/search/<ticker> | READ | Search for a stock or crypto |
| GET | /assets/prices/<ticker> | READ | Get the real-time price of an asset |
| GET | /users | READ | Retrieve a list of all users |
| POST | /users/<username>/friends | CREATE | Send a friend request |
| PUT | /users/<username>/friends | UPDATE | Accept a friend request |
| DELETE | /users/<username>/friends | DELETE | Remove a friend |
| GET | /users/<username>/portfolio | READ | View a friend's portfolio |
| GET | /users/<username>/trades | READ | View a friend's trades |
---
## ERD
![erd](https://i.imgur.com/EgMCLCL.png)
---
## Wireframe
![wireframes 1](https://i.imgur.com/DUkbvG8.png)
![wireframes 2](https://i.imgur.com/aKM8qo5.png)

## User Stories 
* As a user, I want to register an account to keep track of my simulated portfolio
* As a user, I want to log into and out of my account & see my portfolio
* As a user, I want to search for stocks & cryptocurrencies by ticker
* As a user, I want to see near real-time prices of various stocks and cryptocurrencies
* As a user, I want to execute simulated buy/sell trades
* As a user, I want to see historical data and charts for stocks and crypto
* As a user, I want to friend users and see their trades/portfolios
* As a user, I want to view other users' profiles so that I can easily view all of *their* previous posts.

## MVP

* User needs to be able to see accurate and up to date stock prices and history.
* The user should be able to search for a specific stock to get more details for it.
* The ability to purcase a stock and also have the trade value go up and down with the market is a must.
* The user should also be able to purchase the same stock multiple times and at different values. (weekly buyers)
* User needs to be able to sell the stock and have the gains or losses update to their total funds.

## Stretches

* The ability to follow your friends and see what their investing in.
* Implement Pandas, Matplotlib and dateutil.parse to create graphs from the historical data and not rely on the plugin. (the plugin limits our design options)
* let the user create their own algorithim for automatic buying and selling.
* The user can save and name the algorithim and apply it other stocks.
* have a 'real world' mode where users can leave the sand box and buy and sell.
* Make a desktop version.

## Potential Roadblocks

* Calling the api to update the value of the stocks can be difficult especially when someone decides to sell multiple stocks for the same company but all at different values. It needs to be accurate.
* We want to have 'tickets' that will have the effect of covering the old window with the new buying or selling ticket. This could be a css obstacle.
* Working with react native is new, so we predict running into roadblocks there.
* If we hit our stretch goals than having the user create their own algorithims can prove difficult since they are creating conditions that will need to be turned into function in the program. 
* Not a roadblock but maybe a worry is if MarketWatch changes it's html page, we will need to update our application.

## Daily Sprints

**Friday**:
- Finalize project planning/approval
- Set up Django/PostgreSQL environment
- Begin user registration/login
- Continue web scraper for stocks

**Saturday**:
- Set up data models and relationships
- Finish the web scraper for stocks
- Test and validate stock data

**Sunday**:
- Double check data from scraper
- Connect frontend to backend

**Monday**:
- Add functionality for trades

**Tuesday**:
- Add functionality for portfolio tracking

**Wednesday**:
- Implement plugins
- Deployment?

**Thursday**:
- Bug fixes & testing

**Friday**:
- Present App