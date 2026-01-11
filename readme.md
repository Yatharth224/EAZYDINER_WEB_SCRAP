# 🍽️ EazyDiner Web Scraping Project

## Overview

This project demonstrates how to **scrape restaurant data from EazyDiner** in a structured and practical way.
It is designed as a **learning and reference project** to understand real-world web scraping challenges such as dynamic content, headers, cookies, and city-wise variations in data.

The repository focuses on collecting restaurant information across multiple Indian cities and dining categories.

---

## Data Fields Extracted

For each restaurant, the following details are scraped:

* **Restaurant Name**
* **Location**
* **Average Cost for Two**
* **Photos** (1 to 5 images per restaurant)

The data is organized in a clean format so it can be easily reused for analysis or further processing.

---

## Cities & Categories Covered

### Fine Dining

* Bangalore
* Mumbai
* Delhi NCR

### Casual Dining & Hotel Dining

* Indore

### Bars & Pubs

* Bangalore
* Mumbai
* Delhi NCR
* Indore

This split helps in understanding how restaurant data and page structures differ across cities and dining types.

---

## Tech Stack Used

The project uses a minimal and practical scraping stack focused on real-world usage:

* **Python** – Core programming language
* **Requests** – For handling HTTP requests
* **JSON / CSV** – For storing scraped data
* **Browser DevTools** – To inspect network calls, headers, and cookies

The scraping logic is based on **request-level data extraction**, not HTML parsing libraries, making it closer to how modern sites are scraped.

---

## Scraping Workflow (Conceptual)

1. Identify city-wise and category-wise restaurant listing pages
2. Capture required network requests using browser developer tools
3. Send requests with updated headers and cookies
4. Extract restaurant details from responses
5. Handle pagination and multiple listings
6. Store data in a structured format

The goal is to understand **how data flows behind the scenes**, rather than relying only on static HTML scraping.

---

## Headers & Cookies Handling

> **Important:** Headers and cookies must be updated regularly.

EazyDiner uses dynamic request validation mechanisms. To reduce blocking:

* Update cookies based on the current browser session
* Modify request headers according to the day/session
* Avoid aggressive request frequency
* Keep request behavior close to normal browsing patterns

This project intentionally highlights this step so learners understand **why scraping may fail and how to fix it**.

---

## Purpose of This Repository

This project can be used as:

* A **reference project for web scraping learners**
* Practice material for handling real, dynamic websites
* A base for restaurant or food-tech data collection projects
* A **portfolio project** demonstrating practical scraping logic

It is meant for **learning and experimentation**, not as a production-ready scraper.

---

## Disclaimer

* This project is created **strictly for educational purposes**
* All data belongs to the respective platform
* Do not use this repository for commercial scraping
* Always respect website terms, policies, and fair usage rules

---

## Final Thoughts

Web scraping is not just about extracting data —
it’s about understanding requests, adapting to change, and scraping responsibly.

If this project helps you understand even one real-world scraping challenge, it has served its purpose.

Happy Scraping 🚀
