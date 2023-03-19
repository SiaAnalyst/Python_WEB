# Homework #10

In the previous homework, you scraped the website http://quotes.toscrape.com.

You need to implement an analog of this site in Django.

- Implement the ability to register on the site and log in to the site.
- The ability to add a new author to the site only for a registered user.
- The ability to add a new quote to the site with the author's indication only for a registered user.
- Migrate the database you have from MongoDB to Postgres for your site. You can implement it with a custom script. (If you want, you can leave and work with citations and authors in MongoDB, and with users in Postgres)
- You can visit the page of each author without user authentication
- All citations are available for viewing without user authentication

## Additional part
- Implement the search for quotes by tags. When you click on a tag, a list of quotes with this tag is displayed.
- Implement the Top Ten tags block and display the most popular tags.
- Implement pagination. These are the next and previous buttons
- Instead of transferring data from the MongoDB database, implement the ability to scrape data directly from your site by clicking a certain button on the form and fill the site database.