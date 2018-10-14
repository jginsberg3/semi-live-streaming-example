## (Semi)-Real-Time Data Logging and Plotting

This is an example of creating fake log data using ZMQ, capturing and writing that data to rotating log files, storing the log data in a SQLite database, and plotting the results in semi-real-time using a Plotly Dash webapp.

Followed this video tutorial for the log creation and capture piece: https://youtu.be/ObnDarg9CAU.

Plotly Dash info here: https://plot.ly/products/dash/

An environment.yml file is provided instead of requirements.txt as I used a conda environment for development.  The log server, reciever, and storer are all in Jupyter Notebooks although could easily be convertered to and run from .py files.  The Dash app lives in a .py file.  

## Instructions:

- First start the tick_server notebook.
- Then start the tick_client-reciever notebook.  This will create log_a.txt and log_b.txt files.
- Then start the tick_client-storer notebook.  This will create the db.sqlite database.
- Finally, after the db.sqlite database has been created, run the dash_app.py.  This will launch the Plotly Dash app.

In the future, I would like to expand this project to plot in actual real-time will still maintaining some of the resiliency of capturing the data and writing to logs first rather than directly to the sqlite db.
