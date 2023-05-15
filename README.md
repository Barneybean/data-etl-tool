# data-etl-tool
A ETL tool that reads text files in chunk, mung and output to new csv files and ingest data to db

    1. It reads text files in chunk from two files, mung raw data then output data incrementally to output text files

    2. At the same time, it will load the processed chunk data into postgres database


To install the app:
    open your terminal
    ``` cd ```
    ``` git clone [link] ```
    if you want to run the app from a branch then ``` git checkout hh_take_home ```
    ``` brew install pipenv ``` (skip this step if you have pipenv installed already. If you do not have brew installed then follow the instruction here: https://docs.brew.sh/Installation)

To set up:
    run the following shell command in your terminal
    ```source script/setup```
    create environment file to store your database connection variables
    ```touch .env```
    ```open .env```
    then copy the following variable names and update them with your db connections
    ```
    POSTGRES_DATABASE=[replace with your database]
    POSTGRES_USER=[replace with your username]
    POSTGRES_PASSWORD=[replace with your password]
    POSTGRES_HOST=[replace with your host]
    POSTGRES_PORT=[replace with your port]
    ```

To enter the pipenv environment:
    ```source script/start```

To Execute the app:
    ```pipenv run python app.py```

To make sure SQLs are to the standard:
    cd to the query folder
    ```sqlfluff lint [replace this with sql file path] --dialect postgres ```
    ie: sqlfluff lint '/Users/williamgao/data-etl-tool/query/model_companies.sql' --dialect postgres

    To auto fix the format, just chaneg the "lint" to "fix"
    ```sqlfluff fix [replace this with sql file path] --dialect postgres ```

Please contact me if you have any questions

William Gao

seewilliam.gao@gmail.com
