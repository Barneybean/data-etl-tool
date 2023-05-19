-- create a dwh.membership table that match the output columns from the etl.py with primary key using customer_id
-- columns 'customer_id', 'first_name', 'last_name', 'original_customer_id', 'dob','company_name','last_active','score','member_since','state', 'source_org', 'created_at','updated_at', 'deleted_at'
CREATE TABLE IF NOT EXISTS public.test_table
(
    id varchar(255) NOT NULL,
    name varchar(255) NOT NULL,
    age numeric,
    CONSTRAINT test_table_pkey PRIMARY KEY (id) 
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.test_table
    OWNER to postgres;