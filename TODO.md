# Next Step

## Notes:
1. For simplicity given time constraints, I am using the sql create statement in the query folder to create data models in db, in long term, I will need to use sqlalchemy library to build out the data model objects
2. Given the time constraints, I did not write unit test for all the functions. At work, I would write unite tests for all functions ideally

## Data related issues to solve as next step
1. Clean up the membership data loaded in the database Validate unique customer and consolidate if same customer apears in both file sources. verify company id if the two clubs shows conflict details for the same customer
2. Sync scoring for the customers from two companies and maybe create a new scoring system to score the customers
3. Create score history table if there is a need to track last active date and score history
4. The requirement asked me to replace the company_id with company_name, but I think it would make sense to normalize the membership table to show company_id and maitain a dimmension table: public.companies
5. If raw data needs to be stored in the database, I would recommend loading the raw_data files into S3 bucket or ingest as is into the database for future reference (Or load file to S3)
6. Update data model to allow middle name, preferred name.


## Software Enhancements:
1. Move all the non sensitive variables into config.yml files
2. ** Create the the remaining of the CRUD process for both output file and the database.
3. ** Create data partitioon and index the tables to improve the read performance of the tables
4. ** Improve the ingestion process where data with conflit to the table primary key will be skipped. Method, query the table with primary key from the dataframe before ingestion, return
primary keys that is not in the db then remove those rows from dataframe then ingest to db
5. Create a dev, staging and prod database, add a toggle in the software to switch between them for different phrase of product life cycle
6. ** Set data governance policy and implement gatekeeping for the PII data
7. [Added] Implement linting tool such as sqlfluff, quality control tool such as pre-commit
8. Connect to gdrive to read data so the software can execute shared files
9. Schedule the job on airflow if the process needs to happen periodically
10. Add unit test for all utils functions
11. ** Log information to Datadog or similar logging tools currently in use
