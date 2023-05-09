# data-etl-tool
A ETL tool that reads text files in chunk, mung and output to new csv files and ingest data to db 

    1. It reads text files in chunk from two files, mung raw data then output data incrementally to output text files  

    2. At the same time, it will load the processed chunk data into postgres database  


To install the app:  
    open your terminal   
    ``` cd ```  
    ``` git clone [link] ```  
    ``` brew install pipenv ``` (skip this step if you have pipenv installed already. If you do not have brew installed then follow the instruction here: https://docs.brew.sh/Installation)

To set up:  
    run the following shell command in your terminal  
    ```source setup```

To enter the pipenv environment:  
    ```source start```

To Execute the app:     
    ```pipenv run python app.py```

Please contact me if you have any questions  

William Gao  

seewilliam.gao@gmail.com
